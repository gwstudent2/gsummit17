#!groovy
// Starting Jenkinsfile for Lab 4

@Library('Utilities2')_
node ('worker_node1') {

   stage('Source') {          

        // Get code from our git repository
	checkout scm
	stash includes: 'api/**, dataaccess/**, util/**, build.gradle, settings.gradle', name: 'testreqs'
   }
  
   stage('Build') {

       gbuild3 'clean compileJava -x test'

   }

stage('Unit Test') {

        parallel (
           tester2: { node ('worker_node2'){
               // always run with a new workspace
               step([$class: 'WsCleanup'])
                 	
               unstash 'testreqs'
	       gbuild3 '-D test.single=TestExample1* :api:test'


            }},
            tester3: { node ('worker_node3'){
                // always run with a new workspace
                step([$class: 'WsCleanup'])

                unstash 'testreqs'
	        gbuild3 '-D test.single=TestExample2* :api:test'   

            }},
        )
    }

    stage('Integration Test') {


// * 1. Insert "withCredentials" step here to wrap the mysql command below

            sh "mysql -u${env.DBUSER} -p${env.DBPASS} registry_test < registry_test.sql"
        

// * 2. Insert command here to run gradle integrationTest task

       
    }
   
   
}
