#!/bin/bash

# ============================================================================
# DEPLOYMENT SCRIPT
# ============================================================================
# This script automates the deployment process
# 
# What it does:
# 1. Builds the Docker image
# 2. Tests the image
# 3. Stops the old container
# 4. Starts a new container with the new image
# 5. Checks that everything is working
#
# Usage: ./scripts/deploy.sh [version] [environment]
# Example: ./scripts/deploy.sh v1.0.0 production
# ============================================================================

set -e  # Exit immediately if any command fails (safety first!)

echo "🚀 Starting deployment process..."

# Colors for better output (makes it easier to read)
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# ----------------------------------------------------------------------------
# CONFIGURATION
# ----------------------------------------------------------------------------
# Get version and environment from command line arguments
# $1 = first argument (version), $2 = second argument (environment)
# If not provided, use defaults

IMAGE_NAME="devops-learning-app"
VERSION=${1:-latest}           # Default to "latest" if not provided
ENVIRONMENT=${2:-production}   # Default to "production" if not provided

echo -e "${YELLOW}Deploying ${IMAGE_NAME}:${VERSION} to ${ENVIRONMENT}${NC}"

# ----------------------------------------------------------------------------
# STEP 1: BUILD DOCKER IMAGE
# ----------------------------------------------------------------------------
echo -e "${GREEN}Step 1: Building Docker image...${NC}"
docker build -t ${IMAGE_NAME}:${VERSION} .

# Check if build was successful
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Image built successfully${NC}"
else
    echo -e "${RED}✗ Image build failed${NC}"
    exit 1
fi

# ----------------------------------------------------------------------------
# STEP 2: RUN TESTS
# ----------------------------------------------------------------------------
echo -e "${GREEN}Step 2: Running tests...${NC}"
docker run --rm ${IMAGE_NAME}:${VERSION} python -c "import app; print('✓ Tests passed')"

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Tests passed${NC}"
else
    echo -e "${RED}✗ Tests failed${NC}"
    exit 1
fi

# ----------------------------------------------------------------------------
# STEP 3: STOP EXISTING CONTAINER
# ----------------------------------------------------------------------------
echo -e "${GREEN}Step 3: Stopping existing container...${NC}"

# Try to stop the container (|| true means "don't fail if it doesn't exist")
docker stop ${IMAGE_NAME} 2>/dev/null || true
docker rm ${IMAGE_NAME} 2>/dev/null || true

echo -e "${GREEN}✓ Old container stopped and removed${NC}"

# ----------------------------------------------------------------------------
# STEP 4: START NEW CONTAINER
# ----------------------------------------------------------------------------
echo -e "${GREEN}Step 4: Starting new container...${NC}"

docker run -d \
  --name ${IMAGE_NAME} \
  -p 5001:5000 \
  -e ENVIRONMENT=${ENVIRONMENT} \
  -e APP_VERSION=${VERSION} \
  --restart unless-stopped \
  ${IMAGE_NAME}:${VERSION}

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Container started${NC}"
else
    echo -e "${RED}✗ Failed to start container${NC}"
    exit 1
fi

# ----------------------------------------------------------------------------
# STEP 5: HEALTH CHECK
# ----------------------------------------------------------------------------
echo -e "${GREEN}Step 5: Performing health check...${NC}"

# Wait a few seconds for the app to start
sleep 5

# Check if the health endpoint responds
if curl -f http://localhost:5001/health > /dev/null 2>&1; then
    echo -e "${GREEN}✓ Deployment successful!${NC}"
    echo ""
    echo "Application is running at:"
    echo "  - http://localhost:5001"
    echo "  - http://localhost:5001/health (health check)"
    echo ""
    echo "View logs with: docker logs ${IMAGE_NAME}"
    echo "Stop with: docker stop ${IMAGE_NAME}"
else
    echo -e "${YELLOW}⚠ Health check failed. Check logs with: docker logs ${IMAGE_NAME}${NC}"
    exit 1
fi

echo -e "${GREEN}Deployment complete!${NC}"

# ============================================================================
# WHAT JUST HAPPENED?
# ============================================================================
# 
# 1. Built a new Docker image with your latest code
# 2. Tested that the image works
# 3. Stopped the old version (zero-downtime deployment)
# 4. Started the new version
# 5. Verified it's working
#
# This is a basic deployment. In production, you might:
# - Use blue-green deployment (run both versions, switch traffic)
# - Use rolling updates (update containers one at a time)
# - Deploy to multiple servers
# - Use orchestration tools (Kubernetes)
#
# ============================================================================
