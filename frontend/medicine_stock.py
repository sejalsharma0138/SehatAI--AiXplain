import time
import streamlit as st

def medicine_stock(col1, language):
    text = {
        "medicine_stock": {"English": "Medicine Stock", "Hindi": "दवा स्टॉक"},
        "check_stock": {"English": "Check Stock", "Hindi": "स्टॉक की जांच करें"},
        "stock_fetched": {"English": "Stock data fetched successfully!", "Hindi": "स्टॉक डेटा सफलतापूर्वक प्राप्त हुआ!"},
        "loading_message": {"English": "Fetching stock details...", "Hindi": "स्टॉक विवरण लाया जा रहा है..."},
        "error_message": {"English": "Failed to fetch stock data.", "Hindi": "स्टॉक डेटा लाने में विफल।"}
    }
    
    # Fallback values to prevent KeyError
    col1.subheader(text.get("medicine_stock", {}).get(language, "Medicine Stock"))
    
    if col1.button(text.get("check_stock", {}).get(language, "Check Stock")):
        with st.spinner(text.get("loading_message", {}).get(language, "Loading...")):
            time.sleep(2)  # Simulate data fetching
            
            # Simulate success or failure (replace with real data logic)
            success = True
            if success:
                col1.success(text.get("stock_fetched", {}).get(language, "Stock fetched successfully!"))
            else:
                col1.error(text.get("error_message", {}).get(language, "Error fetching stock data."))

