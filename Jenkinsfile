#!groovy
// starting Jenkins file for Lab 3

@Library('Utilities2')_
node ('worker_node1') {
   stage('Source') {          
        // Get code from our git repository
	checkout scm

// * 1. Add stash step here

   }
  
   stage('Build') {

      gbuild3 "clean compileJava -x test"
   }

stage('Unit Test') {
        parallel (
            tester2: { node ('worker_node2'){
               // always run with a new workspace
               step([$class: 'WsCleanup'])
               
// * 2. Add commands here to unstash and do gradle tests for TestExample1*               

            }},
            tester3: { node ('worker_node2'){
                // always run with a new workspace
                step([$class: 'WsCleanup'])

// * 3. Add commands here to unstash and do gradle tests for TestExample2*
                

            }},

            )
            
    }
   
}
