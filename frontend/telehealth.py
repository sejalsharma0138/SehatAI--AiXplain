import streamlit as st
from PIL import Image
import speech_recognition as sr

def telehealth(col1, language):
    text = {
        "describe_symptoms": {"English": "Describe your symptoms:", "Hindi": "अपने लक्षणों का वर्णन करें:"},
        "analyze_button": {"English": "Analyze Symptoms", "Hindi": "लक्षणों का विश्लेषण करें"},
        "success_message": {"English": "✅ Analyzing symptoms...", "Hindi": "✅ लक्षणों का विश्लेषण किया जा रहा है..."},
        "warning_message": {"English": "Please enter symptoms to proceed.", "Hindi": "कृपया आगे बढ़ने के लिए लक्षण दर्ज करें।"},
        "upload_image": {"English": "Upload Image", "Hindi": "छवि अपलोड करें"},
        "record_voice": {"English": "🎙️ Record Voice", "Hindi": "🎙️ आवाज़ रिकॉर्ड करें"}
    }
    col1.subheader(text["telehealth"][language])
    if col1.button(text["start_call"][language]):
        col1.info(text["opening_call"][language])
    