pipeline {
     agent any
     stages {
         stage('dev') {
             steps {
                 sh'serverless deploy --stage '+env.BRANCH_NAME +'--region us-east-1'
             }
         }  
     }
}
