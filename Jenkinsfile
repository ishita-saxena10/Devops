pipeline {
    agent any
    stages {

       
        stage('Build') {
            steps {
                echo "++++Build Successful++++"
                sh "/usr/bin/python3 --version"
                
                
            }
        }

        stage('Test') {
            agent {
                docker { image 'test_call' }
            }
            steps {
                echo "++++Testing Successful++++"
                sh('python3 Calculator.py')
        }
    }
}}