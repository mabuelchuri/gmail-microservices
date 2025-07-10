pipeline {
    agent any

    environment {
        DOCKER_HOST = "unix:///var/run/docker.sock"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/mabuelchuri/gmail-microservices.git'  branch: 'main'
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    sh 'docker build -t email-api:latest ./email-api'
                    sh 'docker build -t spam-checker:latest ./spam-checker'
                    sh 'docker build -t mail-storage:latest ./mail-storage'
                }
            }
        }

        stage('Load Images into Minikube') {
            steps {
                script {
                    sh 'minikube image load email-api:latest'
                    sh 'minikube image load spam-checker:latest'
                    sh 'minikube image load mail-storage:latest'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f ./k8s/'
            }
        }

        stage('Check Pods') {
            steps {
                sh 'kubectl get pods'
            }
        }
    }
}
