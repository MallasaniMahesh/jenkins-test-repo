pipeline {
     agent any
     stages {
         stage('dev') {
             steps {
                 sh'serverless deploy --stage '+env.BRANCH_NAME
             }
         }  
     }
}
