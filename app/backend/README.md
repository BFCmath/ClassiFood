# Backend Overview

This backend is designed to handle image classification tasks using various pre-trained models. It is built using FastAPI and supports model loading, image preprocessing, and prediction.

## Directory Structure

- `app/main.py`: The main entry point for the FastAPI application.
- `app/utils/load_classes.py`: Utility functions for loading class names.
- `app/utils/load_model.py`: Utility functions for loading models.
- `app/utils/base_model.py`: Base class for all models.
- `app/models/`: Directory containing model implementations.
- `app/metadata.json`: Metadata for available models.

## How It Works

### Model Metadata

The `metadata.json` file contains information about the available models, including their names, model IDs, weight paths, and model paths. This metadata is used to dynamically load the models.

### Model Loader

The `ModelLoader` class in `load_model.py` is responsible for loading models based on the metadata. It uses Python's `importlib` to dynamically import and instantiate model classes.

### Base Model

The `BaseModel` class in `base_model.py` defines the interface that all models must implement. It includes methods for loading the model, preprocessing images, and performing predictions.

### Models

Each model implementation (e.g., ResNet50, EfficientNet) resides in its own directory under `app/models/`. These implementations inherit from the `BaseModel` class and provide specific methods for loading the model, preprocessing images, and performing predictions.

### FastAPI Endpoints

- `GET /models`: Returns a list of available models.
- `GET /classes`: Returns the class names used by the models.
- `POST /predict`: Accepts an image and a model ID, preprocesses the image, performs prediction, and returns the results.

## Running the Backend

To run the backend, use the following command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

This will start the FastAPI application on port 8000.

## Example Usage

1. **Get Available Models**:

   ```bash
   curl -X GET "http://localhost:8000/models"
   ```

2. **Get Class Names**:

   ```bash
   curl -X GET "http://localhost:8000/classes"
   ```

3. **Perform Prediction**:

   ```bash
   curl -X POST "http://localhost:8000/predict" -F "image=@path_to_image.jpg" -F "model_id_name=resnet50"
   ```

This will return the prediction results for the given image using the specified model.
