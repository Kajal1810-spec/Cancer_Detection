import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# ------------------- PAGE CONFIG -------------------
st.set_page_config(page_title="Cancer Prediction", page_icon="🧬", layout="wide")

# ------------------- CUSTOM CSS -------------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.stFileUploader {
    border: 2px dashed #00FFAA;
    padding: 10px;
    border-radius: 12px;
}
.result-box {
    padding: 20px;
    border-radius: 15px;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# ------------------- LOAD MODEL -------------------
@st.cache_resource
def load_my_model():
    return load_model("cancer_model.h5")

model = load_my_model()

# ------------------- TITLE -------------------
st.markdown("## 🧬 Cancer Prediction")
st.caption("Upload histopathology image to detect cancer")

# ------------------- FILE UPLOAD -------------------
uploaded_file = st.file_uploader("📤 Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    
    # Load image
    image = Image.open(uploaded_file).convert("RGB")
    
    # Display image
    st.image(image, use_container_width=True)

    # ------------------- PREPROCESS -------------------
    img = image.resize((128, 128))   # IMPORTANT FIX
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    # ------------------- PREDICTION -------------------
    prediction = model.predict(img)[0][0]
    
    # ------------------- RESULT UI -------------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🧪 Input Image")
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("🧠 Prediction Result")

        if prediction > 0.5:
            st.markdown(f"""
            <div class="result-box" style="background-color:#3a1f1f;">
                <h3 style="color:#ff4b4b;">⚠️ Malignant (Cancer Detected)</h3>
                <p style="color:white;">Confidence: {prediction*100:.2f}%</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="result-box" style="background-color:#1f3a2f;">
                <h3 style="color:#00ff88;">✅ Benign (Safe)</h3>
                <p style="color:white;">Confidence: {(1-prediction)*100:.2f}%</p>
            </div>
            """, unsafe_allow_html=True)

        # ------------------- PROGRESS BAR -------------------
        st.subheader("📊 Confidence Meter")
        st.progress(int(prediction * 100))

    # ------------------- EXTRA INFO -------------------
    st.info("🧠 AI is analyzing tissue patterns to detect abnormal cancer cells.")

else:
    st.warning("⚠️ Please upload an image to start prediction.")
