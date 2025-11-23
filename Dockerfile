# ============================================================================
# DOCKERFILE - CONTAINER BUILD INSTRUCTIONS
# ============================================================================
# This file tells Docker HOW to build a container for our application
# 
# Think of it like a recipe:
# 1. Start with a base (Python)
# 2. Add ingredients (install libraries)
# 3. Add our code
# 4. Tell it how to run
#
# This is "Infrastructure as Code" - we define our infrastructure in files
# ============================================================================

# ----------------------------------------------------------------------------
# STAGE 1: Builder Stage
# ----------------------------------------------------------------------------
# Multi-stage builds make our final image smaller
# Stage 1: Install everything (can be big)
# Stage 2: Copy only what we need (stays small)

FROM python:3.11-slim as builder

# Set working directory inside container
# All commands will run from /app
WORKDIR /app

# Copy requirements file first
# Docker caches layers - if requirements.txt doesn't change,
# Docker reuses the cached layer (faster builds!)
COPY requirements.txt .

# Install Python dependencies
# --no-cache-dir = Don't store cache (smaller image)
# --user = Install to user directory (better security)
RUN pip install --no-cache-dir --user -r requirements.txt

# ----------------------------------------------------------------------------
# STAGE 2: Production Stage
# ----------------------------------------------------------------------------
# This is the final image that gets deployed
# It's smaller because we only copy what we need

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy installed packages from builder stage
# We only copy the installed packages, not the build tools
COPY --from=builder /root/.local /root/.local

# Copy our application code
COPY app.py .

# Make sure scripts in .local are usable
# This adds the user's local bin to PATH
ENV PATH=/root/.local/bin:$PATH

# Expose port 5000
# This tells Docker: "This container listens on port 5000"
# It's documentation - doesn't actually open the port
EXPOSE 5000

# Set environment variables
# FLASK_APP tells Flask which file is the application
# PYTHONUNBUFFERED ensures Python output is shown immediately (better for logs)
ENV FLASK_APP=app.py
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# ----------------------------------------------------------------------------
# HEALTH CHECK
# ----------------------------------------------------------------------------
# Docker can automatically check if our container is healthy
# If health check fails, Docker knows something is wrong
# 
# --interval=30s = Check every 30 seconds
# --timeout=3s = If no response in 3 seconds, consider it failed
# --start-period=5s = Wait 5 seconds before first check (app needs time to start)
# --retries=3 = Try 3 times before marking as unhealthy

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')"

# ----------------------------------------------------------------------------
# COMMAND TO RUN
# ----------------------------------------------------------------------------
# This is what runs when the container starts
# 
# gunicorn = Production web server (better than Flask's dev server)
# --bind 0.0.0.0:5000 = Listen on all interfaces, port 5000
# --workers 2 = Run 2 worker processes (can handle more requests)
# app:app = Import "app" from "app.py", use the "app" variable

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]

# ============================================================================
# HOW TO USE THIS DOCKERFILE
# ============================================================================
# 
# Build the image:
#   docker build -t devops-learning-app .
#
# Run the container:
#   docker run -p 5000:5000 devops-learning-app
#
# ============================================================================
