from fastapi import FastAPI, UploadFile
from recognition_Model.predict import prediction_model
from PIL import Image  
import numpy as np

app = FastAPI()

@app.post("/image")
async def prase_an_image(file: UploadFile):
    img = file.resize((300, 300))
    return prediction_model(np.array(img))