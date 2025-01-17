# Frontend Overview

The frontend is built using Streamlit and allows users to upload images, select models, and get predictions for food image classification.

## Features

- Image upload
- Model selection
- Top K predictions
- Boosting predictions option (trade-off between speed and accuracy)

## Running the Frontend Locally

To run the frontend locally, use the following command:

```bash
streamlit run app.py
```

## Running the Frontend with Docker

To run the frontend using Docker, follow these steps:

1. **Pull the Docker image**:

   ```bash
   docker pull bfcmath/classifood-frontend:1.0
   ```

2. **Run the container**:

   ```bash
   docker run --name frontend --network app-network -p 8501:8501 -e DOCKER_ENV=true bfcmath/classifood-frontend:1.0
   ```

3. **Build and run the container (Optional)**:

   If you want to build the image locally, you can use the following command:

   ```bash
   docker-compose up --build frontend
   ```

This will start the frontend service and it will be accessible at `http://localhost:8501`.

## Example Usage

1. **Upload an Image**: Choose an image file (jpg, jpeg, png).
2. **Select Model**: Choose a model from the dropdown.
3. **Select Top K Predictions**: Adjust the slider for the number of top predictions.
4. **Enable Boosting**: Check the box for more accurate predictions.
5. **Predict**: Click the "Predict" button to get the results.

The prediction results will be displayed with the class names and their respective probabilities.
