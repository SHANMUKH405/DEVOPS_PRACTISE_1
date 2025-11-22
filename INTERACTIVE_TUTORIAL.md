# 🎓 Interactive Step-by-Step Tutorial

Follow along with me! I'll guide you through each step and explain what's happening.

---

## 🎯 Step 1: Check What's Running

Let's see what containers are currently running.

**Run this command:**
```bash
docker-compose ps
```

**What this does:**
- `docker-compose` = Tool for managing multiple containers
- `ps` = "Process Status" - shows what's running
- This shows all containers defined in docker-compose.yml

**What you should see:**
- Two containers: `devops-learning-app` and `devops-nginx`
- Their status (should be "Up")
- Port mappings

**What you're learning:** How to check if your services are running

---

## 🎯 Step 2: View Your Application

Let's see your application in action!

**Run this command:**
```bash
open http://localhost:5001
```

**What this does:**
- `open` = Opens a URL in your default browser (Mac command)
- Opens your Flask application
- You should see a beautiful webpage with app information

**What you should see:**
- A webpage showing "DevOps Learning App"
- Version, environment, server time
- List of available endpoints

**What you're learning:** How to access your containerized application

---

## 🎯 Step 3: Test the Health Check Endpoint

Let's test if your app is healthy using the command line.

**Run this command:**
```bash
curl http://localhost:5001/health
```

**What this does:**
- `curl` = Command-line tool to make HTTP requests
- Sends a GET request to `/health` endpoint
- Returns JSON data showing app health

**What you should see:**
```json
{"status":"healthy","timestamp":"2025-11-21T..."}
```

**What you're learning:** 
- How to test API endpoints
- Health checks (important for monitoring!)
- JSON responses

---

## 🎯 Step 4: Test Another Endpoint

Let's get more information about your app.

**Run this command:**
```bash
curl http://localhost:5001/api/info
```

**What this does:**
- Calls the `/api/info` endpoint
- Returns detailed information about your application
- Shows app name, version, environment, hostname

**What you should see:**
```json
{
  "app_name": "DevOps Learning App",
  "version": "1.0.0",
  "environment": "production",
  ...
}
```

**What you're learning:** REST API endpoints, JSON data format

---

## 🎯 Step 5: View Container Logs

Let's see what your application is doing behind the scenes.

**Run this command:**
```bash
docker-compose logs web
```

**What this does:**
- `logs` = Shows log output from containers
- `web` = Only show logs from the "web" service (your Flask app)
- Shows all the print statements and requests

**What you should see:**
- Log entries showing when the app started
- HTTP requests being processed
- Any errors or warnings

**What you're learning:** 
- How to debug applications
- Where to look when something goes wrong
- Logging is crucial for DevOps!

**Try this too:**
```bash
docker-compose logs -f web
```
- `-f` = "follow" - keeps showing new logs in real-time
- Press `Ctrl+C` to stop watching

---

## 🎯 Step 6: See Container Resource Usage

Let's check how much CPU and memory your containers are using.

**Run this command:**
```bash
docker stats devops-learning-app
```

**What this does:**
- `stats` = Shows resource usage statistics
- Shows CPU %, memory usage, network I/O
- Updates in real-time (like Task Manager)

**What you should see:**
- A table showing CPU%, memory usage, network stats
- Updates every few seconds

**What you're learning:**
- Container resource monitoring
- How to check if your app needs more resources
- Performance monitoring basics

**Press `Ctrl+C` to stop watching**

---

## 🎯 Step 7: Explore the Application Code

Let's look at the actual code that's running.

**Open the file:**
```bash
open app.py
```
Or open it in your code editor.

**What to look for:**
1. **Imports** (top of file)
   - `from flask import Flask` - We're using Flask framework
   - `import os` - For environment variables

2. **Routes** (functions with `@app.route`)
   - `@app.route('/')` - Homepage
   - `@app.route('/health')` - Health check
   - `@app.route('/api/info')` - API endpoint

3. **Read the comments** - They explain everything!

**What you're learning:**
- How web applications are structured
- What routes/endpoints are
- How Flask works

---

## 🎯 Step 8: Make Your First Change

Let's modify the code and see it update!

**Step 8a: Edit app.py**

