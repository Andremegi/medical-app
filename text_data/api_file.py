from fastapi import FastAPI
from text_data.model import predict_disease
import os

app = FastAPI()

@app.get('/')
def root():
    return {'hello': 'team'}

@app.get('/symptoms')
def predict(symptoms):
    prediction , probability = predict_disease(symptoms)
    print('disease', prediction)
    return {'disease': prediction, 'probability': str(probability)}
