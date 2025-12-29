This project implements a Pharmacy Prescription Handling & Storage Explainer Bot using Google Gemini Flash and Streamlit.

Problem Identification
Pharmacy staff and customers often misunderstand prescription handling rules, medicine storage conditions, and expiry guidelines. Explaining these repeatedly increases pharmacist workload.

Solution Design
A Generative AI chatbot was designed to provide clear, non-clinical explanations of pharmacy operations while strictly avoiding medical advice or medication recommendations.

Model Integration
The application uses Google Gemini 3 Flash Preview via the google-genai Python SDK to generate fast, factual responses.
A strict prompt strategy ensures regulatory-safe behavior.

Streamlit Interface
Streamlit provides a lightweight web interface where users can:

Enter pharmacy-related questions

Receive instant explanations

View safety disclaimers

Safety & Compliance

No diagnosis or treatment advice is allowed

No medication recommendations are generated

The bot focuses only on procedures, storage, expiry, and responsibilities

Deployment Readiness
The app runs locally or on cloud platforms with a Gemini API key stored as an environment variable, making it suitable for hackathons and demos.

Outcome
The solution improves awareness, consistency, and safety in pharmacy operations while demonstrating responsible GenAI usage in healthcare.
