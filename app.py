from flask import Flask, render_template_string
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def index():
    try:
        conn = mysql.connector.connect(
            host=os.environ.get('DB_HOST', 'db'),
            user=os.environ.get('DB_USER', 'root'),
            password=os.environ.get('DB_PASSWORD', 'rootpass'),
            database=os.environ.get('DB_NAME', 'appdb')
        )
        return "<h1>Flask app is running and connected to MySQL</h1>"
    except Exception as e:
        return f"<h1>Flask is running but DB not connected: {str(e)}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
