pipeline {

    agent any

    environment {
        PYTHONUNBUFFERED = '1'
    }

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/SowmyaGuru/Web_Scrap_Python'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install --upgrade pip'
                sh 'pip3 install -r requirement.txt'
            }
        }

        stage('Run Regression Tests') {
            steps {
                sh 'pytest -m regression --html=reports/report.html --alluredir=allure-results'
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