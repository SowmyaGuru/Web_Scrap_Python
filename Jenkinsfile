pipeline {

    agent any

//     tools {
//         // Optional if Python configured in Jenkins
//     }

    environment {
        PYTHONUNBUFFERED = '1'
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                url: 'https://github.com/SowmyaGuru/Web_Scrap_Python.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirement.txt'
            }
        }

        stage('Run Smoke Tests') {
            steps {
                bat 'pytest -m smoke'
            }
        }

        stage('Run Full Regression') {
            steps {
                bat 'pytest -m regression'
            }
        }
    }

    post {

        always {

            publishHTML([
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Automation Test Report'
            ])
        }

        success {
            echo 'Pipeline executed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}