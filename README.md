# 🚀 PipeTier — Containerized Backend with Persistent Storage

PipeTier is a **Dockerized Flask backend** connected to **MySQL**, built to demonstrate **real backend execution, container orchestration, and data persistence**, with verified testing and cloud hosting proof.

> This project focuses on **working systems**, not slides or mock demos.

## ❓ Why This Project Exists :

In many beginner projects:
- APIs run only on localhost
- Docker is used without persistence
- Cloud experience is claimed without proof

**PipeTier exists to close that gap.**

It answers:
> *Can this backend actually run, store data, and be verified end-to-end?*


## 🧩 Real Problems PipeTier Solves :

| Real-World Problem | What Usually Happens | How PipeTier Solves It |
|--------------------|----------------------|-------------------------|
| Backend runs only on localhost | Apps work only on developer machines | Runs inside Docker containers, making it portable and reproducible |
| Database data gets lost on restart | Containers are recreated without persistent storage | Uses Docker volumes to ensure MySQL data persists |
| Hard-to-setup multi-service apps | Manual setup of backend and database leads to errors | Docker Compose brings up the full stack with one command |
| Incorrect container networking | Developers use `localhost` instead of service names | Uses service-name based networking (`mysql`) like real deployments |
| No proof of actual execution | Projects show only code or screenshots without verification | Includes real test results and EC2 deployment proof |
| Lack of cloud deployment experience | Many projects never leave the local machine | Deployed and tested on AWS EC2 with public access |
| Unverified APIs | Endpoints are not tested end-to-end | Tested with real POST and GET requests using Postman |
| No persistent system behavior | Data disappears between runs | Demonstrates stateful backend with persistent storage |


## 🏗️ System Architecture :
![System Architecture](architecture.png)

## Why This Design?

- This project uses a simple and practical two-tier architecture to demonstrate real-world containerized deployment patterns.
- Docker Compose simplifies the setup of multiple services with a single command.
- Service-name based networking (mysql) reflects actual Docker container communication instead of using localhost.
- Persistent volumes ensure database data is not lost when containers restart.
- Flask provides a lightweight, readable backend suitable for learning and rapid development.

## 📈 Core Features :

| ✅ What This Project IS | ❌ What This Project is NOT |
|------------------------|---------------------------|
| Containerized Backend System — Flask REST API running inside Docker with service orchestration via Docker Compose | Not a simple local script or non-containerized backend |
| Persistent Data Layer — MySQL integrated with volume-based storage to ensure data durability across container restarts | Not an in-memory or temporary database setup |
| API-Driven Architecture — Exposes structured REST endpoints tested via Postman for real request/response validation | Not a UI-based or frontend-heavy application |
| Production-Like Deployment — Runs on AWS EC2 simulating real cloud-hosted backend execution | Not a local-only or mock deployment |
| Service-Oriented Setup — Backend and database run as isolated, connected services using Docker networking | Not a monolithic or tightly coupled setup |
| Verified End-to-End System — API → Container → Database flow tested and validated with real data persistence | Not a static demo or screenshot-only project |

## 🔄 Request Lifecycle :

***Flow***
Client → Flask API → Business Logic → MySQL → Response

***Step-by-step***
1. Client sends HTTP request to Flask endpoint  
2. Flask validates input and routes request  
3. Business logic processes data (CRUD operations)  
4. Query executed on MySQL database  
5. Result returned and formatted as JSON response  

***System Architecture (Text)***
- Flask acts as the application layer (stateless API)
- MySQL acts as the persistent data layer
- Docker ensures consistent runtime across environments
- Docker Compose manages service orchestration (app + DB)

## ⚙️ Tech Stack :

- 🐍 Python (Flask) — Backend web application
- 🐳 Docker — Containerization
- 🧩 Docker Compose — Multi-container orchestration
- 🗄️ MySQL 8.0 — Relational database
- 🔍 Postman — API testing
- ☁️ AWS EC2 (t3.micro) — Cloud deployment environment

## 🛡️ Resilience & Security :

***Failure Scenarios***
- MySQL container crash → data persists via Docker volumes  
- API container restart → stateless recovery without data loss  
- Invalid requests → handled with input validation and error responses  

***Security Considerations***
- Environment variables used for DB credentials (no hardcoding)  
- Isolated container network (internal communication only)  
- No direct external exposure of database service  

***Scalability & Performance Thinking***
- Flask app can be horizontally scaled (multiple containers)  
- Database is the bottleneck → requires optimization or managed DB for scale  
- Suitable for small to mid-scale workloads, not high concurrency systems  


## 🧪 Proof of Working :

All real execution proof is included without modification.

### 📂 Folder:
`results/`

- Here is some of them


### 1️⃣ Docker Containers Running :
![Docker Containers](result/one.jpeg)

### 2️⃣ Flask Backend Running on Port 5000 :
![Flask Running](result/two.jpeg)

### 3️⃣ POST Request Inserting Data :
![POST Request](result/three.jpeg)

### 4️⃣ GET Request Returning Stored Data :
![GET Request](result/four.jpeg)



***Contains screenshots showing:***

- Docker containers running
- Flask backend live on port 5000
- POST request inserting data
- GET request returning stored data
- MySQL persistence
- AWS EC2 instance running (Mumbai region)

These are real execution screenshots, not mockups.


## ⚙️ Engineering Philosophy :

***Trade-offs & Decisions***
- Chose simplicity (Flask + MySQL) over complex frameworks  
  → Faster development, easier debugging, and clear understanding of core backend flow  

- Used Docker Compose instead of Kubernetes  
  → Faster setup, minimal operational overhead, suitable for single-node architecture  

- Prioritized working system over premature optimization  
  → Focused on correctness and end-to-end functionality before scaling concerns  

***Explicit Limitations***
- No load balancing or auto-scaling  
- Single database instance (no replication)  
- Limited fault tolerance at large scale  
- Not production-grade for high traffic systems

This project focuses on demonstrating real backend execution, containerization, and persistence — not distributed system complexity.

## 🙌 Contributions Welcome!
GrowEasy is an open-source initiative, and we welcome contributions from developers, data scientists, cloud engineers, and e-commerce enthusiasts!

## 🔮 Future Improvements :

- Environment-based secret management
- Production WSGI server (Gunicorn)
- CI/CD pipeline
- Managed database (RDS)
- Basic authentication


This project reflects how I approach **real-world backend and DevOps problems**.
**If you can run it, test it, and explain it — you own it. 💪**

### 🛠️ How to Contribute

1. 🍴 Fork the repo
2. 📦 Create a new feature branch: `git checkout -b feature-name`
3. ✅ Make your changes and test them
4. 📬 Submit a pull request describing your enhancement

 🤝 Let's Build This Together!
Made with 💚 by **Manas Gantait**  

