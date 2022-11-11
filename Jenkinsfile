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
                docker { image 'python:3.8.15-alpine3.16' }
            }
            steps {
                echo "++++Testing Successful++++"
                sh('python3 unit_test.py')
        }
    }
}}