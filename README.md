# 🚀 Flask API Deployment on AWS EC2

A production-ready Flask REST API deployed on AWS EC2 using Nginx, Gunicorn, and systemd.

---

## 🌐 Live Demo

http://13.233.197.179/

---

## 📌 Features

- REST API built using Flask
- Interactive HTML landing page
- Dynamic API endpoints
- Deployed on AWS EC2 (Ubuntu)
- Production setup using Gunicorn
- Nginx reverse proxy (no :5000)
- Systemd service for auto-start and background execution

---

## 🛠️ Tech Stack

- Python
- Flask
- AWS EC2
- Nginx
- Gunicorn
- Linux (Ubuntu)
- GitHub

---

## 📡 API Endpoints

| Endpoint | Description |
|---------|------------|
| `/` | Landing page (HTML UI) |
| `/api` | API information |
| `/user/{name}` | Dynamic greeting |
| `/health` | Health check |

---

## ⚙️ Local Setup

### 1. Clone repository
```bash
git clone https://github.com/suryanshsinghal/flask-api-aws
cd flask-api-aws
