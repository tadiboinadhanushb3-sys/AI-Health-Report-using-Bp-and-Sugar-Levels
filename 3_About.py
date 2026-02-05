import streamlit as st
from utils.ui_helper import apply_custom_style

st.set_page_config(page_title="About", page_icon="ℹ️")
apply_custom_style()

st.title("ℹ️ About the Metrics")

st.markdown("""
This application uses standard medical ranges to evaluate your health. Here is a breakdown of the metrics used:

### 1. BMI (Body Mass Index)
- **Formula:** Weight (kg) / Height (m)²
- **Normal Range:** 18.5 – 24.9
- **Impact:** High BMI is linked to heart disease and diabetes.

### 2. Blood Pressure (BP)
- **Systolic:** Pressure when heart beats (Upper number). Ideal < 120.
- **Diastolic:** Pressure when heart rests (Lower number). Ideal < 80.
- **Impact:** Hypertension is a "silent killer."

### 3. Heart Rate
- **Resting:** 60 – 100 bpm is normal.
- **Impact:** High or low heart rates can indicate cardiovascular issues.

### 4. SpO2 (Oxygen Saturation)
- **Normal:** 95% – 100%
- **Impact:** Low oxygen levels can indicate respiratory problems.

### 5. Health Score Calculation
The **Anti-Gravity Health Score** starts at 100 (Perfect).
- **-10 to -20** for BMI deviations.
- **-15** for abnormal Blood Pressure.
- **-10** for abnormal Heart Rate.
- **-20** for low SpO2.

---
**Disclaimer:** This tool is for educational purposes only and does not replace professional medical advice.
""")
