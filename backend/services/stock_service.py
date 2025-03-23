from sqlalchemy.orm import Session
from models import MedicineStock

def get_stock(db: Session):
    return db.query(MedicineStock).all()

def update_stock(db: Session, data: dict):
    stock = db.query(MedicineStock).filter(MedicineStock.name == data["name"]).first()
    if stock:
        stock.quantity = data["quantity"]
    else:
        stock = MedicineStock(**data)
        db.add(stock)
    db.commit()
    return {"message": "Stock updated successfully"}
