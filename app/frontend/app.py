import streamlit as st
import requests
from PIL import Image
import io

# Backend API URL
API_URL = "http://localhost:8000"

# Title
st.title("Food Image Classification App")

# Image Upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Fetch available models from backend
@st.cache
def fetch_models():
    response = requests.get(f"{API_URL}/models")
    if response.status_code == 200:
        return response.json()["models"]
    return []

models = fetch_models()
model_options = [model["name"] for model in models]
model_ids = {model["name"]: model["id"] for model in models}

# Model Selection
selected_model = st.selectbox("Select Model", model_options)

# Predict Button
if st.button("Predict"):
    if uploaded_file is not None:
        # Read image
        image = Image.open(uploaded_file)
        buffered = io.BytesIO()
        image.save(buffered, format="JPEG")
        img_bytes = buffered.getvalue()

        # Prepare multipart/form-data
        files = {
            "image": ("image.jpg", img_bytes, "image/jpeg"),
        }
        data = {
            "model_id": model_ids[selected_model]
        }

        # Send POST request to backend
        response = requests.post(f"{API_URL}/predict", files=files, data=data)

        if response.status_code == 200:
            results = response.json()["results"]
            st.image(image, caption='Uploaded Image.', use_column_width=True)
            st.write("### Prediction Results:")
            for cls, prob in results:
                st.write(f"{cls}: {prob*100:.2f}%")
        else:
            st.error("Prediction failed. Please try again.")
    else:
        st.warning("Please upload an image.")
