pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            steps {
                sh 'python3 -m py_compile short.py test-short.py'
                stash(name: 'compiled-results', includes: '*.py*')
            }
        }
        stage('Test') { 
            steps {
                
                sh 'python3 -m pytest --junit-xml test-reports/results.xml test-short.py' 
            }
            post {
                always {
                    junit 'test-reports/results.xml' 
                }
            }
        }
        stage('Deliver') { 
            steps {   
                sh 'python3 -m PyInstaller -v'
                sh 'python3 -m PyInstaller short.py'
            }
            
        }
        
    }
}
