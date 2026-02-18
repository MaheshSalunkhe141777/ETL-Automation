pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Initialize & Setup') {
            steps {
                echo 'Ensuring all plugins are ready...'
                bat 'python -m pip install pandas openpyxl pytest pytest-html'
            }
        }

        stage('Data Validation (Tests)') {
            steps {
                echo 'Targeting tests in ETL_Project folder...'
                // Explicitly pointing to the folder where your test_*.py files live
                bat 'python -m pytest ETL_Project/ -v --html=report.html --self-contained-html'
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
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
        }
    }
}
