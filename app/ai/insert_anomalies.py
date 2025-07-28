
import pandas as pd
from app import create_app, mysql

app = create_app()

def insert_anomalies(csv_path='app/ai/detection_result.csv'):
    with app.app_context():
        df = pd.read_csv(csv_path)

        anomalies = df[df['threat'] == 'Anomaly']
        if anomalies.empty:
            print("No anomalies found in detection_result.csv.")
            return

        cur = mysql.connection.cursor()
        for index, row in anomalies.iterrows():
            title = f"Anomaly Detected: Row {index}"
            description = f"Detected unusual behavior with score {row['ai_score']:.3f}"
            severity = 'medium'
            cur.execute("INSERT INTO incidents (title, description, severity) VALUES (%s, %s, %s)",
                        (title, description, severity))

        mysql.connection.commit()
        cur.close()
        print(f"{len(anomalies)} anomalies inserted into incidents table.")

if __name__ == '__main__':
    insert_anomalies()
