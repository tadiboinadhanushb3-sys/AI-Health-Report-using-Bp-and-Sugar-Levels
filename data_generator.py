import pandas as pd
import numpy as np
import random

def generate_synthetic_data(n=1000):
    """
    Generates synthetic health data for training and testing.
    Features: Age, BMI, BP_Systolic, BP_Diastolic, Heart_Rate, SpO2
    Target: Risk_Level (Low, Medium, High)
    """
    np.random.seed(42)
    
    data = []
    
    for _ in range(n):
        age = np.random.randint(20, 80)
        
        # Base vitals based on age (rough approximation)
        bmi = np.random.uniform(18.5, 35.0)
        
        # Correlate BP with weight/age slightly
        bp_systolic = np.random.randint(90, 160)
        bp_diastolic = np.random.randint(60, 100)
        
        heart_rate = np.random.randint(50, 110)
        spo2 = np.random.randint(90, 100)
        
        # Determine Risk Level based on simple logic
        risk_score = 0
        if bmi > 30: risk_score += 2
        elif bmi > 25: risk_score += 1
        
        if bp_systolic > 140 or bp_diastolic > 90: risk_score += 2
        elif bp_systolic > 120 or bp_diastolic > 80: risk_score += 1
        
        if heart_rate > 100 or heart_rate < 60: risk_score += 1
        
        if spo2 < 95: risk_score += 2
        
        if age > 60: risk_score += 1
        
        if risk_score <= 1:
            risk_level = 'Low'
        elif risk_score <= 3:
            risk_level = 'Medium'
        else:
            risk_level = 'High'
            
        data.append([age, bmi, bp_systolic, bp_diastolic, heart_rate, spo2, risk_level])
        
    columns = ['Age', 'BMI', 'BP_Systolic', 'BP_Diastolic', 'Heart_Rate', 'SpO2', 'Risk_Level']
    df = pd.DataFrame(data, columns=columns)
    
    return df

if __name__ == "__main__":
    df = generate_synthetic_data(10)
    print(df.head())
