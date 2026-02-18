pipeline {
    agent any

    stages {
        stage('Run ETL') {
            steps {
                echo 'Starting ETL Automation...'
                // Ensure python is installed on your Jenkins agent
                sh 'python main.py'
            }
        }
    }
    
    post {
        success {
            echo 'ETL Process completed successfully!'
        }
        failure {
            echo 'ETL Process failed. Check the console output above.'
        }
    }
}
