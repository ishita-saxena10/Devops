
pipeline {
    agent {
        docker { image 'python:3.8.15-alpine3.16' }
    }
    stages {

       
        stage('Build') {
            steps {
                echo "++++Build Successful++++"
                sh "python --version"
                
                
                
            }
        }

        stage('Test') {
            
            steps {
                echo "++++Testing Successful++++"
                sh('python unit_test.py')
        }
    }
}}