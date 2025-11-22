# 🎓 Advanced DevOps Tutorial - Step by Step

Let's dive deeper into DevOps concepts with hands-on exercises!

---

## 📚 Step 1: Understanding Multi-Stage Builds

### What is a Multi-Stage Build?

Your Dockerfile has **TWO stages**:

**Stage 1: Builder** (lines 22-36)
- Installs all dependencies
- Can be large (has build tools)
- Creates packages

**Stage 2: Production** (lines 44-95)
- Only copies what's needed
- Smaller final image
- No build tools

### Why Use Multi-Stage?

**Without multi-stage:**
- Final image: ~500MB (includes build tools)

**With multi-stage:**
- Final image: ~221MB (only runtime)
- **50% smaller!**

### Let's See the Difference

```bash
# Check your image size
docker images devops_prac1-web
```

---

## 📚 Step 2: Understanding Docker Layers

Docker builds images in **layers**. Each instruction creates a layer.

### Your Dockerfile Layers:

1. **FROM python:3.11-slim** → Base layer
2. **WORKDIR /app** → New layer
3. **COPY requirements.txt** → New layer
4. **RUN pip install** → New layer (this is BIG)
5. **COPY app.py** → New layer (small)

### Layer Caching

Docker **caches** layers. If a layer doesn't change, Docker reuses it!

**Example:**
- You change `app.py` → Only rebuilds that layer
- You don't change `requirements.txt` → Reuses cached layer
- **Result:** Faster builds!

### Let's Test Layer Caching

```bash
# First build (slow - builds everything)
docker build -t test-app .

# Change app.py slightly
# Second build (fast - reuses cached layers!)
docker build -t test-app .
```

---

## 📚 Step 3: Understanding Volumes

### What are Volumes?

Volumes let you **persist data** outside containers.

**Problem:** When container stops, data inside is lost!
**Solution:** Volumes store data on your host machine.

### Types of Volumes:

1. **Named Volumes** - Managed by Docker
2. **Bind Mounts** - Map to host directory
3. **tmpfs** - In-memory (temporary)

### Your docker-compose.yml Has a Volume!

Look at line 52-53:
```yaml
volumes:
  - ./app.py:/app/app.py:ro
```

