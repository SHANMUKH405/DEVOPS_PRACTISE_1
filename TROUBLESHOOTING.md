# 🆘 Troubleshooting Guide

Common issues and how to fix them.

---

## ❌ Error: "Cannot connect to the Docker daemon"

### Problem
```
unable to get image 'nginx:alpine': Cannot connect to the Docker daemon at 
unix:///Users/shannu405/.docker/run/docker.sock. Is the docker daemon running?
```

### Solution

**Docker Desktop is not running!** You need to start it first.

#### On Mac:
1. **Open Docker Desktop**
   - Press `Cmd + Space` (Spotlight)
   - Type "Docker"
   - Click "Docker Desktop" to open it
   
2. **Wait for Docker to start**
   - Look for the Docker whale icon in your menu bar (top right)
   - Wait until it shows "Docker Desktop is running"
   - This usually takes 10-30 seconds

3. **Verify it's running**
   ```bash
   docker ps
   ```
   - If you see a table (even if empty), Docker is running! ✅
   - If you get an error, Docker is still starting (wait a bit more)

#### On Windows:
1. Open Docker Desktop from Start Menu
2. Wait for it to start (whale icon in system tray)
3. Verify with `docker ps`

#### On Linux:
```bash
sudo systemctl start docker
sudo systemctl status docker
```

### After Starting Docker Desktop

Once Docker Desktop is running, try again:
```bash
docker-compose up -d
```

---

## ⚠️ Warning: "the attribute `version` is obsolete"

### Problem
```
WARN[0000] /Users/shannu405/Devops_Prac1/docker-compose.yml: the attribute 
`version` is obsolete, it will be ignored
```

### Solution

This is just a warning (not an error). The `version` field is no longer needed in newer Docker Compose versions. 

**Already fixed!** The `version` line has been removed from `docker-compose.yml`.

If you still see this warning, make sure you're using the latest version of the file.

---

## ❌ Error: "Port already in use"

### Problem
```
Error: bind: address already in use
```

### Solution

Something else is using port 5000 or 80.

**Find what's using the port:**
```bash
# For port 5000
lsof -i :5000

# For port 80 (requires sudo on Mac)
sudo lsof -i :80
```

**Kill the process:**
```bash
# Replace <PID> with the number from the lsof output
kill -9 <PID>
```

**Or change the port in docker-compose.yml:**
```yaml
ports:
  - "5001:5000"  # Use 5001 instead of 5000
```

---

## ❌ Error: "Permission denied"

### Problem
```
bash: ./scripts/deploy.sh: Permission denied
```

### Solution

Make the script executable:
```bash
chmod +x scripts/deploy.sh
chmod +x scripts/monitor.sh

# Or make all scripts executable
chmod +x scripts/*.sh
```

---

## ❌ Error: "No such file or directory"

### Problem
```
docker-compose: command not found
```

### Solution

**On Mac/Windows:**
- Docker Compose comes with Docker Desktop
- Make sure Docker Desktop is installed and running

**On Linux:**
```bash
# Install Docker Compose
sudo apt-get update
sudo apt-get install docker-compose-plugin

# Or use the standalone version
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

---

## ❌ Error: Container keeps restarting

### Problem
Container starts but immediately stops and restarts in a loop.

### Solution

**Check the logs:**
```bash
docker-compose logs web
# or
docker logs devops-learning-app
```

**Common causes:**
1. **Application error** - Check the logs for Python errors
2. **Port conflict** - Another service is using the port
3. **Missing dependencies** - Check if requirements.txt is correct

**Debug mode:**
```bash
# Run without -d to see output
docker-compose up

# Or run container interactively
docker run -it devops-learning-app /bin/bash
```

---

## ❌ Error: "Cannot find Dockerfile"

### Problem
```
ERROR: Cannot locate Dockerfile
```

### Solution

Make sure you're in the correct directory:
```bash
# Check current directory
pwd

# Should show: /Users/shannu405/Devops_Prac1

# If not, change to it
cd /Users/shannu405/Devops_Prac1

# Verify Dockerfile exists
ls -la Dockerfile
```

---

## ❌ Error: Build fails

### Problem
```
ERROR: failed to solve: failed to fetch
```

### Solution

**Check your internet connection** - Docker needs to download base images.

**Try again:**
```bash
# Clean up and rebuild
docker-compose down
docker system prune -f
docker-compose up -d --build
```

**If using a proxy/VPN:**
- Configure Docker Desktop settings
- Or set proxy environment variables

---

## ❌ Error: "Out of disk space"

### Problem
```
no space left on device
```

### Solution

**Clean up Docker:**
```bash
# Remove unused containers, networks, images
docker system prune -a

# Remove unused volumes
docker volume prune
```

**Check disk space:**
```bash
df -h
```

---

## ✅ Quick Health Check

Run these commands to verify everything is working:

```bash
# 1. Check Docker is running
docker ps

# 2. Check Docker Compose version
docker-compose --version

# 3. Check if containers are running
docker-compose ps

# 4. Check application health
curl http://localhost:5000/health

# 5. View logs
docker-compose logs
```

---

## 🆘 Still Having Issues?

1. **Check Docker Desktop status**
   - Is the whale icon in your menu bar?
   - Does it show "Docker Desktop is running"?

2. **Restart Docker Desktop**
   - Quit Docker Desktop completely
   - Wait 10 seconds
   - Start it again

3. **Check logs**
   ```bash
   docker-compose logs -f
   ```

4. **Start fresh**
   ```bash
   docker-compose down
   docker system prune -f
   docker-compose up -d --build
   ```

5. **Verify files**
   - Make sure all files are in the project directory
   - Check that Dockerfile and docker-compose.yml exist

---

## 💡 Prevention Tips

1. **Always start Docker Desktop first** before running Docker commands
2. **Wait for Docker to fully start** (whale icon should be steady)
3. **Check ports** before starting (make sure nothing else is using them)
4. **Keep Docker Desktop updated** for latest fixes

---

**Most common issue: Docker Desktop not running!** 🐳

Make sure Docker Desktop is started before running any Docker commands.

