pipeline {
    agent any
    stages {

       
        stage('Build') {
            steps {
                echo "++++Build Successful++++"
                sh "/usr/bin/python3 unit_test.py"
                
                
            }
        }

        stage('Test') {
            steps {
                echo "++++Test Successful++++"
            }
        }
    }
}