pipeline {
    agent any

    stages {
        stage('Get repository') {
            steps {
                // Get code from repository
                git url: 'https://github.com/frankachu/ci_tests.git', branch: 'main'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Create venv and install dependencies
                sh '''
                   python3 -m venv venv
                   . venv/bin/activate
                   ./venv/bin/pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                // Activate venv and run pytest
                sh '''
                    . venv/bin/activate
                    ./venv/bin/pytest test_app.py
                '''
            }
        }
    }
    post {
        always {
            // Send anyway
            echo 'Pipeline finished.'
        }
        success {
            echo 'All tests passed!'
        }
        failure {
            echo 'Some tests failed.'
        }
    }
}