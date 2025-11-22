# 🎯 Hands-On Walkthrough: Build Your First DevOps Project

Follow these steps EXACTLY. I'll explain what's happening at each step.

---

## 🎬 Step 1: Set Up Your Environment

### What We're Doing
Making sure you have the tools needed to run this project.

### Commands to Run

```bash
# Check if Docker is installed
docker --version

# Expected output: Docker version 20.10.x or higher
# If you see an error, install Docker Desktop from docker.com
```

```bash
# Check if Docker Compose is installed
docker-compose --version

# Expected output: docker-compose version 1.29.x or higher
```

### ✅ Checkpoint
- [ ] Docker is installed
- [ ] Docker Compose is installed
- [ ] Docker Desktop is running (if on Mac/Windows)

**What Just Happened?**
- We verified you have Docker, which is like having a "virtual machine" tool
- Docker lets us package and run applications consistently

---

## 🎬 Step 2: Explore the Project Structure

### What We're Doing
Understanding what files we have and what they do.

### Commands to Run

```bash
# See all files in the project
ls -la

# Or on Windows
dir
```

### Files You Should See

```
app.py              ← Our web application (Python code)
requirements.txt    ← List of Python libraries we need
Dockerfile         ← Instructions for building a container
docker-compose.yml ← Configuration for running multiple containers
README.md          ← Documentation
```

### ✅ Checkpoint
- [ ] You can see all the files
- [ ] You understand what each file is for

**What Just Happened?**
- We looked at the project structure
- Each file has a specific purpose in DevOps

---

## 🎬 Step 3: Understand the Application (app.py)

### What We're Doing
Looking at the actual code to understand what our app does.

### Commands to Run

```bash
# Open app.py in a text editor
# Or view it in terminal
cat app.py
```

### What to Look For

1. **Imports** (lines at top)
   - `from flask import Flask` - We're using Flask framework
   - `import os` - For environment variables

2. **Routes** (functions with @app.route)
   - `/` - Homepage
   - `/health` - Health check
   - `/api/info` - API endpoint

3. **Main section** (if __name__ == '__main__')
   - This starts the web server

### ✅ Checkpoint
- [ ] You've read through app.py
- [ ] You understand it's a web application
- [ ] You see the different routes/endpoints

**What Just Happened?**
- We examined the application code
- This is the "what" - what our application does

---

## 🎬 Step 4: Build Your First Docker Image

### What We're Doing
Creating a Docker image (like a template) from our application.

### Commands to Run

```bash
# Build the Docker image
docker build -t devops-learning-app .

# What you'll see:
# Step 1/8 : FROM python:3.11-slim
# Step 2/8 : WORKDIR /app
# ... (more steps)
# Successfully built abc123def456
# Successfully tagged devops-learning-app:latest
```

### What's Happening Behind the Scenes

1. Docker reads the `Dockerfile`
2. Starts with a base image (Python 3.11)
3. Installs our dependencies
4. Copies our code
5. Creates the final image

### Verify It Worked

```bash
# List all Docker images
docker images

# You should see: devops-learning-app
```

### ✅ Checkpoint
- [ ] Image built successfully
- [ ] You can see it in `docker images`

**What Just Happened?**
- We created a Docker image
- This image contains everything needed to run our app
- It's like creating a "snapshot" that works anywhere

---

## 🎬 Step 5: Run Your First Container

### What We're Doing
Starting a container (running instance) from our image.

### Commands to Run

```bash
# Run the container
docker run -d -p 5000:5000 --name my-first-container devops-learning-app

# -d = run in background (detached)
# -p 5000:5000 = map port 5000 (your computer) to port 5000 (container)
# --name = give it a name
```

### Verify It's Running

```bash
# Check running containers
docker ps

# You should see: my-first-container
```

### Test the Application

```bash
# Test the health endpoint
curl http://localhost:5000/health

# Or open in browser: http://localhost:5000
```

### ✅ Checkpoint
- [ ] Container is running (`docker ps` shows it)
- [ ] You can access http://localhost:5000
- [ ] Health check works