**What this does:**
- Maps `./app.py` (your file) to `/app/app.py` (container)
- `:ro` = Read-only (container can't modify it)
- Changes to your file reflect immediately!

### Let's Test Volumes

```bash
# Edit app.py on your computer
# The change appears in the container immediately!
# (No rebuild needed for development)
```

---

## 📚 Step 4: Environment Variables Deep Dive

### What are Environment Variables?

Environment variables are **configuration** that can change without modifying code.

### Your docker-compose.yml Sets Environment Variables:

```yaml
environment:
  - APP_NAME=My First DevOps App!
  - APP_VERSION=1.0.0
  - ENVIRONMENT=production
```

### Why Use Environment Variables?

1. **Different environments:**
   - Development: `ENVIRONMENT=development`
   - Production: `ENVIRONMENT=production`

2. **Secrets:**
   - API keys
   - Database passwords
   - (Never hardcode these!)

3. **Configuration:**
   - Port numbers
   - Feature flags
   - App settings

### Let's Test Environment Variables

```bash
# Run with different environment
docker run -e APP_NAME="Test App" -p 5002:5000 devops_prac1-web

# Check the API
curl http://localhost:5002/api/info
```

---

## 📚 Step 5: Understanding Health Checks

### What is a Health Check?

A health check tells Docker if your container is **healthy** (working correctly).

### Your Dockerfile Has a Health Check:

```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')"
```

**What this does:**
- Every 30 seconds, checks `/health` endpoint
- If it fails 3 times → Container marked unhealthy
- Docker can restart unhealthy containers

### Let's Check Container Health

```bash
# See health status
docker ps

# Check health check logs
docker inspect devops-learning-app | grep -A 10 Health
```

---

## 📚 Step 6: Understanding Gunicorn

### What is Gunicorn?

**Gunicorn** = Production web server for Python apps.

**Why not Flask's dev server?**
- Dev server: Single-threaded, not secure
- Gunicorn: Multi-worker, production-ready

### Your Dockerfile Uses Gunicorn:

```dockerfile
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]
```

**What this means:**
- `--bind 0.0.0.0:5000` = Listen on all interfaces, port 5000
- `--workers 2` = Run 2 worker processes
- `app:app` = Import app from app.py

### Why 2 Workers?

- **1 worker** = Can handle 1 request at a time
- **2 workers** = Can handle 2 requests simultaneously
- **More workers** = More concurrent requests (but more memory)

---

## 📚 Step 7: Understanding Networks (Deep Dive)

### Network Types:

1. **Bridge** (default) - Containers can communicate
2. **Host** - Uses host's network directly
3. **None** - No networking

### Your Network:

```yaml
networks:
  devops-network:
    driver: bridge
```

**Bridge network:**
- Containers get IP addresses
- Can communicate by name or IP
- Isolated from host network

### Container Communication:

**By name:**
```nginx
server web:5000;  # Nginx finds "web" service
```

**By IP:**
```bash
# Containers have IPs like 172.18.0.2
ping 172.18.0.2
```

---

## 📚 Step 8: Understanding CI/CD Pipeline

### What is CI/CD?

**CI = Continuous Integration**
- Every code change is automatically tested
- Catches bugs early

**CD = Continuous Deployment**
- Automatically deploy when tests pass
- Faster releases

### Your CI/CD Pipeline (`.github/workflows/ci-cd.yml`):

**3 Jobs:**

1. **Test Job:**
   - Runs tests
   - Checks code quality
   - Must pass before build

2. **Build Job:**
   - Builds Docker image
   - Tests the image
   - Only runs if test passes

3. **Security Job:**
   - Scans for vulnerabilities
   - Checks dependencies
   - Reports security issues

### Pipeline Flow:

```
Code Push → Test → Build → Security Scan
    ↓         ↓      ↓          ↓
  GitHub   Run    Create    Check for
           Tests  Image     Vulnerabilities
```

---

## 🎯 Hands-On Exercises

### Exercise 1: Test Layer Caching

```bash
# Build image (note the time)
time docker build -t test-cache .

# Make a small change to app.py
# Rebuild (should be faster - uses cache!)
time docker build -t test-cache .
```

### Exercise 2: Test Environment Variables

```bash
# Run with custom environment
docker run -d -p 5002:5000 \
  -e APP_NAME="Custom Name" \
  -e ENVIRONMENT="staging" \
  devops_prac1-web

# Check it
curl http://localhost:5002/api/info
```

### Exercise 3: Explore Container Internals

```bash
# Go inside container
docker exec -it devops-learning-app /bin/bash

# Inside container:
ls -la
cat app.py
env  # See environment variables
ps aux  # See running processes
exit
```

### Exercise 4: Test Health Check

```bash
# Check health status
docker ps

# Manually test health endpoint
curl http://localhost:5001/health

# See health check history
docker inspect devops-learning-app | grep -A 20 Health
```

### Exercise 5: Test Network Communication

```bash
# From nginx container, ping web container
docker exec devops-nginx ping -c 3 devops-learning-app

# From nginx, access web API
docker exec devops-nginx wget -qO- http://devops-learning-app:5000/api/info
```

---

## 🎓 Key Concepts Summary

| Concept | What It Is | Why It Matters |
|---------|-----------|----------------|
| **Multi-Stage Builds** | Build in stages, copy only needed | Smaller images |
| **Layer Caching** | Docker reuses unchanged layers | Faster builds |
| **Volumes** | Persistent storage outside containers | Data survives restarts |
| **Environment Variables** | Configuration outside code | Different environments |
| **Health Checks** | Automatic container health monitoring | Know when app is broken |
| **Gunicorn** | Production web server | Better performance, security |
| **Networks** | Container communication | Services can talk to each other |
| **CI/CD** | Automated testing and deployment | Faster, safer releases |

---

## 🚀 Next Advanced Topics

1. **Add a Database** - Learn persistent storage
2. **Kubernetes** - Container orchestration
3. **Monitoring** - Prometheus, Grafana
4. **Logging** - Centralized log management
5. **Secrets Management** - Secure configuration
6. **Scaling** - Handle more traffic

---

**Keep learning and practicing!** 🎉

