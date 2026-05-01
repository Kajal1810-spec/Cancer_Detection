# 🧬 Breast Cancer Detection System

## 📌 Project Overview

This project is an AI-powered web application that detects **Breast Cancer** from histopathology images using a **Deep Learning (CNN)** model.

The system allows users to upload an image and get real-time predictions.

---

## 🚀 Features

* 📷 Image upload for prediction
* 🤖 Deep Learning-based classification
* 📊 Confidence score visualization
* 🖥️ Multi-page Streamlit UI
* ⚡ Fast and user-friendly interface

---

## 🧠 Model Details

* Model Type: Convolutional Neural Network (CNN)

* Input Size: 128x128 images

* Output:

  * 0 → Benign
  * 1 → Malignant

* Optimizer: Adam

* Loss Function: Binary Crossentropy

* Accuracy: ~85%

---

## 📁 Project Structure

```
Cancer_Project/
│
├── app.py
├── pages/
│   ├── 1_Predict.py
│   ├── 2_Model_Info.py
│   └── 3_About.py
│
├── train_model.py
├── cancer_model.h5
├── dataset/
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Project

```
git clone <your-repo-link>
cd Cancer_Project
```

### 2️⃣ Create Virtual Environment

```
py -3.10 -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run Application

```
streamlit run app.py
```

Open browser:

```
http://localhost:8501
```

---

## 🧪 How to Use

1. Open the app
2. Go to **Predict Page**
3. Upload histopathology image
4. Get prediction (Benign / Malignant)

---

## 🎯 Objective

To assist in **early detection of breast cancer** using AI and Deep Learning.

---

## 🔧 Technologies Used

* Python
* TensorFlow / Keras
* Streamlit
* NumPy
* PIL

---

## 👩‍💻 Developed By

**Kajal Thakkar**

---

## 💡 Future Improvements

* Improve accuracy using transfer learning
* Deploy on cloud
* Add real-time scanning
* Integrate with hospital systems

---

## 📌 Conclusion

This project demonstrates how AI can help in **medical diagnosis**, making cancer detection faster and more efficient.

---
