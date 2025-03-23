import streamlit as st
from PIL import Image

def education(col1, language):
    # Language-based text options
    text = {
        "Interactive Quizzes": {"English": "Interactive Quizzes", "Hindi": "इंटरएक्टिव प्रश्नोत्तरी"},
        "Informative Videos": {"English": "Informative Videos", "Hindi": "सूचनात्मक वीडियो"},
        "Infographics & Illustrations": {"English": "Infographics & Illustrations", "Hindi": "इन्फोग्राफिक्स और चित्रण"},
        "Voice Notes": {"English": "Voice Notes", "Hindi": "ध्वनि नोट्स"},
        "Chatbot for Q&A": {"English": "Chatbot for Q&A", "Hindi": "प्रश्नोत्तरी के लिए चैटबॉट"},
        "Localized Content": {"English": "Localized Content", "Hindi": "स्थानीयकृत सामग्री"},
        "Health Challenges": {"English": "Health Challenges", "Hindi": "स्वास्थ्य चुनौतियाँ"},
        "Community Forum": {"English": "Community Forum", "Hindi": "सामुदायिक मंच"},
        "Emergency Guidance": {"English": "Emergency Guidance", "Hindi": "आपातकालीन मार्गदर्शन"},
        "Education Module": {"English": "Education Module", "Hindi": "शिक्षा मॉड्यूल"}
    }

    # Define the options
    options = [
        {"key": "Interactive Quizzes", "link": "#quizzes", "image": "h.png"},
        {"key": "Informative Videos", "link": "#videos", "image": "h.png"},
        {"key": "Infographics & Illustrations", "link": "#infographics", "image": "h.png"},
        {"key": "Voice Notes", "link": "#voice-notes", "image": "h.png"},
        {"key": "Chatbot for Q&A", "link": "#chatbot", "image": "h.png"},
        {"key": "Localized Content", "link": "#localized", "image": "h.png"},
        {"key": "Health Challenges", "link": "#challenges", "image": "h.png"},
        {"key": "Community Forum", "link": "#forum", "image": "h.png"},
        {"key": "Emergency Guidance", "link": "#emergency", "image": "h.png"}
    ]

    # Subheader based on language
    col1.subheader(text["Education Module"][language])

    # Create a 3x3 grid inside col1
    cols = col1.columns(3)

    # Loop through the options and display them in the grid
    for i, option in enumerate(options):
        with cols[i % 3]:
            st.markdown(
                f"""
                <div style="
                    border: 1px solid #ddd;
                    border-radius: 12px;
                    padding: 15px;
                    margin-bottom: 12px;
                    text-align: center;
                    background-color: #ffffff;
                    box-shadow: 2px 2px 12px rgba(0,0,0,0.1);
                    transition: transform 0.2s ease;
                " 
                onmouseover="this.style.transform='scale(1.05)'" 
                onmouseout="this.style.transform='scale(1)'">
                    <img src='frontend/homepics/{option["image"]}' alt='{text[option["key"]][language]}' width='60' style="margin-bottom: 10px;">
                    <div>
                        <a href="{option['link']}" style="
                            text-decoration: none;
                            color: #4F8BF9;
                            font-size: 16px;
                            font-weight: 500;
                        ">
                            {text[option["key"]][language]}
                        </a>
                    </div>
                </div>
                """, 
                unsafe_allow_html=True
            )
