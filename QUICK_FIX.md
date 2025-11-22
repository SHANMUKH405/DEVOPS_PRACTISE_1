# ⚡ Quick Fix: Docker Not Running

## The Problem
```
Cannot connect to the Docker daemon... Is the docker daemon running?
```

**Docker Desktop is not running!**

---

## ✅ Solution (3 Steps)

### Step 1: Start Docker Desktop

**Option A: I just started it for you!**
- Wait 15-30 seconds for Docker Desktop to fully start
- Look for the Docker whale icon 🐳 in your menu bar (top right)

**Option B: Start it manually**
1. Press `Cmd + Space` (Spotlight)
2. Type "Docker"
3. Press Enter to open Docker Desktop
4. Wait for it to start (15-30 seconds)

### Step 2: Verify Docker is Running

Look for the Docker whale icon 🐳 in your menu bar:
- ✅ **Solid whale icon** = Docker is running
- ❌ **No icon or animated** = Still starting (wait more)

Or check in terminal:
```bash
docker ps
```

**Expected output:**
```
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```
(Even if empty, this means Docker is working!)

**If you still get an error:**
- Docker is still starting → Wait 30 more seconds
- Docker didn't start → Try Step 1 again

### Step 3: Run Your Command Again

Once Docker is running:
```bash
docker-compose up -d
```

---

## 🎯 Quick Checklist

- [ ] Docker Desktop is open (you see the Docker Desktop window)
- [ ] Whale icon 🐳 appears in menu bar
- [ ] `docker ps` command works (shows a table)
- [ ] Now run `docker-compose up -d`

---

## ⏱️ How Long to Wait?

- **First time:** 30-60 seconds (Docker needs to initialize)
- **After that:** 10-20 seconds (faster startup)

**Signs Docker is ready:**
- Whale icon is solid (not animated)
- Menu shows "Docker Desktop is running"
- `docker ps` works without errors

---

## 🆘 Still Not Working?

1. **Quit Docker Desktop completely**
   - Click whale icon → Quit Docker Desktop
   - Wait 10 seconds

2. **Start it again**
   - Open Docker Desktop from Applications
   - Wait 30 seconds

3. **Check if Docker Desktop is installed**
   ```bash
   ls /Applications/ | grep -i docker
   ```
   - If nothing shows, install Docker Desktop from docker.com

---

**Once Docker Desktop is running, your `docker-compose up -d` command will work!** 🚀

