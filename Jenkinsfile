pipeline {
     agent any
     stages {
         stage('dev') {
             steps {
                 sh'serverless deploy --region us-east-1 --stage '+env.BRANCH_NAME
             }
         }  
     }
}
