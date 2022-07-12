pipeline {
     agent any
     stages {
         stage('main') {
             steps {
                 sh'serverless deploy --stage prod'
             }
         }  
         stage('dev'){
             steps{
                 sh'serverless deploy --stage dev'
             }
         }
     }
}
