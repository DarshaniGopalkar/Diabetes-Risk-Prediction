# Diabetes Risk Prediction

An AI-powered and Machine Learning-based project that predicts whether a patient is diabetic or non-diabetic based on health parameters. This project combines traditional ML models with an LLM (Large Language Model) to provide accurate predictions and plain-language explanations.

## Sample Output

**Diabetic Patient Example:**

![Diabetic Patient Output](diabetic_output.png)

## Features

Predicts Diabetic or Non-Diabetic from patient health data.

Uses ML models (trained on diabetes dataset) for prediction.

Optionally integrates LLM for advanced insights and explanations.

Accepts custom user input or random patient data.

Provides plain-language explanations for predictions.

Robust and user-friendly for any input data.

## Usage
1. Run via Python
python ml_src/predict_diabetes.py

Example patient data:

patient_data = {
    "Pregnancies": 3,
    "Glucose": 150,
    "BloodPressure": 80,
    "SkinThickness": 25,
    "Insulin": 100,
    "BMI": 30.5,
    "DiabetesPedigreeFunction": 0.6,
    "Age": 40
}
run(patient_data)

2. Run via Streamlit Web App
streamlit run streamlit_src/app.py


- Enter patient health data through the interface.

- Get instant prediction and explanation.

## Sample Output

- Diabetic Patient Example:

Patient Data:
Glucose: 150
BMI: 30.5
...

Prediction Result:
Status: Diabetic
Explanation: High glucose and BMI levels indicate a high risk of diabetes.


- Non-Diabetic Patient Example:

Patient Data:
Glucose: 95
BMI: 22.5
...

Prediction Result:
Status: Non-Diabetic
Explanation: Normal glucose and BMI levels indicate low risk of diabetes.

## Notes

The project uses CrewAI and litellm for AI-based predictions.

Make sure API keys and LLM credentials are set in .env or config/settings.py.
