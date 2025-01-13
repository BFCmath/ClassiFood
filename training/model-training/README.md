# Model Training

## Model Selection

For this project, I decided to use multiple models to compare their performance. The models I chose are:

- ResNet
- EfficientNet

I chose these models because they are widely used in image classification tasks and have shown good performance in many benchmarks and competitions.

Additionally, we can use pretrained weights to speed up the training process (Transfer Learning).

## Training Techniques

You can check the end-to-end training pipeline in the [training script](training-script.ipynb) file.

### Ensemble Learning

For each model architecture, I trained multiple versions of the model with different hyperparameters and data augmentation techniques. This helps with hyperparameter tuning and data augmentation selection.

For each version of a model, I used 5-fold cross-validation to evaluate the model's performance, and then I aggregated those 5 predictions to get the final performance.

Finally, I combined the predictions of different models to improve the overall performance.

### Data Augmentation

I applied various data augmentation techniques, from simple to advanced, to improve the model's performance.

Check the data augmentation techniques for each model in the [config](config) folder.

For advanced data augmentation, check the [Mixup and CutMix implementation](Mixup&CutMix.ipynb).

## Configuration

You can check the configuration for each model in the [config](config) folder.
