# Anti-Gravity – AI Health Monitoring System

An intelligent health monitoring application built with Streamlit and AI.

## Project Overview
This application predicts health risks and calculates a health score based on user vitals (Age, BMI, Blood Pressure, Heart Rate, SpO2).

## Features
- **Health Score**: 0-100 rating algorithm.
- **AI Risk Prediction**: Machine Learning model (Random Forest / Logistic Regression) to detect health risks.
- **Smart Alerts**: Detailed warnings for abnormal vitals.
- **Interactive Dashboard**: Modern UI with charts and visualizations.

## Folder Structure
```
anti_gravity_health_system/
├── Home.py                 # Main App
├── requirements.txt        # Dependencies
├── models/                 # ML Models
├── pages/                  # Multipage Modules
└── utils/                  # Logic & UI Helpers
```

## How to Run Locally
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run Home.py
   ```

## Deployment on Streamlit Community Cloud
1. Push this code to a GitHub repository.
2. Login to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Connect your GitHub and select this repository.
4. Set "Main file path" to `Home.py`.
5. Click **Deploy**.

### Common Deployment Mistakes & Fixes
- **`ModuleNotFoundError`**: Ensure you have an empty `__init__.py` file in the `utils/` folder (we have included this).
- **`FileNotFoundError` (models)**: Ensure the `models/` directory works locally. If generated at runtime, make sure `models/` exists. (Ideally, commit the trained `.pkl` files or run the training script during the build if using a custom build process, but committing the model is easier for Streamlit Cloud).
- **Dependencies**: Ensure `requirements.txt` is in the root directory.

## Credits
Built by Anti-Gravity Team (Deepmind).