**What Just Happened?**
- We started a container from our image
- The application is now running
- We can access it through our web browser

---

## 🎬 Step 6: Explore Container Commands

### What We're Doing
Learning essential Docker commands for managing containers.

### Commands to Run

```bash
# See container logs (what the app is doing)
docker logs my-first-container

# See last 20 lines of logs
docker logs --tail 20 my-first-container

# Follow logs in real-time (press Ctrl+C to stop)
docker logs -f my-first-container
```

```bash
# See container resource usage (like Task Manager)
docker stats my-first-container
```

```bash
# Stop the container
docker stop my-first-container

# Verify it's stopped
docker ps

# Start it again
docker start my-first-container
```

```bash
# Remove the container (when you're done)
docker rm my-first-container

# Or stop and remove in one command
docker rm -f my-first-container
```

### ✅ Checkpoint
- [ ] You can view logs
- [ ] You can see resource usage
- [ ] You can stop/start containers
- [ ] You understand the difference between stop and rm

**What Just Happened?**
- We learned how to manage containers
- These are essential DevOps skills
- Logs help us debug problems
- Stats help us monitor performance

---

## 🎬 Step 7: Use Docker Compose

### What We're Doing
Using Docker Compose to run multiple containers together.

### Commands to Run

```bash
# First, stop and remove the container from Step 5
docker rm -f my-first-container

# Start everything with Docker Compose
docker-compose up -d

# What you'll see:
# Creating network "devops_prac1_devops-network" ... done
# Building web ...
# Starting devops-learning-app ... done
# Starting devops-nginx ... done
```

### What's Happening

1. Docker Compose reads `docker-compose.yml`
2. Creates a network for containers to communicate
3. Builds the web service (our Flask app)
4. Starts the nginx service (web server)
5. Connects them together

### Verify Everything is Running

```bash
# See all services
docker-compose ps

# You should see:
# - devops-learning-app (web service)
# - devops-nginx (nginx service)
```

### Test the Application

```bash
# Test through the app directly
curl http://localhost:5000/health

# Test through Nginx (reverse proxy)
curl http://localhost:80/health

# Or open in browser
open http://localhost:5000
```

### ✅ Checkpoint
- [ ] Both containers are running
- [ ] You can access the app
- [ ] Nginx is working as reverse proxy

**What Just Happened?**
- We used Docker Compose to orchestrate multiple containers
- This is how real applications work (multiple services together)
- Nginx acts as a reverse proxy (traffic director)

---

## 🎬 Step 8: View Logs and Monitor

### What We're Doing
Learning how to monitor and debug your application.

### Commands to Run

```bash
# View logs from all services
docker-compose logs

# View logs from just the web service
docker-compose logs web

# Follow logs in real-time
docker-compose logs -f

# View last 50 lines
docker-compose logs --tail 50
```

```bash
# Use our monitoring script
chmod +x scripts/monitor.sh
./scripts/monitor.sh

# This shows:
# - Container status
# - Resource usage
# - Health check
# - Recent logs
```

### ✅ Checkpoint
- [ ] You can view logs
- [ ] You understand what logs show
- [ ] Monitoring script works

**What Just Happened?**
- We learned about monitoring
- Logs help us see what's happening
- Monitoring helps us catch problems early

---

## 🎬 Step 9: Make a Change and Rebuild

### What We're Doing
Learning the development workflow - make changes and see them.

### Steps to Follow

1. **Edit app.py**
   ```python
   # Find this line (around line 50):
   APP_NAME = os.getenv('APP_NAME', 'DevOps Learning App')
   
   # Change it to:
   APP_NAME = os.getenv('APP_NAME', 'My First DevOps App!')
   ```

2. **Rebuild and restart**
   ```bash
   # Stop current containers
   docker-compose down
   
   # Rebuild and start
   docker-compose up -d --build
   ```

3. **See your change**
   ```bash
   # Visit http://localhost:5000
   # You should see "My First DevOps App!" instead
   ```

