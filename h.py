from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Allow requests from your React Native app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================
# Load the trained ML model
# ============================
try:
    model = joblib.load("model.pkl")
    print("✅ Model loaded successfully")
except Exception as e:
    model = None
    print("❌ Error loading model:", e)

# ============================
# Define input data structure
# ============================
class InputData(BaseModel):
    feature1: float
    feature2: float
    feature3: float

# ============================
# Root endpoint
# ============================
@app.get("/")
def root():
    return {"message": "ML Backend with trained model connected to React Native!"}

# ============================
# Prediction endpoint
# ============================
@app.post("/predict")
def predict(data: InputData):
    if model is None:
        return {"error": "Model not loaded"}

    # Convert input to numpy array
    X = np.array([[data.feature1, data.feature2, data.feature3]])
    prediction = model.predict(X)
    return {"prediction": int(prediction[0])}
