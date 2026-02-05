import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

def preprocess_data(df):
    """
    Preprocesses the dataframe:
    - Encodes target variable
    - Splits into X and y
    - Scales numerical features
    - Returns X_train, X_test, y_train, y_test, scaler, le
    """
    # Copy to avoid setting with copy warning
    df = df.copy()
    
    # Encode target
    le = LabelEncoder()
    df['Risk_Level'] = le.fit_transform(df['Risk_Level'])
    
    X = df.drop('Risk_Level', axis=1)
    y = df['Risk_Level']
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler, le
