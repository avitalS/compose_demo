pipeline {
    agent any

    environment {
        DOCKER_HUB_USER = 'avital2163' 
        IMAGE_NAME = 'compose_demo_app' // השם שיופיע ב-Docker Hub
        DOCKER_HUB_CREDS = 'docker-hub-credentials' // המזהה שהגדרת ב-Credentials של ג'נקינס
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Cleanup') {
            steps {
                sh 'docker-compose down --remove-orphans'
                sh 'docker system prune -f'
            }
        }

        stage('Build') {
            steps {
                sh 'docker-compose build --no-cache'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker-compose run --rm tests python -m pytest test_app.py -v'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: "${DOCKER_HUB_CREDS}", passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                        sh "echo \$DOCKER_PASS | docker login -u \$DOCKER_USER --password-stdin"
                        // תיוג והעלאה של ה-image של האפליקציה (app)
                        sh "docker tag ${IMAGE_NAME} ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest"
                        sh "docker push ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest"
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }

    post {
        always {
            sh 'docker-compose down'
        }
    }
}