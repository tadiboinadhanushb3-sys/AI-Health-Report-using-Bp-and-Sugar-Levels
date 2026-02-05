import pandas as pd
import pickle
import os
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from utils.data_generator import generate_synthetic_data
from utils.preprocessor import preprocess_data

MODELS_DIR = "models"
MODEL_PATH = os.path.join(MODELS_DIR, "best_model.pkl")
SCALER_PATH = os.path.join(MODELS_DIR, "scaler.pkl")
ENCODER_PATH = os.path.join(MODELS_DIR, "encoder.pkl")

def train_and_save_model():
    # 1. Generate Data
    print("Generating synthetic data...")
    df = generate_synthetic_data(n=2000)
    
    # 2. Preprocess
    print("Preprocessing data...")
    X_train, X_test, y_train, y_test, scaler, le = preprocess_data(df)
    
    # 3. Train Models
    print("Training Logistic Regression...")
    lr = LogisticRegression()
    lr.fit(X_train, y_train)
    lr_pred = lr.predict(X_test)
    lr_acc = accuracy_score(y_test, lr_pred)
    print(f"Logistic Regression Accuracy: {lr_acc:.4f}")
    
    print("Training Random Forest...")
    rf = RandomForestClassifier(random_state=42)
    rf.fit(X_train, y_train)
    rf_pred = rf.predict(X_test)
    rf_acc = accuracy_score(y_test, rf_pred)
    print(f"Random Forest Accuracy: {rf_acc:.4f}")
    
    # 4. Select Best Model
    if rf_acc >= lr_acc:
        best_model = rf
        print("Best model: Random Forest")
    else:
        best_model = lr
        print("Best model: Logistic Regression")
        
    # 5. Save Model and Artifacts
    if not os.path.exists(MODELS_DIR):
        os.makedirs(MODELS_DIR)
        
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(best_model, f)
        
    with open(SCALER_PATH, 'wb') as f:
        pickle.dump(scaler, f)
        
    with open(ENCODER_PATH, 'wb') as f:
        pickle.dump(le, f)
        
    print(f"Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    train_and_save_model()
