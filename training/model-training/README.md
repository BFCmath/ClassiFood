# Model training

## Model selection

For this project, I decided to use many models to compare their performance. The models I chose are:

+ ResNet
+ EfficientNet

I chose these models because they are widely used in the image classification task and have shown good performance in many benchmarks/competitions.

Also we can use pretrained weight to speed up the training process. (Transfer learning)

## Training techniques

You can check the end-to-end training pipeline in the [training script](training-script.ipynb) file.

### Ensemble learning

For each model architecture, I trained multiple versions of the model with different hyperparameters and data augmentation techniques. This helps hyperparameter tuning and data augmentation selection.

For each version of a model, I used 5-fold cross-validation to evaluate the model's performance, and then I aggregated those 5 predictions to get the final performance.

Finally, I used combine the predictions of many different models to improve the overall performance. (TODO)

### Data augmentation

Apply from simple to advanced data augmentation techniques to improve the model's performance.

Check the data augmentation techniques for each model in the [config](config) folder.

TODO: Mixup, CutMix, etc.

## Configuration

You can check the configuration for each model in the [config](config) folder.
