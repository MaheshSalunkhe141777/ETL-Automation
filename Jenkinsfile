pipeline {
    agent any
    
    stages {
        stage('Install Dependencies') {
            steps {
                // This ensures pandas, openpyxl, and pytest are available
                bat 'pip install pandas openpyxl pytest'
            }
        }
        
        stage('Running Tests') {
            steps {
                // Using 'python -m pytest' is safer on Windows to avoid PATH issues
                bat 'python -m pytest -v'
            }
        }
        
        stage('Run ETL') {
            steps {
                echo 'Running main ETL script...'
                bat 'python main.py'
            }
        }
    }
}
