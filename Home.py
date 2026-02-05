import streamlit as st
from utils.ui_helper import apply_custom_style

st.set_page_config(
    page_title="Anti-Gravity Health",
    page_icon="🩺",
    layout="wide"
)
apply_custom_style()

st.title("🩺 Anti-Gravity – AI Health Monitoring System")

st.markdown("""
### Welcome to the Future of Personal Health Monitoring
This intelligent system uses Artificial Intelligence to analyze your vital signs and provide instant health risk assessments.

#### 🚀 Key Features:
- **Synthetic Data Generation**: Realistic health datasets created on the fly.
- **AI Risk Prediction**: Machine Learning models to predict health risks.
- **Smart Dashboard**: Visualize health trends and insights.
- **Health Score**: Get a personalized health score from 0-100.

#### 👈 Use the sidebar to navigate
- **Dashboard**: Explore the underlying health data.
- **Health Monitoring**: Enter your vitals to get a prediction.
- **About**: Learn more about the parameters and the project.
""")

st.subheader("Quick Navigation")
col1, col2, col3 = st.columns(3)
with col1:
    st.page_link("pages/1_Dashboard.py", label="Go to Dashboard", icon="📊")
with col2:
    st.page_link("pages/2_Health_Monitoring.py", label="Start Health Check", icon="🩺")
with col3:
    st.page_link("pages/3_About.py", label="Read About", icon="ℹ️")

st.info("💡 Note: This is a demonstration project using synthetic data.")
