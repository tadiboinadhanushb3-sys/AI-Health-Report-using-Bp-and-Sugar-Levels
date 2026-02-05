
import streamlit as st
import pandas as pd
from utils.health_metrics import (
    calculate_bmi, classify_bmi, 
    classify_bp, classify_sugar, 
    calculate_health_score, get_health_status, 
    get_risk_assessment, get_detailed_alerts, 
    get_smart_recommendations
)
from utils.ui_helper import apply_custom_style, card_component

# Attempt import of generator
try:
    from utils.report_generator import generate_pdf_report
    has_pdf_lib = True
except ImportError:
    has_pdf_lib = False

st.set_page_config(page_title="Check Your Health", page_icon="🩺", layout="wide")
apply_custom_style()

st.title("🏥 Health Risk Assessment")
st.markdown("Enter your vitals below. Our system observes strict medical thresholds to evaluate your health.")

with st.form("health_form"):
    st.subheader("📝 Patient Information")
    c1, c2, c3 = st.columns(3)
    with c1:
        age = st.number_input("Age (Years)", min_value=1, max_value=120, value=30)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    with c2:
        height = st.number_input("Height (cm)", min_value=50, max_value=250, value=170)
    with c3:
        weight = st.number_input("Weight (kg)", min_value=10, max_value=300, value=70)
        
    st.subheader("🩺 Vitals Measurements")
    c4, c5, c6 = st.columns(3)
    with c4:
        systolic = st.number_input("Systolic BP (mmHg)", min_value=50, max_value=300, value=120)
        diastolic = st.number_input("Diastolic BP (mmHg)", min_value=30, max_value=200, value=80)
    with c5:
        sugar = st.number_input("Blood Sugar (mg/dL)", min_value=20, max_value=600, value=95, help="Random / Post-prandial Glucose")
        heart_rate = st.number_input("Heart Rate (bpm)", min_value=30, max_value=220, value=72)
    with c6:
        st.write("") # Spacer

    submit_btn = st.form_submit_button("Analyze Results")

if submit_btn:
    # Calculations
    bmi = calculate_bmi(height, weight)
    bmi_cat, bmi_color = classify_bmi(bmi)
    
    bp_cat, bp_color = classify_bp(systolic, diastolic)
    
    sugar_cat, sugar_color = classify_sugar(sugar)
    
    health_score = calculate_health_score(bmi, systolic, diastolic, sugar, heart_rate, age)
    health_status, status_color = get_health_status(health_score)
    risk_level = get_risk_assessment(health_score)
    
    risk_color_map = {"Low Risk": "green", "Medium Risk": "orange", "High Risk": "red"}
    risk_color = risk_color_map.get(risk_level, "blue")
    
    # --- Summary Section ---
    st.divider()
    
    # Large Summary Card
    st.markdown(f"""
        <div class="summary-card">
            <div class="summary-title">Overall Health Status</div>
            <div class="summary-risk" style="color: {risk_color_map.get(risk_level, 'black')}">{risk_level}</div>
            <div class="summary-subtitle">Calculated Health Score: {health_score}/100</div>
            <hr style="margin: 20px auto; width: 50%; border-top: 1px solid #ddd;">
             <div style="font-size: 1.3rem; font-weight: 600; color: #444;">
                BMI: <span style="font-size: 1.5rem; font-weight: 800;">{bmi:.1f}</span> 
                <span style="background-color: #eee; padding: 4px 12px; border-radius: 15px; margin-left: 10px; font-size: 1rem;">{bmi_cat}</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    
    st.subheader("📊 Detailed Vitals")
    
    # Detailed Cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        card_component("Blood Pressure", f"{systolic}/{diastolic}", bp_cat, bp_color)
    with col2:
        card_component("Blood Sugar", f"{sugar}", sugar_cat, sugar_color, "mg/dL")
    with col3:
        card_component("Heart Rate", f"{heart_rate}", "Measured", "blue", "bpm")

        
    # Recommendations & Alerts
    st.divider()
    
    alerts = get_detailed_alerts(bmi, systolic, diastolic, sugar)
    recs = get_smart_recommendations(risk_level, alerts) # Alerts is list of tuples here, passing direct
    
    r_col1, r_col2 = st.columns([1, 1])
    
    with r_col1:
        st.subheader("⚠️ Medical Alerts")
        if alerts:
            for title, msg in alerts:
                st.error(f"**{title}**: {msg}")
        else:
            st.success("✅ No critical medical alerts detected.")
            
    with r_col2:
        st.subheader("💡 Lifestyle Recommendations")
        for rec in recs:
            st.info(f"• {rec}")
            
    # --- PDF Generation ---
    st.divider()
    col_dl, col_sp = st.columns([1, 2])
    with col_dl:
        if has_pdf_lib:
            # Prepare data
            user_data = {
                "age": age, "gender": gender, "height": height, "weight": weight,
                "systolic": systolic, "diastolic": diastolic, "sugar": sugar, "heart_rate": heart_rate
            }
            results = {
                "bmi": bmi, "bmi_cat": bmi_cat, "risk_level": risk_level, "health_score": health_score
            }
            
            pdf_file = generate_pdf_report(user_data, results, alerts, recs)
            
            st.download_button(
                label="📥 Download Health Report (PDF)",
                data=pdf_file,
                file_name="Health_Report.pdf",
                mime="application/pdf",
                key="pdf_download"
            )
        else:
            st.warning("⚠️ PDF Generator library not installed. Please install 'fpdf'.")

    # Disclaimer
    st.markdown('<div class="medical-disclaimer">⚠️ This application is for educational purposes only and not a medical diagnosis. Please consult a healthcare professional for advice.</div>', unsafe_allow_html=True)
