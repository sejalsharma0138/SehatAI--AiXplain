from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from symptom_checker import analyze_symptoms

Key="7e253244bde191005f31bf8da48f80b310417abf62f6f2011ac978cc21b730ec"
import os
os.environ["AIXPLAIN_API_KEY"] = Key
app = FastAPI()

# Allow frontend and backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze-symptoms/")
async def analyze_symptoms_api(data: dict):
    symptoms = data.get("symptoms")
    if not symptoms:
        raise HTTPException(status_code=400, detail="Symptoms are required")

    try:
        result = analyze_symptoms(symptoms)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {"message": "Sehat AI Backend is running"}