Find this line (around line 50):
```python
APP_NAME = os.getenv('APP_NAME', 'DevOps Learning App')
```

Change it to:
```python
APP_NAME = os.getenv('APP_NAME', 'My First DevOps App!')
```

**What this does:**
- Changes the default app name
- When you rebuild, the new name will appear

**Step 8b: Rebuild the Container**

**Run this command:**
```bash
docker-compose down
```

**What this does:**
- Stops and removes all containers
- Cleans up the current deployment

**Then run:**
```bash
docker-compose up -d --build
```

**What this does:**
- `up -d` = Start containers in background
- `--build` = Rebuild images before starting
- Creates new containers with your updated code

**Step 8c: See Your Change**

**Run this command:**
```bash
open http://localhost:5001
```

**What you should see:**
- Your new app name: "My First DevOps App!"

**What you're learning:**
- Development workflow
- How to update containerized applications
- The build → deploy cycle

---

## 🎯 Step 9: Understand Docker Images

Let's see what Docker images you have.

**Run this command:**
```bash
docker images
```

**What this does:**
- Lists all Docker images on your system
- Shows image name, tag, size, when created

**What you should see:**
- `devops_prac1-web` - Your application image
- `nginx:alpine` - The Nginx image
- `python:3.11-slim` - Base Python image (used to build yours)

**What you're learning:**
- Images vs containers (images are templates, containers are running instances)
- How images are stored
- Image sizes

---

## 🎯 Step 10: See All Containers (Including Stopped)

Let's see all containers, not just running ones.

**Run this command:**
```bash
docker ps -a
```

**What this does:**
- `ps` = List containers
- `-a` = "all" - includes stopped containers
- Shows full history

**What you should see:**
- Running containers (STATUS: Up)
- Stopped containers (STATUS: Exited)
- Container IDs, names, ports

**What you're learning:**
- Container lifecycle
- Difference between running and stopped
- Container management

---

## 🎯 Step 11: Execute Commands Inside Container

Let's go inside the container and explore!

**Run this command:**
```bash
docker exec -it devops-learning-app /bin/bash
```

**What this does:**
- `exec` = Execute a command in running container
- `-it` = Interactive terminal
- `/bin/bash` = Start a bash shell
- You're now INSIDE the container!

