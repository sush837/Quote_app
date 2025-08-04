pipeline {
    agent any

    environment {
        SONARQUBE = 'MySonarQube'  // Configure this name in Jenkins > Global Config
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/sush837/Quote_app.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('MySonarQube') {
                    sh 'sonar-scanner'
                }
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t quote-app .'
            }
        }

        stage('Docker Run') {
            steps {
                sh 'docker rm -f quote-app || true'
                sh 'docker run -d -p 5000:5000 --name quote-app quote-app'
            }
        }
    }

    post {
        success {
            echo '✅ CI/CD deployment successful!'
        }
        failure {
            echo '❌ CI/CD failed!'
        }
    }
}
