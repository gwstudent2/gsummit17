#!groovy
// Starting Jenkinsfile for Lab 2

// * 1. Add the annotation here to load our shared library 'Utilities2' 


node ('worker_node1') {

   stage('Source') {          

        // Get code from our git repository
	checkout scm
	
   }
  
   stage('Build') {

// * 2. Modify the gradle build command below to use our 'gbuild3' shared library routine 
       sh "'${tool 'gradle3'}/bin/gradle' clean compileJava -x test"

   }


}
