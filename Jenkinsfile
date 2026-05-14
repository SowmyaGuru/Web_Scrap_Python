pipeline {

    agent any

    environment {
        PYTHONUNBUFFERED = '1'
    }

    stages {

        stage('Install Dependencies') {
            steps {

                bat '"C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pip install --upgrade pip'

                bat '"C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pip install -r requirement.txt'
            }
        }

        stage('Run Regression Tests') {
            steps {

                bat '"C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pytest -m regression --html=reports/report.html --alluredir=allure-results'
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

            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: 'allure-results']]
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
pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/SowmyaGuru/Web_Scrap_Python'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirement.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest -v'
            }
        }
    }
}