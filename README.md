# 🚀 DevOps Learning Project - Complete Beginner's Guide

Welcome to your first DevOps project! This is designed for **complete beginners** who want to learn DevOps concepts hands-on.

## 📚 What is This Project?

This project teaches you DevOps by building a real web application. You'll learn:
- How to build web applications
- How to use Docker (containerization)
- How to orchestrate multiple services
- How to automate testing and deployment (CI/CD)
- How to monitor applications

**No prior DevOps experience needed!** We explain everything step by step.

---

## ⚡ Quick Start (5 Minutes)

```bash
# 1. Make sure Docker is running
docker --version

# 2. Start everything
docker-compose up -d

# 3. Open your browser
open http://localhost:5000
```

That's it! Your DevOps learning environment is running! 🎉

---

## 📖 Learning Path

### For Complete Beginners

**Start here:**
1. 📘 **[BEGINNER_GUIDE.md](BEGINNER_GUIDE.md)** - Complete explanation of all concepts
2. 🎓 **[STEP_BY_STEP_TUTORIAL.md](STEP_BY_STEP_TUTORIAL.md)** - Detailed tutorial with explanations
3. 🎯 **[HANDS_ON_WALKTHROUGH.md](HANDS_ON_WALKTHROUGH.md)** - Follow-along guide with commands

**Then:**
- Read the code files (they have detailed comments)
- Experiment and make changes
- Try the exercises in the guides

### Learning Order

1. **Week 1: Basics**
   - Understand the Flask application (`app.py`)
   - Learn basic Docker commands
   - Run containers

2. **Week 2: Docker Deep Dive**
   - Understand Dockerfiles
   - Learn about images vs containers
   - Use Docker Compose

3. **Week 3: Automation**
   - Set up CI/CD with GitHub Actions
   - Understand pipelines
   - Automate deployments

4. **Week 4: Advanced**
   - Add monitoring
   - Learn about scaling
   - Explore cloud platforms

---

## 📁 Project Structure

```
Devops_Prac1/
├── app.py                      # Flask web application (with detailed comments!)
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Container build instructions (with explanations!)
├── docker-compose.yml          # Multi-container setup (fully commented!)
├── nginx.conf                  # Reverse proxy configuration
├── Makefile                    # Automation commands
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # CI/CD pipeline
├── scripts/
│   ├── deploy.sh              # Deployment automation
│   └── monitor.sh             # Monitoring script
├── README.md                   # This file
├── BEGINNER_GUIDE.md          # Complete beginner's guide
├── STEP_BY_STEP_TUTORIAL.md   # Detailed tutorial
└── HANDS_ON_WALKTHROUGH.md    # Hands-on walkthrough
```

---

## 🎓 What You'll Learn

### 1. Web Application Development
- **File:** `app.py`
- **Concepts:** Flask, REST APIs, routes, health checks
- **Why:** You need an application to deploy!

### 2. Containerization with Docker
- **File:** `Dockerfile`
- **Concepts:** Images, containers, multi-stage builds
- **Why:** Package your app so it works everywhere

### 3. Container Orchestration
- **File:** `docker-compose.yml`
- **Concepts:** Services, networks, dependencies
- **Why:** Real apps need multiple services working together

### 4. CI/CD Pipelines
- **File:** `.github/workflows/ci-cd.yml`
- **Concepts:** Continuous Integration, automated testing, deployment
- **Why:** Automate testing and deployment for faster, safer releases

### 5. Monitoring & Operations
- **Files:** `scripts/monitor.sh`, health checks
- **Concepts:** Logs, health checks, resource monitoring
- **Why:** Know when things break and fix them fast

---

## 🚀 Getting Started

### Prerequisites

