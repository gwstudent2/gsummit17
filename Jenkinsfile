#!groovy
// starting Jenkins file for Lab 2

// * 1. Add Library annotation here
@Library('Utilities2')_
node ('worker_node1') {
   stage('Pull Source') {          
        // Get code from our git repository    
         checkout scm
   }
  
   stage('Compile') {

// * 2. modify step below to use shared-library gbuild3 routine

      gbuild3 'clean compileJava -x test"
   }
   
}
