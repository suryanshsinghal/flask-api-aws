from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False  # keep order clean


# 🌐 Home Route (Nice UI for browser)
@app.route('/')
def home():
    return f"""
    <html>
    <head>
        <title>Flask API</title>
        <style>
            body {{
                font-family: Arial;
                text-align: center;
                margin-top: 50px;
                background-color: #f4f6f8;
            }}
            .box {{
                background: white;
                padding: 20px;
                margin: auto;
                width: 50%;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #2c3e50;
            }}
            ul {{
                list-style-type: none;
                padding: 0;
            }}
            li {{
                margin: 10px 0;
                font-size: 18px;
            }}
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🚀 Flask API is Live!</h1>
            <p><b>Project:</b> Cloud Deployed Flask API</p>
            <p><b>Author:</b> Suryansh</p>
            <p><b>Status:</b> Running ✅</p>
            <p><b>Time:</b> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>

            <h3>Available Endpoints:</h3>
<ul>
    <li><a href="/api">/api</a></li>
    <li><a href="/user/Suryansh">/user/{{name}}</a> (replace with any name)</li>
    <li><a href="/health">/health</a></li>
</ul>

            <p><i>Deployed on AWS EC2 using Ubuntu</i></p>
        </div>
    </body>
    </html>
    """


# 🔗 API Route (JSON)
@app.route('/api')
def api():
    return jsonify({
        "project": "Cloud Deployed Flask API",
        "author": "Suryansh",
        "version": "1.0.0",
        "status": "running",
        "message": "My Flask API is live on AWS EC2 🚀",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "tech_stack": ["Python", "Flask", "AWS EC2", "Linux"],
        "endpoints": {
            "/": "Landing page",
            "/api": "API info",
            "/user/{name}": "Dynamic user greeting",
            "/health": "Health check endpoint"
        }
    })


# 👤 Dynamic Route
@app.route('/user/<name>')
def user(name):
    return jsonify({
        "user": name,
        "message": f"Hello, {name}! Welcome to my API 🚀"
    })


# ❤️ Health Check
@app.route('/health')
def health():
    return jsonify({
        "status": "OK",
        "server": "running"
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
