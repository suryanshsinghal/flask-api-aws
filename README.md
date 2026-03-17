# 🚀 Flask API Deployment on AWS EC2

A production-ready Flask REST API deployed on AWS EC2 using Nginx, Gunicorn, and systemd.

---

## 🌐 Live Demo

http://13.233.197.179

---

## 📌 Features

- REST API built using Flask
- Interactive HTML landing page
- Dynamic API endpoints
- Deployed on AWS EC2 (Ubuntu)
- Production-ready setup using Gunicorn
- Nginx reverse proxy (runs on port 80)
- Systemd service for background execution and auto-start

---

## 🛠️ Tech Stack

- Python
- Flask
- AWS EC2
- Nginx
- Gunicorn
- Linux (Ubuntu)

---

## 📡 API Endpoints

| Endpoint | Description |
|---------|------------|
| `/` | Landing page (HTML UI) |
| `/api` | API metadata |
| `/user/{name}` | Dynamic greeting |
| `/health` | Health check |

---

## 📂 Project Structure

flask-api-aws/
├── app/
│ ├── app.py
│ └── requirements.txt
├── screenshots/
│ ├── ec2-instance.png
│ ├── api-running.png
│ ├── api-endpoint.png
│ └── terminal-deploy.png
└── README.md


---

## 📸 Screenshots

### 🔹 EC2 Instance (Running)
![EC2](screenshots/ec2-instance.png)

### 🔹 Application Running
![App](screenshots/api-running.png)

### 🔹 API Response
![API](screenshots/api-endpoint.png)

### 🔹 Systemd Service (Production Setup)
![Service](screenshots/terminal-deploy.png)

---

## ⚙️ Local Setup

```bash
git clone https://github.com/suryanshsinghal/flask-api-aws
cd flask-api-aws/app

python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt
python app.py


---

☁️ AWS Deployment Summary
- Created EC2 instance (Ubuntu)
- Configured security groups (ports 22, 80, 5000)
- Connected via SSH
- Cloned project from GitHub
- Set up Python virtual environment
- Installed dependencies
- Configured Gunicorn (WSGI server)
- Configured Nginx (reverse proxy)
- Created systemd service for auto-start


---

🚀 Production Architecture
Client → Nginx (Port 80) → Gunicorn → Flask App


---

🧪 Health Check
http://13.233.197.179/health


---

📚 Learning Outcomes
- Built REST API using Flask
- Deployed backend on AWS EC2
- Configured Linux server environment
- Implemented production setup (Gunicorn + Nginx)
- Managed services using systemd
- Understood reverse proxy architecture

---

👨‍💻 Author
- Suryansh


---

⭐ Future Improvements
- Add custom domain (Route 53)
- Enable HTTPS (SSL)
- Add database integration
- Implement CI/CD pipeline
