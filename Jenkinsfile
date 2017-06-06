#!groovy
// starting Jenkins file for Lab 2

// * 1. Add Library annotation here

node ('worker_node1') {
   stage('Source') {          
        // Get code from our git repository    
         checkout scm
   }
  
   stage('Build') {

// * 2. modify step below to use shared-library gbuild3 routine

      sh "${tool 'gradle3'}/bin/gradle clean compileJava -x test"
   }
   
}
