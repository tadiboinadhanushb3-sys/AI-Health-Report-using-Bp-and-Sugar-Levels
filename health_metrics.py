
def calculate_bmi(height_cm, weight_kg):
    """Calculates BMI from height in cm and weight in kg."""
    if height_cm <= 0:
        return 0
    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)

def classify_bmi(bmi):
    """Classifies BMI into standard categories."""
    if bmi < 18.5:
        return "Underweight", "blue"
    elif 18.5 <= bmi < 24.9:
        return "Normal", "green"
    elif 25 <= bmi < 29.9:
        return "Overweight", "orange"
    else:
        return "Obese", "red"

def classify_bp(systolic, diastolic):
    """Classifies Blood Pressure based on standard ranges (e.g., AHA)."""
    if systolic < 120 and diastolic < 80:
        return "Normal", "green"
    elif 120 <= systolic < 130 and diastolic < 80:
        return "Elevated", "yellow"
    elif 130 <= systolic < 140 or 80 <= diastolic < 90:
        return "Hypertension Stage 1", "orange"
    elif systolic >= 140 or diastolic >= 90:
        return "Hypertension Stage 2", "red"
    elif systolic > 180 or diastolic > 120:
        return "Hypertensive Crisis", "red" # Critical
    else:
        return "Normal", "green" # Fallback

def classify_sugar(sugar_mg_dl):
    """Classifies Blood Sugar (assuming random/post-prandial for general screening)."""
    # Random Glucose Reference:
    # Normal: < 140 mg/dL
    # Prediabetes: 140 - 199 mg/dL
    # Diabetes: >= 200 mg/dL
    if sugar_mg_dl < 140:
        return "Normal", "green"
    elif 140 <= sugar_mg_dl < 200:
        return "Prediabetic", "orange"
    else:
        return "High (Diabetes Risk)", "red"

def calculate_health_score(bmi, systolic, diastolic, sugar, heart_rate, age):
    """
    Calculates a heuristic health score (0-100).
    100 = Perfect Health
    Penalties applied for deviations from normal ranges.
    """
    score = 100
    
    # BMI Penalties
    if bmi < 18.5: score -= 10
    elif 25 <= bmi < 30: score -= 10
    elif bmi >= 30: score -= 20
    
    # BP Penalties
    if systolic >= 130 or diastolic >= 80: score -= 15
    if systolic >= 140 or diastolic >= 90: score -= 15 # Cumulative
    if systolic > 180 or diastolic > 120: score -= 20
    
    # Sugar Penalties
    if sugar >= 140: score -= 15
    if sugar >= 200: score -= 15
    
    # Heart Rate Penalties (Resting assumption)
    if heart_rate < 60 or heart_rate > 100: score -= 10
    
    # Age factor (minor adjustment, harder to maintain perfect score as we age)
    if age > 50: score -= 5
    
    return max(0, score)

def get_health_status(score):
    if score >= 80:
        return "Excellent", "green"
    elif 60 <= score < 80:
        return "Good", "blue"
    elif 40 <= score < 60:
        return "Fair", "orange"
    else:
        return "Poor", "red"

def get_risk_assessment(score):
    if score >= 85:
        return "Low Risk"
    elif 50 <= score < 85:
        return "Medium Risk"
    else:
        return "High Risk"

def get_detailed_alerts(bmi, systolic, diastolic, sugar):
    """Generates specific alert messages."""
    alerts = []
    
    # BMI Alerts
    if bmi >= 30:
        alerts.append(("Obesity Alert", "Your BMI indicates obesity. This increases risk for heart disease and diabetes."))
    
    # BP Alerts
    if systolic >= 140 or diastolic >= 90:
        alerts.append(("High Blood Pressure", "Readings suggest Hypertension. Please consult a doctor."))
    elif systolic > 180 or diastolic > 120:
        alerts.append(("CRITICAL BP ALERT", "Hypertensive Crisis levels detected. Seek immediate medical attention."))
        
    # Sugar Alerts
    if sugar >= 200:
        alerts.append(("High Blood Sugar", "Glucose levels are in the diabetic range. Medical checkup recommended."))
        
    return alerts

def get_smart_recommendations(risk_level, alerts_count):
    recs = []
    
    rec_pool = {
        "General": [
            "Maintain a balanced diet rich in vegetables and whole grains.",
            "Aim for at least 30 minutes of moderate exercise daily.",
            "Stay hydrated and ensure 7-8 hours of sleep."
        ],
        "High BP": [
            "Reduce sodium (salt) intake in your diet.",
            "Limit alcohol and caffeine consumption.",
            "Practice stress-reducing techniques like meditation."
        ],
        "High Sugar": [
            "Monitor carbohydrate intake.",
            "Avoid sugary drinks and processed foods.",
            "Regular physical activity helps improve insulin sensitivity."
        ],
        "Weight": [
            "Focus on portion control.",
            "Incorporate strength training to boost metabolism."
        ]
    }
    
    recs.extend(rec_pool["General"])
    
    if "High Blood Pressure" in str(alerts_count) or "BP" in str(alerts_count):
        recs.extend(rec_pool["High BP"])
        
    if "Sugar" in str(alerts_count):
        recs.extend(rec_pool["High Sugar"])
        
    return recs[:4] # Return top 4
