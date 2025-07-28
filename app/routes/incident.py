
from flask import Blueprint, render_template
from app import mysql

incident_bp = Blueprint('incident', __name__)

@incident_bp.route('/')
def dashboard():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM incidents ORDER BY timestamp DESC")
    incidents = cur.fetchall()
    cur.close()
    return render_template('dashboard.html', incidents=incidents)
