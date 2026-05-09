pipeline {
    agent any

    environment {
        DOCKER_HUB_USER = 'avital2163' 
        IMAGE_NAME = 'compose_demo_app'
        DOCKER_HUB_CREDS = 'docker-hub-credentials'
    }

    stages {
        stage('Checkout') {
            steps {
                // שימוש ב-checkout scm המובנה של ג'נקינס
                checkout scm
            }
        }

        stage('Cleanup') {
            steps {
                // שימוש ב-bat במקום sh עבור Windows
                bat 'docker-compose down --remove-orphans'
                bat 'docker system prune -f'
            }
        }

        stage('Build') {
            steps {
                bat 'docker-compose build --no-cache'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'docker-compose run --rm tests python -m pytest test_app.py -v'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: "${DOCKER_HUB_CREDS}", passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                        // התחברות ודחיפה באמצעות bat
                        bat "echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin"
                        bat "docker tag ${IMAGE_NAME} ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest"
                        bat "docker push ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest"
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker-compose up -d'
            }
        }
    }

    post {
        always {
            bat 'docker-compose down'
        }
    }
}