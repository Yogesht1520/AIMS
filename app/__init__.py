from flask import Flask
from flask_mysqldb import MySQL

mysql = MySQL()

def create_app():
    app = Flask(__name__)

    # Configuration for MySQL
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'root'
    app.config['MYSQL_DB'] = 'aims_db'

    mysql.init_app(app)

    # Register Blueprints
    from app.routes.incident import incident_bp
    app.register_blueprint(incident_bp)

    return app
