import pandas as pd
import plotly.express as px
import streamlit as st
from utils.data_generator import generate_synthetic_data
from utils.ui_helper import apply_custom_style

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

apply_custom_style()
st.title("📊 Health Data Dashboard")


# Generate data on the fly if not already loaded (or just generate new for demo)
if 'data' not in st.session_state:
    with st.spinner('Generating synthetic health data...'):
        st.session_state['data'] = generate_synthetic_data(n=500)

df = st.session_state['data']

# Top Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Records", len(df))
col2.metric("High Risk Cases", len(df[df['Risk_Level'] == 'High']))
col3.metric("Avg Age", f"{df['Age'].mean():.1f}")

st.markdown("---")

# Visualizations
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Risk Level Distribution")
    fig_risk = px.pie(df, names='Risk_Level', title='Distribution of Health Risk', hole=0.4, color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig_risk, use_container_width=True)

with col_right:
    st.subheader("BMI vs Heart Rate")
    fig_scatter = px.scatter(df, x='BMI', y='Heart_Rate', color='Risk_Level', title='BMI vs Heart Rate Correlation')
    st.plotly_chart(fig_scatter, use_container_width=True)

st.subheader("Vitals Overview")
tab1, tab2 = st.tabs(["Blood Pressure", "SpO2 & Age"])

with tab1:
    fig_bp = px.histogram(df, x='BP_Systolic', color='Risk_Level', nbins=30, title='Systolic Blood Pressure Distribution')
    st.plotly_chart(fig_bp, use_container_width=True)

with tab2:
    fig_age_spo2 = px.box(df, x='Risk_Level', y='SpO2', title='SpO2 Levels by Risk Category')
    st.plotly_chart(fig_age_spo2, use_container_width=True)

st.markdown("### Raw Data Sample")
st.dataframe(df.head())
