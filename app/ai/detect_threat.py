
import pandas as pd
import joblib

def detect_threat(csv_path='kdd_sample.csv', model_path='ai_model.pkl'):
    df = pd.read_csv(csv_path)

    X = df.drop('label', axis=1)

    scaler = joblib.load('scaler.pkl')
    X_scaled = scaler.transform(X)

    model = joblib.load(model_path)
    predictions = model.predict(X_scaled)

    if 'label_encoder.pkl' in model_path or True:
        try:
            le = joblib.load('label_encoder.pkl')
            labels = le.inverse_transform(predictions)
        except:
            labels = predictions
    else:
        labels = predictions

    df['prediction'] = labels
    df.to_csv('detection_result.csv', index=False)

    print("Threat detection completed. Output written to detection_result.csv")

if __name__ == '__main__':
    detect_threat()
