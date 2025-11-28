pipeline {
    agent any

    environment {
        // Updated Docker image with correct Docker Hub username
        DOCKER_IMAGE = 'munazahmed431/cyber-def25-detector'
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
                    // Use the correct credentials ID and Docker username
                    withCredentials([string(credentialsId: 'docker-hub-pass', variable: 'DOCKER_PASS')]) {
                        sh """
                            echo $DOCKER_PASS | docker login -u munazahmed431 --password-stdin
                            docker push ${DOCKER_IMAGE}:${TAG}
                            docker push ${DOCKER_IMAGE}:latest
                        """
                    }
                }
            }
        }

        stage('Run Inference (Deploy)') {
            steps {
                script {
                    echo '🚀 Deploying Container via Docker Compose...'
                    // Pass IMAGE_NAME environment variable to docker compose
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

