pipeline {
    agent any
    stages {

       
        stage('Build') {
            steps {
                echo "++++Build Successful++++"
                sh "python3 --version"
                
                
            }
        }

        stage('Test') {
            agent {
                docker { image 'test_call' }
            }
            steps {
                echo "++++Testing Successful++++"
                sh('python3 unit_test.py')
        }
    }
}}