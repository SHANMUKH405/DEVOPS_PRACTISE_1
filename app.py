"""
Simple Flask application for DevOps practice
"""
from flask import Flask, jsonify, render_template_string
import os
import socket
from datetime import datetime

app = Flask(__name__)

# HTML template for the home page
HOME_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Practice Project 1</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .container {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        }
        h1 {
            text-align: center;
            margin-bottom: 30px;
            font-size: 2.5em;
        }
        .info {
            background: rgba(255, 255, 255, 0.2);
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
        }
        .info-item {
            margin: 10px 0;
            font-size: 1.1em;
        }
        .info-label {
            font-weight: bold;
            color: #ffd700;
        }
        a {
            color: #ffd700;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .endpoints {
            margin-top: 30px;
        }
        .endpoint {
            background: rgba(255, 255, 255, 0.15);
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 DevOps Practice Project 1</h1>
        <div class="info">
            <div class="info-item">
                <span class="info-label">Status:</span> ✅ Running
            </div>
            <div class="info-item">
                <span class="info-label">Hostname:</span> {{ hostname }}
            </div>
            <div class="info-item">
                <span class="info-label">Environment:</span> {{ environment }}
            </div>
            <div class="info-item">
                <span class="info-label">Version:</span> {{ version }}
            </div>
            <div class="info-item">
                <span class="info-label">Time:</span> {{ current_time }}
            </div>
        </div>
        
        <div class="endpoints">
            <h2>Available Endpoints:</h2>
            <div class="endpoint">
                <a href="/">GET /</a> - Home page (this page)
            </div>
            <div class="endpoint">
                <a href="/health">GET /health</a> - Health check endpoint
            </div>
            <div class="endpoint">
                <a href="/api/info">GET /api/info</a> - API info endpoint (JSON)
            </div>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    """Home page with application information"""
    return render_template_string(
        HOME_TEMPLATE,
        hostname=socket.gethostname(),
        environment=os.getenv('ENVIRONMENT', 'development'),
        version=os.getenv('APP_VERSION', '1.0.0'),
        current_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'hostname': socket.gethostname()
    }), 200

@app.route('/api/info')
def info():
    """API endpoint that returns application information"""
    return jsonify({
        'application': 'DevOps Practice Project 1',
        'version': os.getenv('APP_VERSION', '1.0.0'),
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'hostname': socket.gethostname(),
        'timestamp': datetime.now().isoformat()
    }), 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
