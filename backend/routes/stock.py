from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import MedicineStock
from services.stock_service import get_stock, update_stock
from utils.ai_predictor import predict_shortage

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def fetch_stock(db: Session = Depends(get_db)):
    return get_stock(db)

@router.post("/update/")
def update_medicine(data: dict, db: Session = Depends(get_db)):
    return update_stock(db, data)

@router.get("/predict/")
def predict_stock(db: Session = Depends(get_db)):
    return predict_shortage(db)
