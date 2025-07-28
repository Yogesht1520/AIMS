
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_kdd(input_csv='kddcup99_csv.csv', output_csv='kdd_sample.csv'):
    print("Loading dataset...")
    df = pd.read_csv(input_csv)

    # Encode categorical columns
    categorical_cols = ['protocol_type', 'service', 'flag']
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])

    df.to_csv(output_csv, index=False)
    print(f"✅ Preprocessing complete. Saved to: {output_csv}")

if __name__ == '__main__':
    preprocess_kdd()
