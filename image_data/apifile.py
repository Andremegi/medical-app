from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from image_data.model import im_transformation
import os
from PIL import Image

ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()

@app.get("/")
def root():
    return {'hello':'team'}

@app.get("/transform")
def transform(image):
    return im_transformation(image)


@app.post("/items/")
async def create_item(item: Item):
    return item.name


@app.get("/uploadfile")
def create_upload_file(file, image_name):

    image_folder_path = os.path.join(ROOT_PATH, 'image_data', 'uploaded_images', f'{image_name}.jpg')

    file.save(image_folder_path, 'JPEG')

    print(f'Image is saved under the name {image_name} ')
    pass

@app.get("/predict")
def predict(file):

    """ Calls the model.predict funtion to make predictions on api and stremalit """
    pass

#RESUME
# EVEN THOUGHT THE RESPONSE IS A DICTIONARY YOU ACCES THE KEYS WITH .name_key
# HAD TO RUN PIP INSTALL PYTHON MULTIPART TO MAKE IT WORK