### ✅ Checkpoint
- [ ] You made a change to the code
- [ ] You rebuilt the containers
- [ ] You can see your change live

**What Just Happened?**
- We practiced the development workflow
- This is what DevOps engineers do daily
- Make changes → Build → Deploy → Verify

---

## 🎬 Step 10: Understand CI/CD (GitHub Actions)

### What We're Doing
Setting up automated testing and deployment.

### Steps to Follow

1. **Create a GitHub repository**
   - Go to github.com
   - Create a new repository
   - Don't initialize with README (we already have one)

2. **Push your code**
   ```bash
   # Initialize git (if not already done)
   git init
   
   # Add all files
   git add .
   
   # Commit
   git commit -m "My first DevOps project"
   
   # Add remote (replace YOUR_USERNAME and YOUR_REPO)
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   
   # Push
   git push -u origin main
   ```

3. **Watch the CI/CD pipeline run**
   - Go to your GitHub repository
   - Click "Actions" tab
   - You should see the workflow running
   - It will:
     - Run tests
     - Build Docker image
     - Check for security issues

### ✅ Checkpoint
- [ ] Code is on GitHub
- [ ] CI/CD pipeline ran
- [ ] All checks passed (green checkmarks)

**What Just Happened?**
- We set up automated CI/CD
- Now every time you push code, it automatically tests and builds
- This is a core DevOps practice

---

## 🎬 Step 11: Use Deployment Script

### What We're Doing
Learning about deployment automation.

### Commands to Run

```bash
# Make script executable
chmod +x scripts/deploy.sh

# Run deployment script
./scripts/deploy.sh v1.0.0 production

# What happens:
# 1. Builds Docker image
# 2. Tests it
# 3. Stops old container
# 4. Starts new container
# 5. Checks health
```

### ✅ Checkpoint
- [ ] Deployment script ran successfully
- [ ] New version is running
- [ ] Health check passed

**What Just Happened?**
- We automated deployment
- This script does what would take many manual steps
- Automation is key to DevOps

---

## 🎯 Summary: What You've Learned

### Concepts Mastered

1. ✅ **Web Applications** - Built a Flask app
2. ✅ **Containerization** - Created Docker images and containers
3. ✅ **Orchestration** - Used Docker Compose for multi-container apps
4. ✅ **CI/CD** - Set up automated testing and building
5. ✅ **Monitoring** - Learned to view logs and check health
6. ✅ **Deployment** - Automated the deployment process

### Skills Gained

- ✅ Docker commands (build, run, stop, logs)
- ✅ Docker Compose usage
- ✅ Understanding of DevOps workflow
- ✅ Basic monitoring and debugging
- ✅ CI/CD pipeline setup

### Next Steps

1. **Experiment More**
   - Add a database (PostgreSQL)
   - Add more endpoints
   - Try different configurations

2. **Learn More**
   - Kubernetes (container orchestration at scale)
   - Cloud platforms (AWS, GCP, Azure)
   - Infrastructure as Code (Terraform)
   - Advanced monitoring (Prometheus, Grafana)

3. **Build Your Own Project**
   - Create a simple app
   - Containerize it
   - Set up CI/CD
   - Deploy it

---

## 🎓 Congratulations!

You've completed your first DevOps project! 🎉

You now understand:
- How applications are built
- How containers work
- How to orchestrate multiple services
- How to automate testing and deployment
- How to monitor applications

**Keep practicing, keep learning, and keep building!** 🚀

---

## 🆘 Troubleshooting

### Problem: Port 5000 already in use
```bash
# Find what's using it
lsof -i :5000

# Kill it
kill -9 <PID>
```

### Problem: Docker daemon not running
- Start Docker Desktop (Mac/Windows)
- Or: `sudo systemctl start docker` (Linux)

### Problem: Permission denied on scripts
```bash
chmod +x scripts/*.sh
```

### Problem: Container won't start
```bash
# Check logs
docker-compose logs

# Check what's wrong
docker-compose up (without -d to see output)
```

---

**Remember: Every expert was once a beginner. You're doing great!** 💪

