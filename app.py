import streamlit as st

st.set_page_config(page_title="Cancer AI", page_icon="🧬", layout="wide")

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
h1, h2, h3 {
    color: #00FFAA;
}
</style>
""", unsafe_allow_html=True)

st.title("🧬 AI-Based Cancer Detection System")

st.markdown("""
### 👩‍⚕️ Smart Diagnosis using Deep Learning

Welcome to the **AI-powered Breast Cancer Detection System**.

✔ Upload histopathology images  
✔ Get instant predictions  
✔ Powered by CNN (Deep Learning)

---

👉 Use the sidebar to navigate:
- 🔍 Predict
- 📊 Model Info
- ℹ️ About
""")

col1, col2, col3 = st.columns(3)

col1.metric("Accuracy", "85%")
col2.metric("Model", "CNN")
col3.metric("Dataset", "IDC")

st.success("✅ System Ready for Prediction")