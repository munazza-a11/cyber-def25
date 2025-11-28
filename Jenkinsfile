pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'munazza-a11/cyber-def25-detector'
        TAG = "${env.BUILD_NUMBER}"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                script {
                    echo '🔨 Building Docker Image...'
                    sh "docker build -t ${DOCKER_IMAGE}:${TAG} ."
                    sh "docker tag ${DOCKER_IMAGE}:${TAG} ${DOCKER_IMAGE}:latest"
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    echo '📤 Pushing Docker Image to Docker Hub...'
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                        sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                        sh "docker push ${DOCKER_IMAGE}:${TAG}"
                        sh "docker push ${DOCKER_IMAGE}:latest"
                    }
                }
            }
        }

        stage('Run Inference (Deploy)') {
            steps {
                script {
                    echo '🚀 Deploying Container via Docker Compose...'
                    sh "IMAGE_NAME=${DOCKER_IMAGE}:${TAG} docker compose up -d"
                }
            }
        }
    }

    post {
        always {
            echo '🧹 Cleaning up...'
            sh "docker compose down || true"
            sh "docker system prune -f || true"
        }
        success {
            echo '🎯 Malware analysis completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}
