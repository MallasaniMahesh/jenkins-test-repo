pipeline {
     agent any
     stages {
         stage('dev') {
             steps {
                 sh'serverless deploy --region us-east-1 --stage prod'
             }
         }  
     }
}
