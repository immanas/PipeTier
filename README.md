# 🚀 PipeTier — Containerized Backend with Persistent Storage

PipeTier is a **Dockerized Flask backend** connected to **MySQL**, built to demonstrate **real backend execution, container orchestration, and data persistence**, with verified testing and cloud hosting proof.

This project focuses on **working systems**, not slides or mock demos.


## 🧠 One-Line Truth
A real backend API that runs in Docker, stores data in MySQL, and is verified locally and on AWS EC2.


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


## 🧩 Real Problems PipeTier Solves

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


## 🏗️ System Architecture
![System Architecture](architecture.png)


---


## Why This Design?

- This project uses a simple and practical two-tier architecture to demonstrate real-world containerized deployment patterns.
- Docker Compose simplifies the setup of multiple services with a single command.
- Service-name based networking (mysql) reflects actual Docker container communication instead of using localhost.
- Persistent volumes ensure database data is not lost when containers restart.
- Flask provides a lightweight, readable backend suitable for learning and rapid development.

---

## 🔁 Request Lifecycle (How a Request Flows)

1️⃣ A client (Postman or browser) sends an HTTP request to the Flask API  
2️⃣ Docker maps the request from host port `5000` to the backend container  
3️⃣ Flask validates and parses the incoming JSON payload  
4️⃣ The backend connects to MySQL using Docker’s internal service name  
5️⃣ Data is written to or read from the MySQL database  
6️⃣ MySQL persists data using a Docker volume  
7️⃣ Flask formats the response and sends it back to the client  
8️⃣ Client receives a clear JSON response with status codes  

This flow ensures **clean separation of concerns** and predictable behavior.


## ⚠️ Failure Scenarios & Handling

- 🛑 **MySQL container not ready** → Backend retries connection before failing  
- 🔌 **Database container down** → API returns controlled error, not crash  
- 📦 **Docker container restart** → Data remains safe due to volume usage  
- ❌ **Invalid request payload** → API responds with proper validation error  
- 🔁 **Service restart** → Docker Compose restores dependencies automatically  

Failures are **expected, handled, and observable** — not ignored.




## 🔐 Security Considerations

- 🔑 Database credentials are isolated inside containers, not hardcoded in clients  
- 🌐 MySQL is **not exposed** to the host or internet  
- 📦 Internal Docker networking prevents accidental external access  
- 🧱 Clear separation between API layer and database layer  
- ⚠️ No unnecessary open ports (only backend is exposed)  

Security choices prioritize **least exposure over convenience**.



## 🚀 Scalability & Performance Thinking

- 📈 Stateless Flask backend allows horizontal scaling  
- 🧩 Backend and database can scale independently  
- 🐳 Docker Compose structure is migration-ready for ECS / Kubernetes  
- ⚡ Connection reuse and lightweight containers reduce overhead  
- 🌍 Architecture supports future load balancers without redesign  

Designed with **growth in mind**, even at MVP stage.



## ⚙️ Tech Stack

- 🐍 Python (Flask) — Backend web application
- 🐳 Docker — Containerization
- 🧩 Docker Compose — Multi-container orchestration
- 🗄️ MySQL 8.0 — Relational database
- 🔍 Postman — API testing
- ☁️ AWS EC2 (t3.micro) — Cloud deployment environment



## 🧪 Testing Strategy

- 🔍 API tested end-to-end using Postman (real HTTP calls)  
- 🧠 Manual testing validates real behavior, not mocks  
- 🐳 Docker logs used to observe runtime behavior  
- 🔄 Repeated insert + read cycles verify DB persistence  

Focus was on **confidence in behavior**, not just test coverage numbers.





## 🧪 Proof of Working

All real execution proof is included without modification.

### 📂 Folder:
`results/`

- Here is some of them


### 1️⃣ Docker Containers Running
![Docker Containers](result/one.jpeg)

### 2️⃣ Flask Backend Running on Port 5000
![Flask Running](result/two.jpeg)

### 3️⃣ POST Request Inserting Data
![POST Request](result/three.jpeg)

### 4️⃣ GET Request Returning Stored Data
![GET Request](result/four.jpeg)



Contains screenshots showing:

- Docker containers running
- Flask backend live on port 5000
- POST request inserting data
- GET request returning stored data
- MySQL persistence
- AWS EC2 instance running (Mumbai region)

These are real execution screenshots, not mockups.



## ☁️ AWS EC2 Hosting 

PipeTier was verified on **AWS EC2 (t3.micro)** to demonstrate:

- Instance creation
- Public IP & DNS usage
- SSH connectivity
- Backend readiness for hosting

This confirms hands-on cloud fundamentals, not theory.



## ⚖️ Trade-offs & Decisions

- Used Flask dev server instead of Gunicorn (simplicity)
- Used Dockerized MySQL instead of RDS (learning focus)
- No authentication layer (out of scope)
- No frontend (backend-only proof)

All choices were intentional and documented.




## 🚫 Explicit Limitations

- ❗ No authentication or authorization implemented  
- ❗ Not production-hardened (dev Flask server)  
- ❗ No automated CI/CD pipeline yet  
- ❗ No monitoring or alerting stack  

These were **conscious scope decisions**, not oversights.



## 🔮 Future Improvements

- Environment-based secret management
- Production WSGI server (Gunicorn)
- CI/CD pipeline
- Managed database (RDS)
- Basic authentication



## 👨‍💻 What This Project Demonstrates About Me

- 🧠 I think in **systems**, not just files  
- 🐳 I understand **containerized application design**  
- 🧱 I design with **failure awareness**, not happy paths  
- 🔍 I value **clarity, separation, and observability**  
- 📐 I build projects that resemble **real production workflows**, not demos  

This project reflects how I approach **real-world backend and DevOps problems**.



## 🏁 Final Note

PipeTier is not a tutorial copy.  
It is a working backend system, tested locally and verified on AWS, with clear proof.

**If you can run it, test it, and explain it — you own it. 💪**

### 🛠️ How to Contribute

1. 🍴 Fork the repo
2. 📦 Create a new feature branch: `git checkout -b feature-name`
3. ✅ Make your changes and test them
4. 📬 Submit a pull request describing your enhancement

 🤝 Let's Build This Together!
Made with 💚 by **Manas Gantait**  

