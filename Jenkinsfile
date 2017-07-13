#!groovy
pipeline {
    agent{ label 'worker_node1'}
    libraries {
       lib('Utilities2')
   }
   stages {
      stage('Source') {
         steps {
            step([$class: 'WsCleanup'])
            checkout scm
            stash name: 'test-sources', includes: 'build.gradle,src/test/'
       }
    }
    stage('Build') {
         // Run the gradle build
         steps {
             gbuild3 'clean build -x test'
         }
      }
      stage ('Test') {
          // execute required unit tests in parallel
          steps {
               parallel (
                   worker2: { node ('worker_node2'){
                        // always run with a new workspace
                       step([$class: 'WsCleanup'])
	         unstash 'test-sources'
	         gbuild3 '-D test.single=TestExample1* :api:test'
                   }},
                  worker3: { node ('worker_node3'){
                      // always run with a new workspace
                     step([$class: 'WsCleanup'])
                     unstash 'test-sources'
  	       gbuild3 '-D test.single=TestExample2* :api:test'
                   }},
              )
         } 
      } 
  } // end stages
  post {
       always {
          echo "Build stage complete"
       }
       failure{
          echo "Build failed"
          mail body: 'build failed', subject: 'Build failed!', to: '<your email address>'
       }
       success {
           echo "Build succeeded"
           mail body: 'build succeeded', subject: 'Build Succeeded', to: '<your email address>'
      }
   }
} // end pipeline

