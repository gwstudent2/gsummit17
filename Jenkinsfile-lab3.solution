#!groovy
// Completed Jenkinsfile for Lab 3

@Library('Utilities2')_
node ('worker_node1') {

   stage('Source') {          

        // Get code from our git repository
	checkout scm

// 1. Add the stash step here from the Snippet Generator

	stash includes: 'api/**, dataaccess/**, util/**, build.gradle, settings.gradle', name: 'ws-src'
   }
  
   stage('Build') {

       gbuild3 'clean compileJava -x test'

   }

stage('Unit Test') {

        parallel (
           tester2: { node ('worker_node2'){
               // always run with a new workspace
               step([$class: 'WsCleanup'])

// * 2. Add commands here to unstash from the stash we created in the Source stage
//      Add a command to use the shared library gradle routine to test the api test cases named TestExample1* 
                 	
               unstash 'ws-src'
	       gbuild3 '-D test.single=TestExample1* :api:test'


            }},
            tester3: { node ('worker_node3'){
                // always run with a new workspace
                step([$class: 'WsCleanup'])

// * 3. Add commands here to unstash from the stash we created in the Source stage
//      Add a command to use the shared library gradle routine to test the api test cases named TestExample2* 

                unstash 'ws-src'
	        gbuild3 '-D test.single=TestExample2* :api:test'   

            }},
        )
    }
  
}
