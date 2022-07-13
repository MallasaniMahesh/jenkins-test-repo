pipeline {
     agent any
     stages {
         stage(env.BRANCH_NAME) {
             steps {
                 sh'serverless deploy --stage '+env.BRANCH_NAME
             }
         }  
     }
}