- **Docker Desktop** - [Download here](https://www.docker.com/products/docker-desktop)
- **Git** (optional, for CI/CD) - Usually pre-installed
- **Text Editor** - VS Code, Sublime, or any editor

### Step 1: Clone or Download

```bash
# If using Git
git clone <your-repo-url>
cd Devops_Prac1

# Or just download and extract the files
```

### Step 2: Start the Application

```bash
# Start everything with Docker Compose
docker-compose up -d

# Check it's running
docker-compose ps

# View logs
docker-compose logs -f
```

### Step 3: Access the Application

- **Main app:** http://localhost:5000
- **Through Nginx:** http://localhost:80
- **Health check:** http://localhost:5000/health
- **API info:** http://localhost:5000/api/info

### Step 4: Stop When Done

```bash
docker-compose down
```

---

## 📚 Available Commands

### Using Make (Easier)

```bash
make help          # Show all commands
make compose-up    # Start services
make compose-down  # Stop services
make logs          # View logs
make docker-build  # Build Docker image
```

### Using Docker Directly

```bash
# Build image
docker build -t devops-learning-app .

# Run container
docker run -p 5000:5000 devops-learning-app

# View running containers
docker ps

# View logs
docker logs <container-name>

# Stop container
docker stop <container-name>
```

### Using Docker Compose

```bash
# Start all services
docker-compose up -d

# Stop all services
docker-compose down

# View logs
docker-compose logs -f

# Rebuild and restart
docker-compose up -d --build
```

---

## 🎯 Application Endpoints

| Endpoint | Description | Example |
|----------|-------------|---------|
| `GET /` | Homepage | http://localhost:5000/ |
| `GET /health` | Health check | http://localhost:5000/health |
| `GET /api/info` | App information (JSON) | http://localhost:5000/api/info |
| `GET /api/status` | Status information (JSON) | http://localhost:5000/api/status |

---

## 💡 Key Concepts Explained

### What is DevOps?

**DevOps** = Development + Operations

It's about:
- **Automation** - Make repetitive tasks automatic
- **Collaboration** - Developers and operations work together
- **Continuous Improvement** - Always getting better
- **Infrastructure as Code** - Define infrastructure in files

### What is Docker?

**Docker** packages your application with everything it needs:
- Your code
- Dependencies (libraries)
- Runtime (Python)
- Configuration

**Result:** Works the same on your laptop, your friend's computer, and production servers!

### What is CI/CD?

**CI (Continuous Integration):**
- Every code change is automatically tested
- Catch bugs early
- Ensure code quality

**CD (Continuous Deployment):**
- Automatically deploy when tests pass
- No manual steps
- Faster releases

### What is Monitoring?

**Monitoring** = Watching your application to ensure it's working:
- Is it running?
- Is it healthy?
- How much resources is it using?
- Any errors?

---

## 🎓 Learning Resources

### In This Project

1. **BEGINNER_GUIDE.md** - Complete explanations of all concepts
2. **STEP_BY_STEP_TUTORIAL.md** - Detailed tutorial
3. **HANDS_ON_WALKTHROUGH.md** - Follow-along guide
4. **Code comments** - Every file has detailed explanations

### External Resources

- [Docker Documentation](https://docs.docker.com)
- [Flask Documentation](https://flask.palletsprojects.com)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [DevOps Roadmap](https://roadmap.sh/devops)

---

## 🐛 Troubleshooting

### Port Already in Use

```bash
# Find what's using port 5000
lsof -i :5000

# Kill it
kill -9 <PID>
```

### Docker Not Running

- **Mac/Windows:** Start Docker Desktop
- **Linux:** `sudo systemctl start docker`

### Permission Denied

```bash
# Make scripts executable
chmod +x scripts/*.sh
```

### Container Won't Start

```bash
# Check logs
docker-compose logs

# Run without -d to see output
docker-compose up
```

---

## 🎯 Practice Exercises

### Exercise 1: Modify the App
1. Edit `app.py` - change the homepage message
2. Rebuild: `docker-compose up -d --build`
3. See your changes!

### Exercise 2: Add a New Endpoint
1. Add a new route in `app.py`:
   ```python
   @app.route('/hello')
   def hello():
       return "Hello from DevOps!"
   ```
2. Rebuild and test

### Exercise 3: Environment Variables
1. Run with custom name:
   ```bash
   docker run -e APP_NAME="My Cool App" -p 5000:5000 devops-learning-app
   ```
2. See it change!

---

## 🚀 Next Steps

After mastering this project:

1. **Add a Database** - Learn about persistent storage
2. **Learn Kubernetes** - Container orchestration at scale
3. **Cloud Platforms** - Deploy to AWS, GCP, or Azure
4. **Infrastructure as Code** - Learn Terraform
5. **Advanced Monitoring** - Prometheus, Grafana
6. **Microservices** - Build distributed applications

---

## 📝 Notes

- This is a **learning project** - not production-ready
- Security practices are simplified for learning
- Always review code before deploying to production
- **Practice makes perfect** - experiment and break things!

---

## 🤝 Contributing

This is a learning project. Feel free to:
- Add new features
- Improve documentation
- Add more DevOps tools
- Share your learnings

---

## 📄 License

This project is for educational purposes.

---

## 🎉 Congratulations!

You're on your way to becoming a DevOps engineer! 

**Remember:**
- Every expert was once a beginner
- Take it one step at a time
- Experiment and have fun
- Keep learning!

**Start with [BEGINNER_GUIDE.md](BEGINNER_GUIDE.md) and happy learning!** 🚀
