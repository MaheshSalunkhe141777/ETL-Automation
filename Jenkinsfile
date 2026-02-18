pipeline {
    agent any

    stages {
        stage('Initialize & Setup') {
            steps {
                echo 'Cleaning workspace and installing dependencies...'
                // Ensures all necessary Python libraries are present on your Windows machine
                bat 'pip install pandas openpyxl pytest'
            }
        }

        stage('Data Validation (Tests)') {
            steps {
                echo 'Running pytest on ETL_Project folder...'
                // Directs pytest to the specific folder where your test scripts live
                bat 'python -m pytest ETL_Project/ -v'
            }
        }

        stage('Run ETL Job') {
            steps {
                echo 'Executing main ETL script...'
                // Runs your primary transformation logic
                bat 'python main.py'
            }
        }
    }

    post {
        always {
            echo 'Archiving results...'
            // This will save your execution report so you can see it in Jenkins
            archiveArtifacts artifacts: 'test_execution.html', allowEmptyArchive: true
        }
        success {
            echo 'ETL Pipeline finished successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the Console Output for errors.'
        }
    }
}
