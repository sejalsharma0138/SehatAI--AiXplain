import streamlit as st
from PIL import Image
import os, time
import speech_recognition as sr
from streamlit_autorefresh import st_autorefresh

# Page Configuration
st.set_page_config(page_title="Sehat AI", layout="wide")

# Split into two columns
col1, col2 = st.columns([4, 1])

# Theme & Language in Right Column
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
    "title": {"English": "🌿 Sehat AI - Healthcare for Rural India", "Hindi": "🌿 सेहत एआई - ग्रामीण भारत के लिए स्वास्थ्य देखभाल"},
    "description": {"English": "Empowering rural communities with AI-powered medical assistance", "Hindi": "एआई-संचालित चिकित्सा सहायता के साथ ग्रामीण समुदायों को सशक्त बनाना"},
    "symptom_checker": {"English": "🤒 Symptom Checker", "Hindi": "🤒 लक्षण जांचकर्ता"},
    "describe_symptoms": {"English": "Describe your symptoms:", "Hindi": "अपने लक्षणों का वर्णन करें:"},
    "analyze_button": {"English": "Analyze Symptoms", "Hindi": "लक्षणों का विश्लेषण करें"},
    "success_message": {"English": "✅ Analyzing symptoms...", "Hindi": "✅ लक्षणों का विश्लेषण किया जा रहा है..."},
    "warning_message": {"English": "Please enter symptoms to proceed.", "Hindi": "कृपया आगे बढ़ने के लिए लक्षण दर्ज करें।"},
    "upload_image": {"English": "Upload Image", "Hindi": "छवि अपलोड करें"},
    "record_voice": {"English": "🎙️ Record Voice", "Hindi": "🎙️ आवाज़ रिकॉर्ड करें"},
    "medicine_stock": {"English": "💊 Medicine Stock Tracker", "Hindi": "💊 दवा स्टॉक ट्रैकर"},
    "check_stock": {"English": "Check Stock", "Hindi": "स्टॉक की जांच करें"},
    "stock_fetched": {"English": "✅ Stock details fetched!", "Hindi": "✅ स्टॉक विवरण लाया गया!"},
    "telehealth": {"English": "🩺 Telehealth", "Hindi": "🩺 टेलीहेल्थ"},
    "start_call": {"English": "Start Video Call", "Hindi": "वीडियो कॉल शुरू करें"},
    "opening_call": {"English": "🔗 Opening video consultation...", "Hindi": "🔗 वीडियो परामर्श खोल रहा है..."},
    "reports": {"English": "📄 Health Reports", "Hindi": "📄 स्वास्थ्य रिपोर्ट"},
    "generate_report": {"English": "Generate Report", "Hindi": "रिपोर्ट तैयार करें"},
    "report_generated": {"English": "✅ Report generated!", "Hindi": "✅ रिपोर्ट तैयार हो गई!"},
    "education": {"English": "📚 Health Education", "Hindi": "📚 स्वास्थ्य शिक्षा"},
    "load_resources": {"English": "Load Resources", "Hindi": "संसाधन लोड करें"},
    "resources_loaded": {"English": "✅ Educational resources loaded!", "Hindi": "✅ शैक्षिक संसाधन लोड हो गए!"}
}

# Title and Description
col1.title(text["title"][language])
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

# Symptom Checker
if menu == text["symptom_checker"][language]:
    col1.subheader(text["symptom_checker"][language])
    
    # Text Input
    symptoms = col1.text_area(text["describe_symptoms"][language])

    # Image Upload
    uploaded_image = col1.file_uploader(text["upload_image"][language], type=["jpg", "png", "jpeg"])
    if uploaded_image:
        img = Image.open(uploaded_image)
        col1.image(img, caption="Uploaded Image", use_container_width =True)

    # Voice Input
    if col1.button(text["record_voice"][language]):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            col1.info("🎙️ Listening...")
            audio = r.listen(source)
            try:
                text_input = r.recognize_google(audio)
                col1.success(f"✅ {text_input}")
            except Exception as e:
                col1.error(f"❌ Error: {str(e)}")

    # Analyze Symptoms Button
    if col1.button(text["analyze_button"][language]):
        if symptoms or uploaded_image:
            col1.success(text["success_message"][language])
        else:
            col1.warning(text["warning_message"][language])

# Medicine Stock Tracker
elif menu == text["medicine_stock"][language]:
    col1.subheader(text["medicine_stock"][language])
    if col1.button(text["check_stock"][language]):
        col1.success(text["stock_fetched"][language])

# Telehealth Connector
elif menu == text["telehealth"][language]:
    col1.subheader(text["telehealth"][language])
    if col1.button(text["start_call"][language]):
        col1.info(text["opening_call"][language])

# Reports
elif menu == text["reports"][language]:
    col1.subheader(text["reports"][language])
    if col1.button(text["generate_report"][language]):
        col1.success(text["report_generated"][language])

# Education
elif menu == text["education"][language]:
    col1.subheader(text["education"][language])
    if col1.button(text["load_resources"][language]):
        col1.success(text["resources_loaded"][language])

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

    # ✅ Footer ko fixed rakhne ke liye CSS inject karo
    st.markdown("""
        <style>
            .footer {
                position: fixed;
                bottom: 0;
                left: 0;
                width: 100%;
                background-color: #f9f9f9;
                padding: 12px;
                text-align: center;
                font-size: 14px;
                color: #333;
                border-top: 1px solid #ccc;
                z-index: 999;
            }
            .divider-footer {
                margin-bottom: 0;
                border-top: 1px solid #ccc;
            }
            /* Divider ko footer ke saath merge karne ke liye */
            .stDivider {
                margin-bottom: 0 !important;
                padding-bottom: 0 !important;
                border-top: 1px solid #ccc !important;
            }
        </style>
        <div class="divider-footer"></div>
        <div class="footer">
            👩‍⚕️ <b>Sehat AI</b> | Powered by AI for rural healthcare
        </div>
    """, unsafe_allow_html=True)
