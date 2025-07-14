# Cloud SRE Project 
# 🚀 Cloud SRE Flask App with GitHub Actions CI/CD

This project demonstrates how to build and prepare a containerized Flask web application for deployment on Azure Container Apps using GitHub Actions.

## ✅ Highlights

- Flask web app containerized using Docker
- GitHub Actions pipeline with Azure login via service principal
- CI pipeline verifies code + auth flow
- Deployment step documented but skipped due to Azure Free Tier ACR limitations

## 📌 Why deployment was skipped

Azure Free Tier limits prevent ACR Tasks and restrict Container App image pulls without role assignments. Since this app focuses on CI/CD and infrastructure, the project was paused at a successful CI build.

## 🛠️ Stack

- Python + Flask
- Docker
- GitHub Actions
- Azure CLI & Azure Container Apps
