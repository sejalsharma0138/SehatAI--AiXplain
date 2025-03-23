
# # import streamlit as st
# # import requests

# # SYMPTOM_API_URL = "http://127.0.0.1:8000/analyze-symptoms/"

# # def symptom_checker(col1, language):
# #     text = {
# #         "describe_symptoms": {"English": "Describe your symptoms:", "Hindi": "अपने लक्षणों का वर्णन करें:"},
# #         "analyze_button": {"English": "Analyze Symptoms", "Hindi": "लक्षणों का विश्लेषण करें"},
# #         "warning_message": {"English": "Please enter symptoms to proceed.", "Hindi": "कृपया आगे बढ़ने के लिए लक्षण दर्ज करें।"},
# #     }

# #     if 'symptoms' not in st.session_state:
# #         st.session_state.symptoms = ""

# #     col1.subheader(text["describe_symptoms"][language])

# #     symptoms = col1.text_area(text["describe_symptoms"][language], value=st.session_state.symptoms)
# #     st.session_state.symptoms = symptoms

# #     if col1.button(text["analyze_button"][language]):
# #         if st.session_state.symptoms:
# #             col1.markdown("🔎 **Analyzing symptoms, please wait...**")
# #             try:
# #                 print("Sending symptoms to API:", st.session_state.symptoms)
# #                 response = requests.post(SYMPTOM_API_URL, json={"symptoms": st.session_state.symptoms})

# #                 print("API Response Status Code:", response.status_code)
# #                 print("API Response Text:", response.text)
                
# #                 if response.status_code == 200:
# #                     print("Inside success block")
# #                     response_text = response.text.strip().strip('"')
# #                     col1.success("✅ Analysis Complete!")
# #                     col1.markdown("### 🔎 Analysis Results:")
# #                     col1.markdown(response_text.replace("\n", "  \n"))
# #                     print("finished display block")
# #                     # Force UI refresh
# #                     st.experimental_rerun()

# #                 else:
# #                     col1.error(f"❌ {response.text if response.text else 'Unknown Error'}")

# #             except requests.exceptions.RequestException as e:
# #                 col1.error(f"❌ API Error: {str(e)}")

# #         else:
# #             col1.warning(text["warning_message"][language])

# import streamlit as st
# import requests

# SYMPTOM_API_URL = "http://127.0.0.1:8000/analyze-symptoms/"

# def symptom_checker(col1, language):
#     text = {
#         "describe_symptoms": {"English": "Describe your symptoms:", "Hindi": "अपने लक्षणों का वर्णन करें:"},
#         "analyze_button": {"English": "Analyze Symptoms", "Hindi": "लक्षणों का विश्लेषण करें"},
#         "warning_message": {"English": "Please enter symptoms to proceed.", "Hindi": "कृपया आगे बढ़ने के लिए लक्षण दर्ज करें।"},
#     }

#     if 'symptoms' not in st.session_state:
#         st.session_state.symptoms = ""

#     col1.subheader(text["describe_symptoms"][language])

#     symptoms = col1.text_area(text["describe_symptoms"][language], value=st.session_state.symptoms, key="symptoms_input")

#     if col1.button(text["analyze_button"][language]):
#         if symptoms.strip():
#             col1.markdown("🔎 **Analyzing symptoms, please wait...**")
#             try:
#                 response = requests.post(SYMPTOM_API_URL, json={"symptoms": symptoms.strip()})

#                 if response.status_code == 200:
#                     response_text = response.json()  # Ensure JSON response
#                     print(response_text)
#                     with st.container():
#                         st.json(response_text)
#                     # st.json(response_text)   # Ensure correct display

#                     # Debugging: Print the response to verify it
#                     st.write("Debug Response:", response_text)
#                 else:
#                     col1.error(f"❌ {response.text if response.text else 'Unknown Error'}")


#             except requests.exceptions.RequestException as e:
#                 col1.error(f"❌ API Error: {str(e)}")

#         else:
#             col1.warning(text["warning_message"][language])



import streamlit as st
import requests

SYMPTOM_API_URL = "http://127.0.0.1:8000/analyze-symptoms/"

def symptom_checker(col1, language):
    text = {
        "describe_symptoms": {"English": "Describe your symptoms:", "Hindi": "अपने लक्षणों का वर्णन करें:"},
        "analyze_button": {"English": "Analyze Symptoms", "Hindi": "लक्षणों का विश्लेषण करें"},
        "warning_message": {"English": "Please enter symptoms to proceed.", "Hindi": "कृपया आगे बढ़ने के लिए लक्षण दर्ज करें।"},
    }

    # Initialize session state for symptoms and response
    if 'symptoms' not in st.session_state:
        st.session_state.symptoms = ""
    if 'analysis_response' not in st.session_state:
        st.session_state.analysis_response = None

    col1.subheader(text["describe_symptoms"][language])
    symptoms = col1.text_area(text["describe_symptoms"][language], value=st.session_state.symptoms, key="symptoms_input")

    if col1.button(text["analyze_button"][language]):
        if symptoms.strip():
            col1.markdown("🔎 **Analyzing symptoms, please wait...**")
            try:
                response = requests.post(SYMPTOM_API_URL, json={"symptoms": symptoms.strip()})

                if response.status_code == 200:
                    st.session_state.analysis_response = response.text() # Store response in session state
                    print("Got response! ")
                else:
                    st.session_state.analysis_response = None
                    col1.error(f"❌ {response.text if response.text else 'Unknown Error'}")

            except requests.exceptions.RequestException as e:
                st.session_state.analysis_response = None
                col1.error(f"❌ API Error: {str(e)}")

        else:
            col1.warning(text["warning_message"][language])

    # Display response if available
    if st.session_state.analysis_response:
        print("show response")
        print(st.session_state.analysis_response)
        col1.markdown("### 🔎 Analysis Results:")
        col1.json(st.session_state.analysis_response)  # Display API response properly
