from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from text_data.model import predict_disease
import shutil
import os

from images.logic.model import load, predict

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],  # Permettre l'accès depuis toutes les origines (changer "*" pour un domaine spécifique)
    allow_credentials=True,
    allow_methods=["*"],  # Permettre tous les types de requêtes (GET, POST, etc.)
    allow_headers=["*"],  # Permettre tous les headers
)

# Preload model and keep it in state
app.state.model = load()

@app.get('/')
def root():
    return {'hello': 'team'}

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    dir_path = os.path.dirname(__file__)
    image_folder_path = os.path.join(dir_path, "uploaded_files")

    os.makedirs(image_folder_path, exist_ok=True)
    image_path = os.path.join(image_folder_path, file.filename)

    # Enregistrer l'image sur le serveur
    with open(image_path, "wb") as buffer:
        content = await file.read()  # Read the file's content in memory
        buffer.write(content)  # Write content to the local file

    # Predicting
    model = app.state.model

    best_label, predictions_per_label = predict(model, image_path)
    print(f"Predicted label: {best_label}")
    print(f"Predicted probabilities: {predictions_per_label}")

    os.remove(image_path)

    return {"best_label": best_label, "predictions_per_label": predictions_per_label}


@app.get('/symptoms')
def predict(symptoms):
    prediction , probability = predict_disease(symptoms)
    print('disease', prediction)
    return {'disease': prediction, 'probability': str(probability)}
