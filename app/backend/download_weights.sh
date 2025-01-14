#!/bin/bash

# Download the dataset
kaggle datasets download -d phandai/classifoodweight

# Unzip the downloaded file
unzip classifoodweight.zip

# Ensure the directories exist
mkdir -p app/models/efficientnet
mkdir -p app/models/resnet50

# Move the weights to the correct directories
mv efficientnet.pth app/models/efficientnet/weight.pth
mv resnet.pth app/models/resnet50/weight.pth

# Clean up
rm classifoodweight.zip