**What you should see:**
- Your prompt changes (you're inside the container)
- You can run commands inside the container

**Try these commands inside the container:**
```bash
# See where you are
pwd

# List files
ls -la

# See the Python file
cat app.py

# Check Python version
python --version

# Exit the container
exit
```

**What you're learning:**
- Containers are like mini Linux systems
- You can interact with them
- Useful for debugging

---

## 🎯 Step 12: Understand Docker Compose Services

Let's see what services are defined.

**Open the file:**
```bash
open docker-compose.yml
```

**What to look for:**

1. **Services section:**
   - `web:` - Your Flask application
   - `nginx:` - Web server/reverse proxy

2. **For each service:**
   - `build:` - How to build the image
   - `ports:` - Port mappings
   - `environment:` - Environment variables
   - `networks:` - Which network it's on

3. **Networks section:**
   - `devops-network` - Network connecting services

**What you're learning:**
- How multi-container apps are defined
- Service dependencies
- Networking between containers

---

## 🎯 Step 13: Test the Deployment Script

Let's use the automated deployment script.

**First, stop current containers:**
```bash
docker-compose down
```

**Then run the deployment script:**
```bash
./scripts/deploy.sh v1.0.0 production
```

**What this does:**
- Builds the Docker image
- Tests it
- Stops old container
- Starts new container
- Checks health

**Watch what happens:**
- You'll see each step execute
- Build process
- Health check at the end

**What you're learning:**
- Deployment automation
- Scripts make repetitive tasks easy
- Best practices for deployment

---

## 🎯 Step 14: Use the Monitoring Script

Let's monitor your application.

**Run this command:**
```bash
./scripts/monitor.sh
```

**What this does:**
- Checks if container is running
- Shows resource usage
- Tests health endpoint
- Shows recent logs

**What you should see:**
- Container status
- CPU and memory stats
- Health check result
- Recent log entries

**What you're learning:**
- Application monitoring
- Health checks
- Resource monitoring
- Operations basics

---

## 🎯 Step 15: Add a New Endpoint

Let's add a new feature to your app!

**Step 15a: Edit app.py**

Add this code after the `status()` function (around line 120):

```python
@app.route('/api/hello')
def hello():
    """New endpoint that says hello"""
    return jsonify({
        'message': 'Hello from DevOps!',
        'timestamp': datetime.datetime.now().isoformat(),
        'learning': 'I just added a new endpoint!'
    })
```

**What this does:**
- Creates a new route `/api/hello`
- Returns a JSON response
- Shows you can add new features

**Step 15b: Rebuild and Test**

```bash
docker-compose down
docker-compose up -d --build
```

**Step 15c: Test Your New Endpoint**

```bash
curl http://localhost:5001/api/hello
```

**What you should see:**
```json
{
  "message": "Hello from DevOps!",
  "timestamp": "...",
  "learning": "I just added a new endpoint!"
}
```

**What you're learning:**
- Adding new features
- API development
- Testing endpoints
- Full development cycle

---

## 🎯 Step 16: Understand the Dockerfile

Let's see how the container is built.

**Open the file:**
```bash
open Dockerfile
```

**What to understand:**

1. **FROM python:3.11-slim**
   - Starts with a base Python image
   - Like starting with a pre-made foundation

2. **WORKDIR /app**
   - Sets working directory inside container
   - All commands run from here

3. **COPY requirements.txt**
   - Copies dependency list
   - Then installs them

4. **COPY app.py**
   - Copies your application code

5. **EXPOSE 5000**
   - Documents that app uses port 5000

6. **CMD ["gunicorn", ...]**
   - Command to run when container starts
   - Gunicorn is a production web server

**What you're learning:**
- How containers are built
- Multi-stage builds (optimization)
- Container configuration

---

## 🎯 Step 17: View Network Configuration

Let's see how containers communicate.

**Run this command:**
```bash
docker network ls
```

**What this does:**
- Lists all Docker networks
- Shows network names and drivers

**Then inspect your network:**
```bash
docker network inspect devops_prac1_devops-network
```

**What this does:**
- Shows detailed network information
- Lists containers connected to it
- Shows IP addresses

**What you should see:**
- Your containers listed
- Their IP addresses
- Network configuration

**What you're learning:**
- Container networking
- How services communicate
- Network isolation

---

## 🎯 Step 18: Clean Up

Let's learn how to clean up Docker resources.

**Stop and remove containers:**
```bash
docker-compose down
```

**Remove unused images:**
```bash
docker image prune
```

**What this does:**
- Removes images not used by any container
- Frees up disk space

**See what would be removed (dry run):**
```bash
docker system df
```

**What this does:**
- Shows disk usage by Docker
- Images, containers, volumes, etc.

**What you're learning:**
- Resource management
- Cleanup commands
- Disk space management

---

## 🎯 Step 19: Restart Everything

Let's start fresh!

**Run this command:**
```bash
docker-compose up -d
```

**Verify it's running:**
```bash
docker-compose ps
```

**Test it:**
```bash
curl http://localhost:5001/health
```

**What you're learning:**
- Starting services
- Verification
- Basic operations

---

## 🎯 Step 20: Summary - What You Learned

Let's review what you've accomplished!

**You've learned:**
1. ✅ How to check running containers
2. ✅ How to access your application
3. ✅ How to test API endpoints
4. ✅ How to view logs
5. ✅ How to monitor resources
6. ✅ How to read application code
7. ✅ How to make changes and rebuild
8. ✅ How Docker images work
9. ✅ How to explore inside containers
10. ✅ How Docker Compose works
11. ✅ How to use deployment scripts
12. ✅ How to monitor applications
13. ✅ How to add new features
14. ✅ How Dockerfiles work
15. ✅ How container networking works
16. ✅ How to clean up resources

**You've practiced:**
- Docker commands
- Container management
- Application development
- Deployment workflows
- Monitoring and debugging

---

## 🎉 Congratulations!

You've completed the interactive tutorial! You now understand:
- How containers work
- How to manage them
- How to develop and deploy applications
- Basic DevOps workflows

**Next steps:**
- Read BEGINNER_GUIDE.md for deeper explanations
- Read STEP_BY_STEP_TUTORIAL.md for more details
- Experiment on your own!
- Build your own project

**Keep learning and practicing!** 🚀

