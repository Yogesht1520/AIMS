
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib

def train_model(csv_path='kdd_sample.csv', model_path='ai_model.pkl'):
    df = pd.read_csv(csv_path)

    # Basic preprocessing: drop non-numeric columns and encode target
    X = df.drop('label', axis=1)
    y = df['label']

    # Encode labels if categorical
    if y.dtype == 'object':
        le = LabelEncoder()
        y = le.fit_transform(y)
        joblib.dump(le, 'label_encoder.pkl')

    # Normalize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    joblib.dump(scaler, 'scaler.pkl')

    # Train model
    model = DecisionTreeClassifier(max_depth=10, random_state=42)
    model.fit(X_scaled, y)

    joblib.dump(model, model_path)
    print(f"Model trained and saved to {model_path}")

if __name__ == '__main__':
    train_model()
