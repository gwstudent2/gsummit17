#!groovy
// starting Jenkinsfile for Lab 1

node ('worker_node1') {
   stage('Source') {          
        // Get code from our git repository
	checkout scm
   }

// * 1. Add build stage below
   stage('Build') {
        sh "'${tool 'gradle32'}/bin/gradle' build -x test"
   }
}
