pipeline {
     agent any
     stages {
         stage('main') {
             steps {
                 sh'serverless deploy --stage prod'
             }
         }  
     }
}
