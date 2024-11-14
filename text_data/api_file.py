from fastapi import FastAPI
from text_data.model import predict
import os

app = FastAPI()

app.get('/')
def root():
    return {'hello': 'team'}

app.get('/symptoms')
def predict(symptoms):
    prediction , probability = predict(symptoms)
    return {{'disease': prediction}, {'prob': probability}}
