from ...utils.base_model import BaseModel
import albumentations as A
import timm
from albumentations.pytorch import ToTensorV2
from PIL import Image
import io
import numpy as np
import torch
import torchvision.transforms as T

class EfficientNet(BaseModel):
    def __init__(self, model_id_name, name, weight_path, num_classes):
        super().__init__(
            model_id_name=model_id_name,
            name=name,
            weight_path=weight_path,
            num_classes=num_classes 
        )
        self.resized_height = 380
        self.resized_width = 380
        self.transforms = self.get_transforms()
        self.tta_transforms = self.get_tta_transforms()

    def load_model(self):
        model = timm.create_model(self.model_id_name, num_classes=self.num_classes, pretrained=True)
        checkpoint = torch.load(self.weight_path, map_location=torch.device('cpu'), weights_only=False)
        model.load_state_dict(checkpoint['model_state_dict'])
        return model.to('cpu') # Only use CPU
    
    def get_transforms(self):
        return A.Compose([
            A.Resize(height=self.resized_height, width=self.resized_width),
            A.Normalize(
                mean=(0.485, 0.456, 0.406), 
                std=(0.229, 0.224, 0.225), 
                max_pixel_value=255.0
            ),
            ToTensorV2(),
        ])
    
    def get_tta_transforms(self):
        return [
            lambda x: x,  # Original
            lambda x: T.functional.hflip(x),  # Horizontal flip
            lambda x: T.functional.vflip(x),  # Vertical flip
            lambda x: T.functional.vflip(T.functional.hflip(x)),  # Both flips
            lambda x: T.functional.rotate(x, 90),  # 90 degrees
            lambda x: T.functional.rotate(x, 180),  # 180 degrees
            lambda x: T.functional.rotate(x, 270),  # 270 degrees
            lambda x: T.functional.rotate(T.functional.hflip(x), 90)  # Horizontal flip + 90 degrees
        ]
        
    def preprocess(self, image_bytes):
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        image = np.array(image)
        image = self.transforms(image=image)["image"]
        return image.unsqueeze(0)

    def predict(self, preprocessed_image, tta=False):
        self.model.eval()
        with torch.no_grad():
            if tta:
                batch_preds = []
                for transform in self.tta_transforms:
                    augmented_data = transform(preprocessed_image)
                    outputs = self.model(augmented_data)
                    batch_preds.append(torch.softmax(outputs, dim=1))
                avg_preds = torch.stack(batch_preds).mean(dim=0)
                probabilities = avg_preds
                _, predictions = torch.max(avg_preds, 1)
            else:
                outputs = self.model(preprocessed_image)
                probabilities = torch.nn.functional.softmax(outputs, dim=1)
                _, predictions = torch.max(outputs, 1)
            return predictions.item(), probabilities.squeeze().numpy()
