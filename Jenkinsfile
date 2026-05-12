pipeline {

    agent any

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
                powershell 'python -m pip install --upgrade pip'
                powershell 'pip install -r requirements.txt'
            }
        }

        stage('Run Smoke Tests') {
            steps {
                powershell 'python -m pytest -m smoke --html=reports/report.html'
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