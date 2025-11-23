#!/bin/bash

# ============================================================================
# MONITORING SCRIPT
# ============================================================================
# This script provides monitoring capabilities for the DevOps learning project
# This script monitors your application to ensure it's working correctly
# 
# What it checks:
# 1. Is the container running?
# 2. Is the application healthy?
# 3. How much resources is it using?
# 4. What are the recent logs?
#
# Usage: ./scripts/monitor.sh
# ============================================================================

CONTAINER_NAME="devops-learning-app"
HEALTH_ENDPOINT="http://localhost:5000/health"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo "📊 Monitoring DevOps Learning App"
echo "=================================="
echo ""

# ----------------------------------------------------------------------------
# CHECK 1: Container Status
# ----------------------------------------------------------------------------
echo "Container Status:"
if docker ps | grep -q ${CONTAINER_NAME}; then
    echo -e "${GREEN}✓ Container is running${NC}"
else
    echo -e "${RED}✗ Container is not running${NC}"
    echo ""
    echo "Start it with: docker-compose up -d"
    exit 1
fi
echo ""

# ----------------------------------------------------------------------------
# CHECK 2: Container Statistics
# ----------------------------------------------------------------------------
echo "Container Statistics (CPU, Memory, Network):"
echo "--------------------------------------------"
docker stats ${CONTAINER_NAME} --no-stream --format "table {{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}"
echo ""

# ----------------------------------------------------------------------------
# CHECK 3: Health Check
# ----------------------------------------------------------------------------
echo "Health Check:"
echo "-------------"
if curl -f ${HEALTH_ENDPOINT} > /dev/null 2>&1; then
    echo -e "${GREEN}✓ Application is healthy${NC}"
    echo ""
    echo "Health check response:"
    curl -s ${HEALTH_ENDPOINT} | python3 -m json.tool 2>/dev/null || curl -s ${HEALTH_ENDPOINT}
else
    echo -e "${RED}✗ Application health check failed${NC}"
    echo "The application may not be responding correctly."
fi
echo ""

# ----------------------------------------------------------------------------
# CHECK 4: Recent Logs
# ----------------------------------------------------------------------------
echo "Recent Logs (last 10 lines):"
echo "----------------------------"
docker logs --tail 10 ${CONTAINER_NAME}
echo ""

# ----------------------------------------------------------------------------
# SUMMARY
# ----------------------------------------------------------------------------
echo "=================================="
echo "Monitoring complete!"
echo ""
echo "Useful commands:"
echo "  - View all logs: docker logs -f ${CONTAINER_NAME}"
echo "  - View stats: docker stats ${CONTAINER_NAME}"
echo "  - Restart: docker restart ${CONTAINER_NAME}"
echo "  - Stop: docker stop ${CONTAINER_NAME}"

# ============================================================================
# WHAT IS MONITORING?
# ============================================================================
# 
# Monitoring helps you:
# - Know if your app is working
# - Catch problems early
# - Understand resource usage
# - Debug issues faster
#
# In production, you'd use tools like:
# - Prometheus (metrics collection)
# - Grafana (visualization)
# - ELK Stack (log aggregation)
# - Datadog, New Relic (APM tools)
#
# ============================================================================
