# Frontend Overview

The frontend is built using Streamlit and allows users to upload images, select models, and get predictions for food image classification.

## Features

- Image upload
- Model selection
- Top K predictions
- Boosting predictions option (trade-off between speed and accuracy)

## Running the Frontend

To run the frontend, use the following command:

```bash
streamlit run app.py
```

## Example Usage

1. **Upload an Image**: Choose an image file (jpg, jpeg, png).
2. **Select Model**: Choose a model from the dropdown.
3. **Select Top K Predictions**: Adjust the slider for the number of top predictions.
4. **Enable Boosting**: Check the box for more accurate predictions.
5. **Predict**: Click the "Predict" button to get the results.

The prediction results will be displayed with the class names and their respective probabilities.
