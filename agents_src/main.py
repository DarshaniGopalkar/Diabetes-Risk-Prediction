import sys
import os
import random
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.settings import Settings
from crew import diabetes_prediction_crew

settings = Settings()

# Normalization / validation ranges
RANGES = {
    "Pregnancies": (0, 15),
    "Glucose": (70, 200),
    "BloodPressure": (50, 120),
    "SkinThickness": (10, 50),
    "Insulin": (15, 276),
    "BMI": (18, 40),
    "DiabetesPedigreeFunction": (0.1, 2.5),
    "Age": (10, 90)
}

def normalize_patient_data(patient_data: dict) -> dict:
    """Clamp values to realistic medical ranges."""
    normalized = {}
    for key, (min_val, max_val) in RANGES.items():
        if key in patient_data:
            normalized[key] = min(max(patient_data[key], min_val), max_val)
        else:
            # If key missing, use mid-range value
            normalized[key] = (min_val + max_val) / 2
    return normalized

def generate_random_patient() -> dict:
    """Generate a random patient dictionary with realistic values."""
    return {key: random.uniform(*RANGES[key]) if isinstance(RANGES[key][0], float) else random.randint(*RANGES[key])
            for key in RANGES}

def run(patient_data: dict):
    normalized_data = normalize_patient_data(patient_data)
    print(f"Patient Data (Normalized): {normalized_data}")
    try:
        result = diabetes_prediction_crew.kickoff(inputs={"patient_data": normalized_data})
        print(f"Prediction Result: {result}")
    except Exception as e:
        print(f"Error during prediction: {e}")

if __name__ == "__main__":
    # Predefined patients
    patient_diabetic = {
        "Pregnancies": 3,
        "Glucose": 150,
        "BloodPressure": 80,
        "SkinThickness": 25,
        "Insulin": 100,
        "BMI": 30.5,
        "DiabetesPedigreeFunction": 0.6,
        "Age": 40
    }

    patient_non_diabetic = {
        "Pregnancies": 1,
        "Glucose": 95,
        "BloodPressure": 70,
        "SkinThickness": 20,
        "Insulin": 85,
        "BMI": 22.5,
        "DiabetesPedigreeFunction": 0.2,
        "Age": 25
    }

    print("=== Predefined Patients ===")
    run(patient_diabetic)  # Likely diabetic
    print("-"*50)
    run(patient_non_diabetic)  # Likely non-diabetic
    print("-"*50)

    print("=== Random Patients ===")
    for i in range(3):  # Generate 3 random patients
        random_patient = generate_random_patient()
        run(random_patient)
        print("-"*50)
