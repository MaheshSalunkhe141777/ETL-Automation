pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Pulls the code from your GitHub repository
                checkout scm
            }
        }

        stage('Initialize & Setup') {
            steps {
                echo 'Installing dependencies including pyodbc...'
                // Added pyodbc to the list to fix the ModuleNotFoundError
                bat '''
                    python -m pip install --upgrade pip
                    python -m pip install pandas openpyxl pytest pytest-html pyodbc
                '''
            }
        }

        stage('Data Validation (Tests)') {
            steps {
                echo 'Running data validation tests...'
                // Runs pytest and generates the HTML report
                bat 'python -m pytest . -v --html=report.html --self-contained-html'
            }
        }

        stage('Run ETL Job') {
            steps {
                echo 'Tests passed! Executing main ETL script...'
                bat 'python main.py'
            }
        }
    }

    post {
        always {
            echo 'Archiving HTML Report...'
            // This ensures the report is saved even if the tests fail
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
        }
        failure {
            echo 'Pipeline failed. Please check the "Data Validation" stage for errors.'
        }
    }
}
