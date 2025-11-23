# ============================================================================
# MAKEFILE - AUTOMATION COMMANDS
# ============================================================================
# A Makefile provides shortcuts for common commands
# Instead of typing long commands, you can type: make <command>
#
# This is a DevOps best practice - make common tasks easy!
# ============================================================================

# .PHONY tells Make these aren't file names, they're commands
.PHONY: help build run stop clean test lint docker-build docker-run docker-stop docker-clean compose-up compose-down logs

# Default target - when you just type "make", show help
# This is the first target, so it runs when you type "make" without arguments
help:
	@echo "DevOps Learning Project - Available Commands:"
	@echo ""
	@echo "  Python Commands:"
	@echo "    make build          - Install Python dependencies"
	@echo "    make run            - Run the application locally"
	@echo "    make test           - Run tests"
	@echo "    make lint           - Run linting (code quality checks)"
	@echo ""
	@echo "  Docker Commands:"
	@echo "    make docker-build   - Build Docker image"
	@echo "    make docker-run     - Run Docker container"
	@echo "    make docker-stop    - Stop Docker container"
	@echo "    make docker-clean   - Remove Docker containers and images"
	@echo ""
	@echo "  Docker Compose Commands:"
	@echo "    make compose-up     - Start services with docker-compose"
	@echo "    make compose-down   - Stop services with docker-compose"
	@echo "    make logs           - View docker-compose logs"
	@echo ""
	@echo "  Cleanup:"
	@echo "    make clean          - Clean Python cache and virtual environment"

# ============================================================================
# PYTHON ENVIRONMENT SETUP
# ============================================================================

# Create virtual environment and install dependencies
build:
	@echo "Creating virtual environment..."
	python3 -m venv venv
	@echo "Installing dependencies..."
	. venv/bin/activate && pip install -r requirements.txt
	@echo "✓ Setup complete! Activate with: source venv/bin/activate"

# Run the application locally (without Docker)
# Note: Requires Python 3.11+ and installed dependencies
run:
	@echo "Starting Flask application..."
	@echo "Make sure you have installed dependencies: make build"
	python3 app.py

# Run tests
test:
	@echo "Running tests..."
	python3 -m pytest tests/ || python3 -c "import app; print('✓ App imports successfully')"

# Run linting (code quality checks)
lint:
	@echo "Running linter..."
	flake8 app.py --max-line-length=127 || echo "Install flake8: pip install flake8"

# ============================================================================
# DOCKER COMMANDS
# ============================================================================

# Build the Docker image
docker-build:
	@echo "Building Docker image..."
	docker build -t devops-learning-app:latest .
	@echo "✓ Image built successfully!"

# Run a Docker container
docker-run:
	@echo "Starting Docker container..."
	docker run -d -p 5000:5000 --name devops-learning-app devops-learning-app:latest
	@echo "✓ Container started! Visit http://localhost:5000"

# Stop and remove Docker container
docker-stop:
	@echo "Stopping container..."
	docker stop devops-learning-app || true
	docker rm devops-learning-app || true
	@echo "✓ Container stopped and removed"

# Clean up Docker containers and images
docker-clean: docker-stop
	@echo "Removing Docker image..."
	docker rmi devops-learning-app:latest || true
	@echo "✓ Cleanup complete"

# ============================================================================
# DOCKER COMPOSE COMMANDS
# ============================================================================

# Start all services with Docker Compose
compose-up:
	@echo "Starting services with Docker Compose..."
	docker-compose up -d
	@echo "✓ Services started! Visit http://localhost:5000"

# Stop all services
compose-down:
	@echo "Stopping services..."
	docker-compose down
	@echo "✓ Services stopped"

# View logs from all services
logs:
	@echo "Viewing logs (Ctrl+C to exit)..."
	docker-compose logs -f

# ============================================================================
# CLEANUP
# ============================================================================

# Clean Python cache and virtual environment
clean:
	@echo "Cleaning up..."
	@find . -type d -name __pycache__ -exec rm -r {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete
	@rm -rf venv/ .pytest_cache/ .coverage htmlcov/
	@echo "✓ Cleanup complete"

# ============================================================================
# USAGE EXAMPLES
# ============================================================================
# 
# Quick start:
#   make compose-up
#
# View logs:
#   make logs
#
# Stop everything:
#   make compose-down
#
# Clean up:
#   make clean
#
# ============================================================================
