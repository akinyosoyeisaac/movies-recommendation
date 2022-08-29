import pandas as pd
import numpy as np
from fastapi import FastAPI, Form
from src.models.predict_model import recommender
import uvicorn


app = FastAPI()

@app.get('/')
async def Home():
    return {'text': 'Welcome! Here you we help recommend a movie to you base on your previous watch'}

@app.post('/predict')   
async def Recommendations(title: str = Form()):
    predictions = recommender(title, 0)
    return predictions

if __name__ == "__main__":
    uvicorn.run("app.fast_app:app", host="127.0.0.1", port=8080, reload=True)