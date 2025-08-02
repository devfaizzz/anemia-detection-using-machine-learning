<div align="center">

# 🚑 Anemia Detection Using Machine Learning 🚑

*An intelligent system for predicting anemia using Random Forest Classification*

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](https://opensource.org/licenses/MIT)

<img src="https://user-images.githubusercontent.com/74038190/212257454-16e3712e-945a-4ca2-b238-408ad0bf87e6.gif" width="100">

</div>

---

<div align="center">

## <img src="https://user-images.githubusercontent.com/74038190/216122041-518ac897-8d92-4c6b-9b3f-ca01dcaf38ee.png" width="30" /> Overview
</div>

This project implements a **Random Forest Classifier** to predict whether an individual is anemic or non-anemic based on their blood-related attributes. The project includes:
- A **Flask-based web application** to interact with the model
- Pre-trained model for predictions
- A detailed implementation of training, class balancing, and feature importance analysis
- **NEW FEATURE**: Upload a **blood report image** to predict anemia using **Google Gemini 2.0 Flash** for text extraction

<div align="center">

## <img src="https://user-images.githubusercontent.com/74038190/216121964-513bdf95-3c8c-429a-82bc-7c770caca8fc.png" width="30" /> Features

</div>

1. **Random Forest Classifier** for high accuracy predictions
2. **SMOTE (Synthetic Minority Oversampling Technique)** for handling class imbalance
3. **Feature Importance Analysis** to identify the most significant contributors to predictions
4. Simple **frontend interface** for user input
5. **NEW**: **Image-Based Prediction** – Upload a **blood test report** image to automatically extract relevant values and get predictions

<div align="center">

## 📊 Performance Evaluation

*Model Comparison Analysis*

| Algorithm            | Accuracy | AUC |
|:-------------------:|:--------:|:---:|
| Random Forest       | 99%      | 99% |
| Logistic Regression | 98%      | 98% |
| SVM                 | 90%      | 90% |
| KNN                 | 87%      | 87% |

</div>

*Random Forest Classifier demonstrates superior performance across both metrics.*

<div align="center">

## 🏰 System Architecture

![System Architecture](images/diagram-export-5-21-2024-4_49_14-PM.png)

*The system follows a structured pipeline from dataset handling to model predictions.*

## 📊 Dataset Attributes

</div>

- 💉 **Hemoglobin Levels**
- 🔬 **Mean Corpuscular Volume (MCV)**
- 🧪 **Mean Corpuscular Hemoglobin (MCH)**
- 📈 **Mean Corpuscular Hemoglobin Concentration (MCHC)**
- 👤 **Gender**

<div align="center">

## ⚖️ Class Balance Management

![Balanced Dataset](images/After_SMOTE.png)

*Achieved perfect balance: 801 samples each for anemic and non-anemic classes using SMOTE*

## 🔍 Feature Importance Analysis

![Feature Importance](images/Feature_importance.png)

</div>

Key Contributors:
- 🟥 **Hemoglobin**: 87.0% contribution
- 👥 **Gender**: 9.1% contribution
- 🧬 **MCH**: 2.7% contribution
- 💉 **Others**: 1.2% contribution

<div align="center">

## <img src="https://user-images.githubusercontent.com/74038190/216126268-3e0ffee3-4448-4cec-9969-4bf6209ae1c1.png" width="30" /> Flask Web Application

</div>

### 🛠️ Application Structure
```bash
Directory structure:
└── yogeshwaran10-anemia_detection/
    ├── README.md
    ├── Procfile
    ├── app.py
    ├── process_image.py
    ├── requirements.txt
    ├── runtime.txt
    ├── utils.py
    ├── images/
    ├── model/
    │   └── random_forest_classifier.pkl
    ├── static/
    │   └── style.css
    └── templates/
        └── index.html
```

<div align="center">

## 💻 Installation & Usage

</div>

### 1️⃣ Clone the Repository
```bash
git clone <repository_url>
cd anemia-detection
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application
```bash
python app.py
```

Then open the app in your browser at `http://127.0.0.1:5000/`

<div align="center">

## 📈 Results

</div>

- ✅ **High Accuracy**: Achieved through class balancing and Random Forest optimization
- 🎯 **Precise Predictions**: Driven by significant features like hemoglobin levels
- 📸 **New Image Upload Feature**: Extracts blood test attributes automatically for prediction

<div align="center">

## 🔮 Future Scope

</div>

- 📊 **Expand dataset** to include more diverse features
- 🚀 **Implement advanced models** like XGBoost or LightGBM
- ⚖️ **Address Feature scaling** ⚙️ importance to other features

<div align="center">

## 📸 Screenshots

### 1. System Architecture
![System Architecture](images/diagram-export-5-21-2024-4_49_14-PM.png)

### 2. Balanced Dataset After SMOTE
![Balanced Dataset](images/After_SMOTE.png)

### 3. Feature Importance Analysis
![Feature Importance](images/Feature_importance.png)

</div>

---

<div align="center">

## <img src="https://user-images.githubusercontent.com/74038190/216125640-2783eae5-094f-4b20-a5bf-2c48260a43f5.png" width="30" /> **Live Deployment** ☁️ **Deployed on Render**

You can try the deployed version of the application here 🚀:

[**Anemia Detection App**](https://anemia-detection-46ji.onrender.com)

<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="400">

---

</div>

### **Outcome Variable Explanation:**

The **outcome variable** in the dataset indicates the final diagnosis or classification for each patient. The outcome is binary, with two possible values:

- **Not Anemic**: The patient is not anemic, based on clinical criteria and test results.
- **Anemic**: The patient is anemic, suggesting a deficiency of red blood cells or hemoglobin in the blood.

## <img src="https://user-images.githubusercontent.com/74038190/214644145-264f4759-7633-441e-9d67-d8dda9d50d26.gif" width="30" /> Contributing

Your contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest features
- 🔧 Submit pull requests

## 🐝 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

</div>
