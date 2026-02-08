# 🚀 PipeTier — Containerized Backend with Persistent Storage

PipeTier is a **Dockerized Flask backend** connected to **MySQL**, built to demonstrate **real backend execution, container orchestration, and data persistence**, with verified testing and cloud hosting proof.

This project focuses on **working systems**, not slides or mock demos.

---

## 🧠 One-Line Truth

**A real backend API that runs in Docker, stores data in MySQL, and is verified locally and on AWS EC2.**

---

## ❓ Why This Project Exists

In many beginner projects:
- APIs run only on localhost
- Docker is used without persistence
- Cloud experience is claimed without proof

**PipeTier exists to close that gap.**

It answers:
> *Can this backend actually run, store data, and be verified end-to-end?*

---

## 📌 What PipeTier IS / IS NOT

### ✅ PipeTier IS
- A Flask REST API 🐍
- Dockerized using Docker & Docker Compose 🐳
- Connected to MySQL with persistent storage 🗄️
- Tested using Postman 🔍
- Verified on AWS EC2 ☁️

### ❌ PipeTier is NOT
- A frontend app
- A SaaS product
- A managed cloud service
- A fake demo or screenshot-only project

---

## 🏗️ System Architecture

```text
Client (Postman / Browser)
        ↓
Flask API (Docker container)
        ↓
MySQL Database (Docker container)
        ↓
Docker Volume (Persistent Storage)
```

---


## Why This Design?

- This project uses a simple and practical two-tier architecture to demonstrate real-world containerized deployment patterns.
- Docker Compose simplifies the setup of multiple services with a single command.
- Service-name based networking (mysql) reflects actual Docker container communication instead of using localhost.
- Persistent volumes ensure database data is not lost when containers restart.
- Flask provides a lightweight, readable backend suitable for learning and rapid development.

---


## ⚙️ Tech Stack

- 🐍 Python (Flask) — Backend web application
- 🐳 Docker — Containerization
- 🧩 Docker Compose — Multi-container orchestration
- 🗄️ MySQL 8.0 — Relational database
- 🔍 Postman — API testing
- ☁️ AWS EC2 (t3.micro) — Cloud deployment environment

