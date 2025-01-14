import importlib
from app.utils.base_model import BaseModel

class ModelLoader:
    def __init__(self, model_metadata, num_classes):
        self.model_metadata = model_metadata
        self.num_classes = num_classes
        self.models = {}

    def get_model(self, model_id_name):
        if model_id_name in self.models:
            return self.models[model_id_name]

        model_info = next((m for m in self.model_metadata if m["model_id_name"] == model_id_name), None)
        if not model_info:
            return None

        module_path = model_info["model_path"].replace("/", ".").replace(".py", "")
        model_module = importlib.import_module(module_path)
        model_class = getattr(model_module, model_info["class_name"])
        model_instance: BaseModel = model_class(model_info["model_id_name"], model_info["name"], model_info["weight_path"], self.num_classes)
        model_instance.load_model()
        self.models[model_id_name] = model_instance
        return model_instance