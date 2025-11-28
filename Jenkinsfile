pipeline {
    agent any

    environment {
        // Your specific Docker Hub repository
        DOCKER_IMAGE = 'munazahmed431/cyber-def25-detector'
        TAG = "${currentBuild.number}"
    }

    stages {
        stage('Build Image') {
            steps {
                script {
                    echo 'Building Docker Image...'
                    // Build the image using the Dockerfile in current directory
                    sh "docker build -t ${DOCKER_IMAGE}:${TAG} ."
                    // Tag it as 'latest' as well
                    sh "docker tag ${DOCKER_IMAGE}:${TAG} ${DOCKER_IMAGE}:latest"
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    echo 'Logging into Docker Hub...'
                    // Uses the 'dockerhub-creds' ID you set up in Jenkins Dashboard
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                        sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                        
                        echo 'Pushing images...'
                        sh "docker push ${DOCKER_IMAGE}:${TAG}"
                        sh "docker push ${DOCKER_IMAGE}:latest"
                    }
                }
            }
        }

        stage('Run Inference (Deploy)') {
            steps {
                script {
                    echo 'Running Container via Docker Compose...'
                    // Passes your specific image to the docker-compose.yml file
                    sh "IMAGE_NAME=${DOCKER_IMAGE}:${TAG} docker compose up"
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up containers...'
            // Shuts down container to save resources
            sh "docker compose down"
        }
        success {
            echo 'CYBER-DEF25 Assignment Completed Successfully!'
        }
    }
}
