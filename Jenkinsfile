pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Disabling changelog to bypass the Git 'whatchanged' error
                checkout([$class: 'GitSCM', 
                    branches: [[name: '*/main']], 
                    extensions: [[$class: 'DisableRemotePoll']], 
                    userRemoteConfigs: [[url: 'https://github.com/MaheshSalunkhe141777/ETL-Automation.git']],
                    changelog: false 
                ])
            }
        }

        stage('Initialize & Setup') {
            steps {
                echo 'Installing requirements...'
                // Using -m pip is safer on Windows to ensure it hits the right Python version
                bat 'python -m pip install pandas openpyxl pytest'
            }
        }

        stage('Data Validation (Tests)') {
            steps {
                echo 'Running Automation Tests...'
                // Telling pytest to look specifically in the ETL_Project folder
                bat 'python -m pytest ETL_Project/ -v --html=report.html'
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
            // This makes your report.html available to download from the Jenkins UI
            archiveArtifacts artifacts: '*.html', allowEmptyArchive: true
        }
    }
}
