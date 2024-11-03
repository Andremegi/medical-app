# main.py
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permettre l'accès depuis toutes les origines (changer "*" pour un domaine spécifique)
    allow_credentials=True,
    allow_methods=["*"],  # Permettre tous les types de requêtes (GET, POST, etc.)
    allow_headers=["*"],  # Permettre tous les headers
)

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    save_directory = "uploaded_files"
    os.makedirs(save_directory, exist_ok=True)
    file_path = os.path.join(save_directory, file.filename)

    # Enregistrer l'image sur le serveur
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename, "path": file_path}
