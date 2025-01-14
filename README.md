# ClassiFood

End-to-end project for simple classification food project

## TODO

- [X] Find dataset
- [X] Exploratory Data Analysis (EDA)
- [X] Training model
  - [X] An end-to-end pipeline for training
  - [X] ResNet
  - [X] EfficientNet
  - [X] Ensemble learning
- [X] Web app
  - [X] Setup streamlit
  - [X] Setup FastAPI
- [X] Deployment
  - [X] Docker

## Dataset

The dataset for this project is the [Food-101 dataset](https://www.kaggle.com/datasets/kmader/food41) from Kaggle. It contains 101,000 images across 101 different food categories. Each category has 1,000 images (750 training, 250 testing).

You can also check other datasets in the [Source of Datasets](training/data-preparation/SOURCE.md) file.

## Exploratory Data Analysis (EDA)

The EDA for this project is in the [EDA notebook](training/data-preparation/EDA.ipynb) file.

**TL;DR**:

- 101 classes with 1000 images each
- 75% training and 25% testing
- Various image sizes (mostly 512x512)

## Training
[![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/code/phandai/food101-training)

Model: ResNet, EfficientNet

For detailed information on model training, refer to the [Training README](training/model-training/README.md).

## Inference
[![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/code/phandai/food101-inference)

You can check the inference pipeline in the [inference script](training/model-evaluation/inference-script.ipynb) file.

## Model Evaluation

For detailed information on model evaluation, refer to the [Evaluation README](training/model-evaluation/README.md).

## App

The application consists of a backend built with FastAPI and a frontend built with Streamlit. The backend handles image classification tasks using various pre-trained models, while the frontend allows users to upload images, select models, and get predictions.

For detailed information on the backend, refer to the [Backend README](app/backend/README.md).
For detailed information on the backend, refer to the [Frontend README](app/frontend/README.md).

### Running the App

To run the backend, use the following command:

```bash
cd app/backend
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

To run the frontend, use the following command:

```bash
cd app/frontend
pip install -r requirements.txt
streamlit run app.py
```

<!-- ### Docker Deployment

To make it easier for others to run the app, you can use Docker. Follow these steps:

1. **Create a Dockerfile for the backend**:

```dockerfile
// filepath: /d:/Project/ProjectBasedLearning/ComputerVision/ImageClassification/ClassiFood/app/backend/Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

2. **Create a Dockerfile for the frontend**:

```dockerfile
// filepath: /d:/Project/ProjectBasedLearning/ComputerVision/ImageClassification/ClassiFood/app/frontend/Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
```

3. **Create a `docker-compose.yml` file**:

```yaml
// filepath: /d:/Project/ProjectBasedLearning/ComputerVision/ImageClassification/ClassiFood/docker-compose.yml
version: '3.8'

services:
  backend:
    build:
      context: ./app/backend
    ports:
      - "8000:8000"
    volumes:
      - ./app/backend:/app

  frontend:
    build:
      context: ./app/frontend
    ports:
      - "8501:8501"
    volumes:
      - ./app/frontend:/app
    depends_on:
      - backend
```

4. **Build and run the containers**:

```bash
docker-compose up --build
```

This will start both the backend and frontend services. The backend will be accessible at `http://localhost:8000` and the frontend at `http://localhost:8501`. -->
