
from PIL import Image

def im_transformation(image):
    if image is not None :
        # image_file = Image.open(image) # open colour image
        image_file = image.convert('1')
        return image_file
    else:
        return 'Sorry , the process couldnt be done :( )'

def preprocessing(file):
    """Preprocess the image given by the user"""
    pass


def predict(file):
    """calls the model saved in .models and make prediction
    the image given by the user """
    pass
