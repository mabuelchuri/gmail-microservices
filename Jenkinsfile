pipeline {
    agent any

    environment {
        DOCKER_HOST = "unix:///var/run/docker.sock"
    }

    stages {

        stage('Clone Repository') {
            steps {
                git(
                    url: 'https://github.com/mabuelchuri/gmail-microservices.git',
                    branch: 'main'
                )
            }
        }

        stage('Build Docker Images') {
            steps {
                echo "Building Docker images..."
                sh 'docker build -t email-api:latest ./email-api'
                sh 'docker build -t mail-storage:latest ./mail-storage'
                sh 'docker build -t spam-checker:latest ./spam-checker'
            }
        }

        stage('Load Images into Minikube') {
            steps {
                echo "Loading images into Minikube..."
                sh 'minikube image load email-api:latest'
                sh 'minikube image load mail-storage:latest'
                sh 'minikube image load spam-checker:latest'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying Kubernetes manifests..."
                sh 'kubectl apply -f ./k8s'
            }
        }

        stage('Check Pods') {
            steps {
                echo "Checking pod status..."
                sh 'kubectl get pods'
            }
        }
    }
}
