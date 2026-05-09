pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo "שלב 1: שליפת הקוד מהמאגר"
                checkout scm
            }
        }

        stage('Cleanup Old Containers') {
            steps {
                echo "שלב 2: ניקוי קונטיינרים וimages ישנים"
                sh '''
                    docker-compose down --remove-orphans
                    docker system prune -f --volumes
                '''
            }
        }

        stage('Build Images') {
            steps {
                echo "שלב 3: בנייה של ה-images"
                sh '''
                    docker-compose build --no-cache
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo "שלב 4: הרצת בדיקות"
                sh '''
                    docker-compose run --rm tests python -m pytest test_app.py -v
                '''
            }
        }
        stage('Deploy') {
            steps {
                echo "שלב 5: הצבת האפליקציה"
                sh '''
                    docker-compose up -d
                    echo "האפליקציה מורצת בהצלחה!"
                    docker-compose logs app
                '''
            }
        }
    }

    post {
        always {
            echo "ניקוי סיום - הורדת קונטיינרים"
            sh '''
                docker-compose down
            '''
        }
        success {
            echo "הפايפליין הצליח בהצלחה! ✓"
        }
        failure {
            echo "הפايפליין נכשל! ✗"
        }
    }
}
