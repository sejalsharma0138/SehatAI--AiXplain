# 🌿 Sehat AI – Empowering Rural Healthcare with AI  
Sehat AI is an AI-powered healthcare solution designed to provide accessible and affordable medical assistance to rural communities in India. Leveraging aiXplain's advanced AI models, Sehat AI aims to bridge the healthcare gap by offering real-time symptom analysis, medicine stock tracking, telehealth consultations, and health education — all through a simple, user-friendly platform.

---

## 🚀 Project Overview  
In rural India, access to quality healthcare remains a significant challenge due to inadequate medical infrastructure and limited access to healthcare professionals. Sehat AI addresses this gap by combining AI-driven diagnosis, predictive medicine tracking, and secure telehealth services, ensuring that even the most remote areas receive timely medical care.

---

## 🏆 Key Features  
### 1. 🤒 Symptom Checker AI  
✅ Built using aiXplain’s pre-trained NLP models.  
✅ Understands local dialects through speech-to-text conversion.  
✅ Provides a list of possible illnesses and suggests next steps for treatment.  

---

### 2. 💊 Medicine Stock Tracker  
✅ AI agent tracks medicine availability in rural clinics.  
✅ Predicts shortages using aiXplain’s data analysis tools.  
✅ Sends real-time alerts to health workers and suppliers.  

---

### 3. 🩺 Telehealth Connector  
✅ Enables video consultations with doctors using aiXplain’s agent connectors.  
✅ Ensures secure, real-time communication.  
✅ Maintains patient confidentiality using aiXplain’s built-in security.  

---

### 4. 🤖 Agent Collaboration and Fine-Tuning  
✅ aiXplain’s multi-agent orchestration enables smooth collaboration between AI agents.  
✅ Fine-tunes models based on real-world feedback.  
✅ Supports deployment on cloud, on-premises, and edge devices.  

---

### 5. 📄 AI-Powered Health Report Generation *(TBA)*  
✅ Automatically generates and updates patient health records.  
✅ Securely stores and organizes patient data for future reference.  

---

### 6. 📚 Health Education Module *(TBA)*  
✅ Provides educational resources on hygiene, nutrition, and disease prevention.  
✅ Delivers content in regional languages.  

---

### 7. 🚨 Emergency Response Integration *(TBA)*  
✅ Links with local emergency services.  
✅ Sends automatic alerts for critical medical emergencies.  

---

## 💡 Tech Stack  
| Component           | Technology               |
|--------------------|--------------------------|
| **Frontend**        | Streamlit (Python)        |
| **Backend**         | FastAPI                   |
| **AI Models**       | aiXplain                  |
| **Database**        | SQLite/PostgreSQL         |
| **Deployment**      | to be added |

---

## 🔎 How It Works  
1. Patient inputs symptoms (voice or text).  
2. AI model analyzes symptoms → Returns possible diagnosis.  
3. Medicine stock tracker predicts shortages and sends alerts.  
4. Telehealth connector enables video consultations.  
5. Health reports and education modules provide additional support.  

---

## 🚀 Setup Instructions  

### 1. **Clone Repository**  
```bash
git clone https://github.com/username/sehat-ai.git  
cd sehat-ai  
```

---

### 2. **Set Up aiXplain Account and API Keys**  
- Sign up for an aiXplain account at [https://aixplain.com](https://aixplain.com).  
- Generate an API key from the aiXplain developer console.  
- Create a `.env` file in the root directory and add:  

```env
AIXPLAIN_API_KEY="your-api-key"
```

---

### 3. **Install Dependencies**  
Install required Python libraries:  
```bash
pip install -r requirements.txt
```

---

### 4. **Configure Backend (FastAPI)**  
Create a `backend.py` file in the root directory:  

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Sehat AI Backend Running"}
```

Run the backend:  
```bash
uvicorn backend:app --reload
```

---

### 5. **Set Up aiXplain Models**  
Use aiXplain’s API to set up models for:  
- Symptom analysis  
- Speech-to-text conversion  
- Medicine stock prediction  
- Telehealth connection  

Sample connection:  
```python
import requests

API_URL = "https://api.aixplain.com/v1/analyze"
HEADERS = {"Authorization": f"Bearer {AIXPLAIN_API_KEY}"}

data = {
    "input_text": "I have a headache and fever."
}

response = requests.post(API_URL, json=data, headers=HEADERS)
print(response.json())
```

---

### 6. **Build Frontend (Streamlit)**  
Create an `app.py` file for the frontend:  
```python
import streamlit as st

st.title("Sehat AI – Healthcare for Rural India")

symptom = st.text_input("Enter your symptoms:")
if st.button("Analyze"):
    st.write(f"Analyzing symptoms: {symptom}")
```

Run the frontend:  
```bash
streamlit run app.py
```

---

### 7. **Connect Backend with Frontend**  
Modify `app.py` to connect with FastAPI backend:  
```python
import streamlit as st
import requests

symptom = st.text_input("Enter your symptoms:")
if st.button("Analyze"):
    response = requests.get("http://127.0.0.1:8000")
    st.write(response.json())
```

---

### 8. **Deploy to Production**  

**Frontend:**  
Deploy the Streamlit app on **Vercel** or **Render**:  
```bash
vercel deploy
```

**Backend:**  
Deploy FastAPI backend using **Render**:  
```bash
render.yaml
```

---

### 9. **Monitor and Scale**  
✅ Set up aiXplain’s fine-tuning options to improve performance.  
✅ Monitor logs and usage metrics to optimize performance.  
✅ Adjust model parameters as needed based on user feedback.  

---


🌍 Future Scope

✅ Integration with government healthcare systems.

✅ Multilingual support for diverse Indian dialects.

✅ Expansion to wearable device integration and mobile app services.

🏅 Why Sehat AI Matters
Sehat AI is more than just an AI tool — it’s a lifeline for underserved communities. By combining AI with real-time healthcare delivery, Sehat AI empowers rural healthcare infrastructure and improves health outcomes where it matters the most.

👩‍💻 Contributors
Sejal Sharma – GitHub
Ankit 

👉 Feel free to fork, contribute, or reach out for collaboration! 😎


