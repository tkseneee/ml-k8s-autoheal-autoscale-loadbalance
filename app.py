from fastapi import FastAPI
import pickle
import numpy as np
from pydantic import BaseModel

# Load pre-trained model
with open("iris_model.pkl", "rb") as f:
    model = pickle.load(f)

# Define API using FastAPI
app = FastAPI()

class InputData(BaseModel):
    features: list

@app.post("/predict")
def predict(data: InputData):
    features = np.array(data.features).reshape(1, -1)
    prediction = model.predict(features)
    return {"prediction": int(prediction[0])}

# Run using: uvicorn app:app --host 0.0.0.0 --port 8000
