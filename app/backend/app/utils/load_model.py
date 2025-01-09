from importlib import import_module

class ModelLoader:
    def __init__(self, metadata):
        self.metadata = metadata
        self.models = {}

    def get_model(self, model_id_name):
        if model_id_name in self.models:
            return self.models[model_id_name]
        
        model_info = next((m for m in self.metadata if m["model_id_name"] == model_id_name), None)
        if not model_info:
            return None
        
        module_path = model_info["model_path"].replace("/", ".").replace(".py", "")
        model_module = import_module(module_path)
        model_class = getattr(model_module, model_info["name"])
        model_instance = model_class()
        self.models[model_id_name] = model_instance
        return model_instance