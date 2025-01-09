# ClassiFood

End-to-end project for simple classification food project

## TODO

- [X] Find dataset
- [X] Exploratory Data Analysis (EDA)
- [ ] Training model
  - [X] An end-to-end pipeline for training
  - [X] ResNet
  - [ ] EfficientNet
  - [ ] Inception
  - [ ] Xception
  - [ ] ViT
- [ ] Web app
  - [ ] Streamlit
  - [ ] FastAPI
- [ ] Deployment
  - [ ] Docker

## Dataset

The dataset for this project is the [Food-101 dataset](https://www.kaggle.com/datasets/kmader/food41) from Kaggle. It contains 101,000 images across 101 different food categories. Each category has 1,000 images (750 training, 250 testing).

You can also check other datasets in the [Source of Datasets](training/data-preparation/SOURCE.md) file.

## Exploratory Data Analysis (EDA)

The EDA for this project is in the [EDA notebook](training/data-preparation/EDA.ipynb) file.

**TL;DR**:

- 101 clases with 1000 images each
- 75% training and 25% testing
- Various image sizes (mostly 512x512)

<!-- https://www.kaggle.com/code/phandai/eda-food101 -->

## Training

Model: ResNet
