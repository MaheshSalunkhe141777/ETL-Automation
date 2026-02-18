pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Simplified checkout to avoid the 'whatchanged' Git error
                checkout scm
            }
        }

        stage('Initialize & Setup') {
            steps {
                echo 'Installing requirements and HTML reporting plugin...'
                // Added pytest-html to fix the unrecognized argument error
                bat 'python -m pip install pandas openpyxl pytest pytest-html'
            }
        }

        stage('Data Validation (Tests)') {
            steps {
                echo 'Running Automation Tests...'
                // Removed 'ETL_Project/' to search the whole repo for test_*.py files
                bat 'python -m pytest -v --html=report.html --self-contained-html'
            }
        }

        stage('Run ETL Job') {
            steps {
                echo 'Executing ETL main script...'
                bat 'python main.py'
            }
        }
    }

    post {
        always {
            echo 'Capturing Test Report...'
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
        }
    }
}
