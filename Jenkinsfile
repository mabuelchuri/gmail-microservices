pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    environment {
        IMAGE_NAME = "email-api"
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning Git repository manually...'
                git url: 'https://github.com/mabuelchuri/gmail-microservices.git', branch: 'main'
            }
        }

        stage('Build Docker Images') {
            steps {
                echo 'Building Docker images...'
                sh 'docker build -t email-api:latest ./email-api'
                sh 'docker build -t spam-checker:latest ./spam-checker'
                sh 'docker build -t mail-storage:latest ./mail-storage'
            }
        }

        stage('Load Images into Minikube') {
            steps {
                echo 'Loading Docker images into Minikube...'
                sh 'minikube image load email-api:latest'
                sh 'minikube image load spam-checker:latest'
                sh 'minikube image load mail-storage:latest'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying to Kubernetes...'
                sh 'kubectl apply -f k8s/'
            }
        }

        stage('Check Pods') {
            steps {
                sh 'kubectl get pods -o wide'
            }
        }
    }
}
