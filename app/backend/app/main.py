from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json
from app.utils.load_model import ModelLoader
from app.utils.load_classes import load_classes

app = FastAPI()
CLASS_NAME_PATH = "not found yet"
# Allow CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model metadata
with open('app/metadata.json') as f:
    model_metadata = json.load(f)

# Load classes once
classes = load_classes()

# Initialize Model Loader
model_loader = ModelLoader(model_metadata, len(classes))

@app.get("/")
def get_test():
    return {"message": "Hello World"}

@app.get("/models")
def get_models():
    return {"models": [{"id": m["model_id_name"], "name": m["name"]} for m in model_metadata]}

@app.get("/classes")
def get_classes():
    return {"classes": classes}

@app.post("/predict")
async def predict(image: UploadFile = File(...), model_id_name: str = Form(...), tta: bool = Form(False)):
    # Load the selected model
    model = model_loader.get_model(model_id_name)
    if not model:
        return {"error": "Model not found"}

    # Read image file
    image_bytes = await image.read()

    # Preprocess image
    preprocessed_image = model.preprocess(image_bytes)

    # Perform prediction
    prediction, probabilities = model.predict(preprocessed_image, tta=tta)

    # Convert numpy.float32 to native Python types
    probabilities = probabilities.tolist()

    # Sort results
    sorted_results = sorted(zip(classes, probabilities), key=lambda x: x[1], reverse=True)

    return {"results": sorted_results}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
