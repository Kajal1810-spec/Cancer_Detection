import streamlit as st

st.title("📊 Model Details")

st.markdown("""
## 🧠 Model Architecture

- CNN (Convolutional Neural Network)
- Input: 48x48 Images
- Layers: Conv2D, MaxPooling, Dropout
- Optimizer: Adam
- Loss: Categorical Crossentropy

---

## 📁 Dataset

- IDC Breast Cancer Dataset
- Classes:
  - 0 → Benign
  - 1 → Malignant

---

## 📈 Performance

- Accuracy: ~85%
- Balanced classification

---

## ⚙️ Training Setup

- Epochs: 10
- Batch size: 32
""")