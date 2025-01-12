import streamlit as st
import requests
from PIL import Image
import io

# Set page configuration
st.set_page_config(layout="wide")

# Backend API URL
API_URL = "http://localhost:8000"

# Title
st.title("Food Image Classification App")

# Fetch available models from backend
@st.cache_data
def fetch_models():
    response = requests.get(f"{API_URL}/models")
    if response.status_code == 200:
        return response.json()["models"]
    return []

models = fetch_models()
model_options = [model["name"] for model in models]
model_ids = {model["name"]: model["id"] for model in models}

# Layout
left_column, right_column = st.columns(2)

# Right Column: Predict button, Model Selection, and Top K slider
with right_column:
    button_column, model_column, top_k_column = st.columns([1, 1, 1])  # Adjust the width ratio as needed

    # Top K Slider in the first part of the row
    with top_k_column:
        top_k = st.slider("Select Top K Predictions", min_value=1, max_value=20, value=5)

    # Center the Model Selection
    with model_column:
        selected_model = st.selectbox("Select Model", model_options)

    # Center the Predict Button
    with button_column:
        predict_button = st.button("Predict", key="predict_button", type="primary")

# Left Column: Image upload and other options
with left_column:
    # Image Upload
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    # Render image after user chooses it
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_container_width=True)


# Handle Predictions
if predict_button:  # Check if the button is clicked
    if uploaded_file is not None:
        # Read image
        buffered = io.BytesIO()
        image.save(buffered, format="JPEG")
        img_bytes = buffered.getvalue()

        # Prepare multipart/form-data
        files = {
            "image": ("image.jpg", img_bytes, "image/jpeg"),
        }
        data = {
            "model_id_name": model_ids[selected_model]
        }

        # Send POST request to backend
        response = requests.post(f"{API_URL}/predict", files=files, data=data)

        if response.status_code == 200:
            results = response.json()["results"]
            with right_column:
                st.write("### Prediction Results:")
                for cls, prob in results[:top_k]:
                    st.markdown(f"""
                    <div style="margin-bottom: 16px; padding: 8px; border: 1px solid #ddd; border-radius: 8px;">
                        <div style="font-weight: bold; text-align: left; margin-bottom: 4px;">{cls}</div>
                        <div style="display: flex; align-items: center;">
                            <progress style="width: 100%; height: 20px;" value="{prob*100}" max="100"></progress>
                        </div>
                        <div style="text-align: right; font-size: 0.9em; margin-top: 4px;">{prob*100:.2f}%</div>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.error("Prediction failed. Please try again.")
    else:
        st.warning("Please upload an image.")
