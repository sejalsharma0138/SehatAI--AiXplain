import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/stock/"

def medicine_stock_tracker():
    st.subheader("📦 Medicine Stock Overview")

    # Fetch stock data
    response = requests.get(API_URL)
    if response.status_code == 200:
        stocks = response.json()
        for stock in stocks:
            st.write(f"**{stock['name']}**: {stock['quantity']} left")
    else:
        st.error("❌ Failed to fetch stock data")

    # Update Stock
    st.subheader("✏️ Update Stock")
    name = st.text_input("Medicine Name")
    quantity = st.number_input("Quantity", min_value=0)
    
    if st.button("Update Stock"):
        res = requests.post(API_URL + "update/", json={"name": name, "quantity": quantity})
        if res.status_code == 200:
            st.success("✅ Stock Updated Successfully")
        else:
            st.error("❌ Failed to update stock")

    # AI Prediction
    if st.button("🔮 Predict Shortages"):
        res = requests.get(API_URL + "predict/")
        if res.status_code == 200:
            st.json(res.json())
        else:
            st.error("❌ AI Prediction Failed")
