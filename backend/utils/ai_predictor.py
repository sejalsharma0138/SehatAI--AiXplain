import os
import time
from aixplain.factories import PipelineFactory
from sqlalchemy.orm import Session
from models import MedicineStock

os.environ["AIXPLAIN_API_KEY"] = "6ef68d4f39475dcccc680e7d0ee98e64aaecfcd50dd8131a3ed28892315d12b6"

def predict_shortage(db: Session):
    pipeline = PipelineFactory.get("67dfe525338999cb9696a5ca")

    stocks = db.query(MedicineStock).all()
    predictions = {}

    for stock in stocks:
        response = pipeline.run_async({"Query": f"Medicine {stock.name} stock is {stock.quantity}. Will it run out soon?"})
        
        while True:
            result = pipeline.poll(response["url"])
            if result.get("completed"):
                predictions[stock.name] = result.get("data", ["No prediction available"])
                break
            time.sleep(5)
    
    return predictions
