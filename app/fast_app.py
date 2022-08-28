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
    return recommender["Name"].to_dict()

