pipeline {

    agent any

    environment {
        PATH = "/var/lib/jenkins/.local/bin:${env.PATH}"
    }

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install --break-system-packages --upgrade pip'
                sh 'pip3 install --break-system-packages -r requirement.txt'
            }
        }

        stage('Run Regression Tests') {
            steps {
                sh 'python3 -m pytest -v --html=reports/report.html'
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
        emailext(
            subject: "Jenkins Build Success - ${env.JOB_NAME}",
            body: "Build Passed Successfully.\nBuild URL: ${env.BUILD_URL}",
            to: "sowmyaguru62@gmail.com"
        )
    }

    failure {
        emailext(
            subject: "Jenkins Build Failed - ${env.JOB_NAME}",
            body: "Build Failed.\nCheck Console: ${env.BUILD_URL}",
            to: "sowmyaguru62@gmail.com"
        )
    }
}