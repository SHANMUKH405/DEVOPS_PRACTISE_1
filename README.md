# DevOps Practice Project 1 🚀

A comprehensive DevOps practice repository demonstrating modern DevOps practices including containerization, CI/CD, infrastructure as code, and monitoring.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Development](#development)
- [Testing](#testing)
- [Docker](#docker)
- [Kubernetes](#kubernetes)
- [CI/CD](#cicd)
- [Infrastructure as Code](#infrastructure-as-code)
- [Monitoring](#monitoring)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This is a hands-on DevOps practice project featuring a simple Flask web application with complete DevOps tooling and best practices. The project is designed to help learn and practice:

- Application development with Python Flask
- Containerization with Docker
- Container orchestration with Kubernetes
- CI/CD automation with GitHub Actions
- Infrastructure as Code with Terraform
- Monitoring and alerting with Prometheus
- Security scanning and testing

## ✨ Features

- **Simple Flask Web Application**: RESTful API with health checks
- **Dockerized Application**: Multi-stage Docker build with security best practices
- **Kubernetes Manifests**: Complete K8s deployment, service, and ingress configurations
- **CI/CD Pipeline**: Automated testing, building, and security scanning
- **Infrastructure as Code**: AWS infrastructure provisioning with Terraform
- **Monitoring Setup**: Prometheus configuration with alerting rules
- **Unit Tests**: Comprehensive test coverage with pytest
- **Security**: Non-root container, vulnerability scanning, and security best practices

## 🔧 Prerequisites

- Python 3.11+
- Docker and Docker Compose
- kubectl (for Kubernetes)
- Terraform (for IaC)
- Git

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/SHANMUKH405/DEVOPS_PRACTISE_1.git
   cd DEVOPS_PRACTISE_1
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   - Open your browser and navigate to `http://localhost:5000`
   - Health check: `http://localhost:5000/health`
   - API info: `http://localhost:5000/api/info`

### Using Docker Compose

1. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

2. **Access the application**
   - Navigate to `http://localhost:5000`

3. **Stop the application**
   ```bash
   docker-compose down
   ```

## 📁 Project Structure

```
DEVOPS_PRACTISE_1/
├── app.py                      # Main Flask application
├── test_app.py                 # Unit tests
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker configuration
├── docker-compose.yml          # Docker Compose configuration
├── .gitignore                  # Git ignore rules
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # GitHub Actions CI/CD pipeline
├── k8s/                        # Kubernetes manifests
│   ├── deployment.yaml        # Application deployment
│   ├── service.yaml           # Service configuration
│   └── ingress.yaml           # Ingress configuration
├── terraform/                  # Infrastructure as Code
│   ├── main.tf                # Main Terraform configuration
│   ├── variables.tf           # Variable definitions
│   ├── outputs.tf             # Output definitions
│   └── resources.tf           # AWS resource definitions
└── monitoring/                 # Monitoring configurations
    ├── prometheus.yml         # Prometheus configuration
    └── alerts.yml             # Alert rules
```

## 💻 Development

### Running Tests

```bash
# Run all tests
pytest test_app.py -v

# Run with coverage
pytest test_app.py -v --cov=app --cov-report=term-missing

# Run with coverage HTML report
pytest test_app.py -v --cov=app --cov-report=html
```

### Code Quality

```bash
# Check code style with flake8
flake8 app.py test_app.py --max-line-length=120

# Run pylint
pylint app.py --disable=C0111,C0103
```

## 🐳 Docker

### Building the Image

```bash
docker build -t devops-practice:latest .
```

### Running the Container

```bash
docker run -d \
  -p 5000:5000 \
  -e ENVIRONMENT=production \
  -e APP_VERSION=1.0.0 \
  --name devops-practice-app \
  devops-practice:latest
```

### View Logs

```bash
docker logs -f devops-practice-app
```

### Health Check

```bash
docker inspect --format='{{json .State.Health}}' devops-practice-app
```

## ☸️ Kubernetes

### Deploy to Kubernetes

```bash
# Apply all manifests
kubectl apply -f k8s/

# Or apply individually
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml
```

### Check Deployment Status

```bash
# Check pods
kubectl get pods -l app=devops-practice

# Check services
kubectl get svc devops-practice-service

# Check ingress
kubectl get ingress devops-practice-ingress
```

### View Logs

```bash
kubectl logs -l app=devops-practice --tail=100 -f
```

### Scale Deployment

```bash
kubectl scale deployment devops-practice-app --replicas=5
```

## 🔄 CI/CD

The project includes a comprehensive GitHub Actions workflow that:

1. **Tests**: Runs unit tests with coverage reporting
2. **Linting**: Checks code quality with flake8 and pylint
3. **Build**: Builds Docker image with caching
4. **Security**: Scans for vulnerabilities with Trivy

The pipeline runs on:
- Push to `main` or `develop` branches
- Pull requests to `main` or `develop` branches

## 🏗️ Infrastructure as Code

### Initialize Terraform

```bash
cd terraform
terraform init
```

### Plan Infrastructure Changes

```bash
terraform plan -var="environment=dev"
```

### Apply Infrastructure

```bash
terraform apply -var="environment=dev"
```

### Destroy Infrastructure

```bash
terraform destroy -var="environment=dev"
```

## 📊 Monitoring

### Prometheus Setup

The `monitoring/prometheus.yml` file contains the Prometheus configuration for scraping metrics.

### Alert Rules

Alert rules are defined in `monitoring/alerts.yml` for:
- Application downtime
- High response times
- High memory usage

### Setting Up Monitoring

```bash
# Run Prometheus (example)
docker run -d \
  -p 9090:9090 \
  -v $(pwd)/monitoring/prometheus.yml:/etc/prometheus/prometheus.yml \
  prom/prometheus
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🎓 Learning Resources

- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Terraform Documentation](https://www.terraform.io/docs/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Prometheus Documentation](https://prometheus.io/docs/)
- [Flask Documentation](https://flask.palletsprojects.com/)

## 📧 Contact

For questions or feedback, please open an issue in this repository.

---

**Happy Learning! 🎉**