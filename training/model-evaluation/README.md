# Model Evaluation

You can check the inference pipeline in the [inference script](inference-script.ipynb) file.

## ResNet

The table below shows the performance of each version of the ResNet model on the test set, using 5-fold cross-validation.

The validation accuracy is calculated by using each fold model to predict the validation set in that fold and concatenating them to get the final prediction on 5 validation folds.

Each fold model is then used to predict the test set, and the average of the 5 test set predictions is calculated (Test Avg).

| Version     | Val          | Test Fold 1 | Test Fold 2 | Test Fold 3 | Test Fold 4 | Test Fold 5 | Test Avg   |
|-------------|--------------|-------------|-------------|-------------|-------------|-------------|------------|
| ResNet v1   | 0.77048      | 0.81378217  | 0.8167920   | 0.8169900   | 0.8194851   | 0.81940594  | 0.81940    |
| ResNet v2   | 0.77301      | 0.8208712   | 0.8202376   | 0.81774257  | 0.82269306  | 0.82356435  | 0.82356435 |
| ResNet v3   | 0.7730429    | 0.8228118   | 0.82063366  | 0.81726732  | 0.81861386  | 0.81996039  | 0.81996039 |
| ResNet v4   | 0.7859669    | 0.8197227   | 0.83679207  | 0.83885148  | 0.83532673  | 0.83992079  | 0.83992079 |

The table below shows the performance using confidence-weighted prediction ([CWP](CWP.ipynb)) and Test Time Augmentation ([TTA](TTA.ipynb)) on the test set.

The validation accuracy is the same. For each fold model, I used TTA8 to predict the test set, and the final test accuracy is calculated using confidence-weighted prediction.

| Version     | Val          | Test Fold 1 | Test Fold 2 | Test Fold 3 | Test Fold 4 | Test Fold 5 | Test CFW   |
|-------------|--------------|-------------|-------------|-------------|-------------|-------------|------------|
| ResNet v4   | 0.7859669    | 0.83750495  | 0.85398019  | 0.85421782  | 0.85069306  | 0.855168316 | 0.88059405 |
| ResNet v5   | 0.8021122    | 0.85580198  | 0.86245544  | 0.86071287  | 0.86304950  | 0.86384158  | 0.88249505 |
| ResNet v6   | 0.819524752  | 0.874059405 | 0.875445544 | 0.8773465346 | 0.8753267326 | 0.87655445  | 0.88823762 |

NOTE: The 6th version of ResNet is the same as the 5th version, but I used Mixup and Cutmix data augmentation techniques.

P/S: Thanks to Saber (aka Mai Duc Minh Huy) for the idea of confidence-weighted prediction.

## EfficientNet

| Version     | Val          | Test Fold 1 | Test Fold 2 | Test Fold 3 | Test Fold 4 | Test Fold 5 | Test CFW   |
|-------------|--------------|-------------|-------------|-------------|-------------|-------------|------------|
| EffNet v1   | 0.81436303   | 0.85390099  | 0.8536237   | 0.855960396 | 0.853346534  | 0.851089108 | 0.885425742 |
| EffNet v2   | 0.818693069  | 0.8560396   | 0.8629306   | 0.860910891 | 0.85405940  | 0.854019801 | 0.88451485 |
| EffNet v3   | 0.83973597   | 0.88724754  | 0.892594059 | 0.8852673267 | 0.88895049  | 0.8902970297 | 0.91160396 |
| EffNet v4   | 0.84869966   | 0.898455445 | 0.898970297 | 0.89750495  | 0.89556435  | 0.8982970297 | 0.91382178 |

## Forward Selection Ensemble

Version: EffNet v4, ResNet v3  
Weight: 1.0, 0.44444444  
Results:  

- Val: 0.8587
- Test: 0.9160396
