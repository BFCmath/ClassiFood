from ...utils.base_model import BaseModel
import albumentations as A
import timm
from albumentations.pytorch import ToTensorV2
from PIL import Image
import io
import numpy as np
import torch

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
        
    def preprocess(self, image_bytes):
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        image = np.array(image)
        image = self.transforms(image=image)["image"]
        return image.unsqueeze(0)

    def predict(self, preprocessed_image):
        # Perform inference and return both hard and soft predictions
        self.model.eval()
        with torch.no_grad():
            outputs = self.model(preprocessed_image)
            probabilities = torch.nn.functional.softmax(outputs, dim=1)
            _, predictions = torch.max(outputs, 1)
            return predictions.item(), probabilities.squeeze().numpy()
