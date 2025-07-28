
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app import create_app, mysql

app = create_app()

def insert_predictions(csv_path='app/ai/detection_result.csv'):
    with app.app_context():
        df = pd.read_csv(csv_path)

        # Skip rows with 'normal' predictions
        threats = df[df['prediction'] != 'normal']
        if threats.empty:
            print("No threats to insert.")
            return

        cur = mysql.connection.cursor()
        for index, row in threats.iterrows():
            attack_type = row['prediction']
            score = row.get('ai_score', 'N/A')
            title = f"Detected: {attack_type}"
            description = f"Threat classified as '{attack_type}'"

            # Simple severity mapping
            if 'dos' in attack_type.lower():
                severity = 'high'
            elif 'probe' in attack_type.lower():
                severity = 'medium'
            else:
                severity = 'low'

            cur.execute("INSERT INTO incidents (title, description, severity) VALUES (%s, %s, %s)",
                        (title, description, severity))

        mysql.connection.commit()
        cur.close()
        print(f"{len(threats)} threat incidents inserted.")

if __name__ == '__main__':
    insert_predictions()
