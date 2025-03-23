from sqlalchemy import Column, Integer, String, Float
from database import Base

class MedicineStock(Base):
    __tablename__ = "medicine_stock"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    quantity = Column(Integer)
    threshold = Column(Integer)
    supplier_email = Column(String)
