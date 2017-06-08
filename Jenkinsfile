#!groovy
// starting Jenkinsfile for Lab 5

@Library('Utilities2')_
node ('worker_node1') {
   stage('Source') {          
        // Get code from our git repository
	checkout scm
	stash includes: 'api/**, dataaccess/**, util/**, build.gradle, settings.gradle', name: 'ws-src'
   }
  
   stage('Build') {

      gbuild3 "clean compileJava -x test"
   }
stage('Unit Test') {
        parallel (
           tester2: { node ('worker_node2'){
               // always run with a new workspace
               step([$class: 'WsCleanup'])
                 	
               unstash 'ws-src'
	       gbuild3 '-D test.single=TestExample1* :api:test'


            }},
            tester3: { node ('worker_node3'){
                // always run with a new workspace
                step([$class: 'WsCleanup'])

                unstash 'ws-src'
	        gbuild3 '-D test.single=TestExample2* :api:test'   

            }},

            )
    }
    stage('Integration Test') {
         withCredentials([usernamePassword(credentialsId: 'mysql-access', passwordVariable: 'DBPASS', usernameVariable: 'DBUSER')]) {
            sh "mysql -u${env.DBUSER} -p${env.DBPASS} registry_test < registry_test.sql"
        }
        gbuild3 'integrationTest' 
    }
    stage('Analysis') {
        withSonarQubeEnv('Local SonarQube') {

// * 1. Insert command to invoke sonarqube scan
		sh "/usr/share/gradle/bin/gradle sonarqube"

        
              //  timeout(time:5, unit:'MINUTES') {

// * 2. Complete the command to wait for the quality gate 

                    def qg = waitForQualityGate()
                    if (qg.status != 'OK') {
                      error "Pipeline aborted due to quality gate failure: ${qg.status}"
                    }
		// }
               
        }
        step([$class: 'JacocoPublisher',
            execPattern:'**/**.exec',
            classPattern: '**/classes/main/com/demo/util,**/classes/main/com/demo/dao',
            sourcePattern: '**/src/main/java/com/demo/util,**/src/main/java/com/demo/dao',
            exclusionPattern: '**/*Test*.class'])

      
    }
    stage('Assemble') {
       def workspace = env.WORKSPACE
       def setPropertiesProc = fileLoader.fromGit('jenkins/pipeline/updateGradleProperties', 
	       'https://github.com/brentlaster/utilities.git', 'master', null, '')

       setPropertiesProc.updateGradleProperties("${workspace}/gradle.properties",
	        "${userInput.MAJOR_VERSION}",
	        "${userInput.MINOR_VERSION}",
	        "${userInput.PATCH_VERSION}",
	        "${userInput.BUILD_STAGE}")
        
            gbuild3 "-x test build assemble"
    }
    stage('Publish Artifacts'){
        def  server = Artifactory.server "LocalArtifactory"
        def artifactoryGradle = Artifactory.newGradleBuild()
        artifactoryGradle.tool = "gradle3"
        artifactoryGradle.deployer repo:'libs-snapshot-local', server: server
        artifactoryGradle.resolver repo:'remote-repos', server: server
        
        def buildInfo = Artifactory.newBuildInfo()
        buildInfo.env.capture = true
        artifactoryGradle.deployer.deployMavenDescriptors = true
        artifactoryGradle.deployer.artifactDeploymentPatterns.addExclude("*.jar")
        artifactoryGradle.usesPlugin = false 

        // 3. Complete the command to do a clean and artifactory publish

        artifactoryGradle.run rootDir: "/", buildFile: 'build.gradle', tasks: 'clean artifactoryPublish' , buildInfo: buildInfo
        server.publishBuildInfo buildInfo

    }
    stage('Retrieve Latest Artifact') {
        def getLatestScript = libraryResource 'ws-get-latest.sh' 
        sh getLatestScript
        stash includes:'*.war', name: 'latest-warfile'
    }
   
}
