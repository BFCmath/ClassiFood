# Model training

## Model selection

For this project, I decided to use many models to compare their performance. The models I chose are:

+ ResNet
+ EfficientNet

I chose these models because they are widely used in the image classification task and have shown good performance in many benchmarks/competitions.

Also we can use pretrained weight to speed up the training process. (Transfer learning)

## Training techniques

## Ensemble learning
For each model, I will train it many times, each time with different hyperparameters. This serves two purposes:

+ Hyperparameter tuning: Find the best hyperparameters for each model.
+ Ensemble learning: Train multiple models with different hyperparameters and combine their predictions to get better performance. (TODO)

Also, I used OOF (Out-of-Fold) technique to prevent overfitting and get a better estimate of the model's performance. Besides, I can use this technique to ensemble models (with the same parameters but have different training/val data).

Moreover, I can ensemble models with different architectures (ResNet, EfficientNet) to get better performance. (TODO)

## Data augmentation

Just simple image augmentation techniques.
TODO: Mixup, CutMix, etc.

## TTA (Test Time Augmentation)

TODO
