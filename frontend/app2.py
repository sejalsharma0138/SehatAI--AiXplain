import streamlit as st
from PIL import Image
import os
from streamlit_autorefresh import st_autorefresh
from symptom_checker import symptom_checker
from medicine_stock import medicine_stock
from reports import reports
from telehealth import telehealth
from education import education
import base64
from io import BytesIO



# Page Configuration
st.set_page_config(page_title="Sehat AI", layout="wide")

# Split into two columns
col1, col2 = st.columns([4, 1])

# Theme & Language in Right Column
with col2:
    theme = "Dark" if st.toggle("🌗 Theme", value=False, key="theme_toggle") else "Light"
    language = "Hindi" if st.toggle("🌍 Language", value=False, key="language_toggle") else "English"

# Apply Theme (Light/Dark Mode)
if theme == "Dark":
    st.markdown(
        """
        <style>
            body, .stApp {
                background-color: #121212;
                color: #ffffff;
            }
            .stButton>button {
                background-color: #333333;
                color: #ffffff;
                border-radius: 8px;
            }
            .stButton>button:hover {
                background-color: #444444;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <style>
            body, .stApp {
                background: linear-gradient(to bottom right, #e6ffe6, #ffffff);
                color: #000000;
            }
            .stButton>button {
                background-color: #4CAF50;
                color: #ffffff;
                border-radius: 8px;
            }
            .stButton>button:hover {
                background-color: #45a049;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Language Mapping
text = {
    "title": {"English": "Sehat AI - Healthcare for Rural India", "Hindi": "🌿 सेहत एआई - ग्रामीण भारत के लिए स्वास्थ्य देखभाल"},
    "description": {"English": "Empowering rural communities with AI-powered medical assistance", "Hindi": "एआई-संचालित चिकित्सा सहायता के साथ ग्रामीण समुदायों को सशक्त बनाना"},
    "symptom_checker": {"English": "🤒 Symptom Checker", "Hindi": "🤒 लक्षण जांचकर्ता"},
    "medicine_stock": {"English": "💊 Medicine Stock Tracker", "Hindi": "💊 दवा स्टॉक ट्रैकर"},
    "telehealth": {"English": "🩺 Telehealth", "Hindi": "🩺 टेलीहेल्थ"},
    "reports": {"English": "📄 Health Reports", "Hindi": "📄 स्वास्थ्य रिपोर्ट"},
    "education": {"English": "📚 Health Education", "Hindi": "📚 स्वास्थ्य शिक्षा"}
}


# Load logo
logo = Image.open("homepics/1.png")

# Convert logo to base64
buffered = BytesIO()
logo.save(buffered, format="PNG")
img_str = base64.b64encode(buffered.getvalue()).decode()

# Display logo and title in the same line
col1.markdown(
    f"""
    <div style="display: flex; align-items: center;">
        <img src="data:image/png;base64,{img_str}" width="100" style="margin-right: 10px;">
        <h1 style="margin: 0; font-size: 50px;">{text["title"][language]}</h1>
    </div>
    """,
    unsafe_allow_html=True
)
col1.markdown(f"### {text['description'][language]}")

# Sidebar Navigation
menu = col1.radio(
    "🚀 Navigation",
    [
        text["symptom_checker"][language],
        text["medicine_stock"][language],
        text["telehealth"][language],
        text["reports"][language],
        text["education"][language]
    ],
)

# Symptom Checker Module
if menu == text["symptom_checker"][language]:
    symptom_checker(col1, language)


# Medicine Stock Tracker
elif menu == text["medicine_stock"][language]:
    medicine_stock(col1, language)

# Telehealth Connector
elif menu == text["telehealth"][language]:
    telehealth(col1, language)

# Reports
elif menu == text["reports"][language]:
    reports(col1,language)
   

# Education
elif menu == text["education"][language]:
    education(col1,language)
        


# ✅ Image Carousel in Right Column
with col2:
    image_folder = 'homepics'
    if os.path.exists(image_folder):
        image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpeg', '.jpg', '.png'))]
        if image_files:
            # Auto-refresh every 2 seconds
            st_autorefresh(interval=2000, key="carousel_refresh")

            if 'carousel_index' not in st.session_state:
                st.session_state.carousel_index = 0
            
            img_path = os.path.join(image_folder, image_files[st.session_state.carousel_index])
            img = Image.open(img_path)
            st.image(img, caption=f"{st.session_state.carousel_index + 1}/{len(image_files)}", use_container_width=True)

            # Update index for next image
            st.session_state.carousel_index = (st.session_state.carousel_index + 1) % len(image_files)
        else:
            st.warning("⚠️ No images found in the 'homepics' folder.")
    else:
        st.error("❌ Folder 'homepics' does not exist. Create the folder and add images.")
        
     # ✅ AI News Section
    st.markdown("### 🌐 Latest AI News in Rural Healthcare")
    with st.container():
        news = [
            {
                "title": "AI Boosts Healthcare Access in Rural India",
                "link": "https://example.com/ai-healthcare-rural",
                "summary": "AI-based platforms are helping doctors provide better healthcare in remote areas."
            },
            {
                "title": "Telehealth Powered by AI Reaches Rural Villages",
                "link": "https://example.com/telehealth-ai",
                "summary": "AI-driven telehealth services are expanding access to medical care in underserved communities."
            },
            {
                "title": "AI Diagnosis Tools Help Reduce Rural Health Disparities",
                "link": "https://example.com/ai-diagnosis",
                "summary": "Machine learning models are improving diagnostic accuracy in rural hospitals."
            }
        ]

        for i, article in enumerate(news):
            st.markdown(f"**[{article['title']}]({article['link']})**")
            st.caption(article["summary"])
            if i != len(news) - 1:  # Last news ke baad divider na ho
                st.divider()

# ✅ Footer
st.markdown("""
    <div style="position: fixed; bottom: 0; left: 0; width: 100%; background-color: #f9f9f9; padding: 10px; text-align: center; border-top: 1px solid #ccc;">
        👩‍⚕️ <b>Sehat AI</b> | Powered by AI for rural healthcare
    </div>
""", unsafe_allow_html=True)
