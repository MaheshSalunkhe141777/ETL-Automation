pipeline {
    agent any
    
    stages {
        stage('Install Requirements') {
            steps {
                // Ensure pip is available and install dependencies
                bat 'python -m pip install --upgrade pip'
                bat 'pip install pytest pandas openpyxl' 
            }
        }
        
        stage('Running Tests') {
            steps {
                // Use 'python -m pytest' to avoid PATH issues
                bat 'python -m pytest -v'
            }
        }
    }
}
