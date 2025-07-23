# Gmail Microservice CI/CD with Jenkins, Docker & Kubernetes

This project demonstrates a secure and automated CI/CD pipeline for a **Gmail-like microservice** using **Jenkins**, **Docker**, and **Kubernetes**. It’s designed to meet the requirements of a DevSecOps coding challenge.

---

## 🧩 Project Overview

This microservice-based application includes:
- A mock **Gmail microservice** (Node.js / Python-based REST API)
- CI/CD pipeline configured in **Jenkins**
- Containerization using **Docker**
- Deployment to a **Kubernetes cluster** (Minikube or EKS)
- Optional: Integration with **SonarQube**, **Trivy**, or other security tools

---

## 🔧 Technologies Used

- Jenkins (LTS)
- Docker
- Kubernetes (Minikube)
- Git & GitHub
- Shell Scripting
- Optional: Trivy, SonarQube, Slack notifications

---

## ⚙️ CI/CD Pipeline Stages

1. **Clone Code from GitHub**
2. **Build Docker Image**
3. **Push Image to Docker Hub**
4. **Deploy to Kubernetes Cluster**
5. **Verify Deployment**

---

## 🚀 How to Run Locally

### 1. Prerequisites

- Docker
- Minikube (with Docker driver)
- Jenkins (running as Docker container)

### 2. Jenkins Container Setup

Run this in PowerShell:

```powershell
docker run -d `
  --name jenkins `
  -u root `
  -p 8080:8080 -p 50000:50000 `
  -v jenkins_home:/var/jenkins_home `
  -v \\.\pipe\docker_engine:\\.\pipe\docker_engine `
  -v "$env:USERPROFILE\.kube":"/root/.kube" `
  jenkins/jenkins:lts-jdk11

