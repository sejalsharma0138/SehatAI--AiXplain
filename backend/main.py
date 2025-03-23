from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from symptom_checker import analyze_symptoms
from routes.stock import router as stock_router

VIDEO_PIPELINE_ID = "67dfee4f181c58b7238eb9af"

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

app.include_router(stock_router, prefix="/stock", tags=["Stock Tracker"])

@app.post("/generate-video-call/")
def generate_video_call():
    url = f"https://api.aixplain.com/v1/pipelines/{VIDEO_PIPELINE_ID}/run"
    headers = {"Authorization": f"Bearer {AIXPLAIN_API_KEY}"}
    payload = {"input": {"request_type": "video_call"}}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=500, detail="Failed to generate video call")


@app.get("/")
def root():
    return {"message": "Sehat AI Backend is running"}
