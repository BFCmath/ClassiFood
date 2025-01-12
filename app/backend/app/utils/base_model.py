from abc import ABC, abstractmethod
class BaseModel(ABC):
    def __init__(self, model_id_name, name, weight_path, num_classes):
        self.model_id_name = model_id_name
        self.name = name
        self.weight_path = weight_path
        self.num_classes = num_classes
        self.model = self.load_model()

    @abstractmethod
    def load_model(self):
        """Load the model weights and prepare the model for inference."""
        pass

    @abstractmethod
    def preprocess(self, image_bytes):
        """Preprocess the input image bytes and return a tensor."""
        pass

    @abstractmethod
    def predict(self, preprocessed_image):
        """Perform inference on the preprocessed image and return predictions."""
        pass
