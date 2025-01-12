# ClassiFood

End-to-end project for simple classification food project

## TODO

- [X] Find dataset
- [X] Exploratory Data Analysis (EDA)
- [ ] Training model
  - [X] An end-to-end pipeline for training
  - [X] ResNet
  - [X] EfficientNet
  - [ ] Ensemble learning
- [ ] Web app
  - [ ] Setup streamlit
  - [X] Setup FastAPI
- [ ] Deployment
  - [ ] Docker

## Dataset

The dataset for this project is the [Food-101 dataset](https://www.kaggle.com/datasets/kmader/food41) from Kaggle. It contains 101,000 images across 101 different food categories. Each category has 1,000 images (750 training, 250 testing).

You can also check other datasets in the [Source of Datasets](training/data-preparation/SOURCE.md) file.

## Exploratory Data Analysis (EDA)
[![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/code/phandai/eda-food101)

The EDA for this project is in the [EDA notebook](training/data-analysis/eda-food101.ipynb) file.

**TL;DR**:

- 101 clases with 1000 images each
- 75% training and 25% testing
- Various image sizes (mostly 512x512)

## Training
[![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/code/phandai/food101-training)

Model: ResNet, EfficientNet

## Inference
[![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/code/phandai/food101-inference)

You can check the inference pipeline in the [inference script](training/model-evaluation/inference-script.ipynb) file.

<!-- 
- ensemble learning between models
- Finish README.md
- Learn FastAPI -->
