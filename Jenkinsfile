pipeline {
  agent any

  environment {
    IMAGE_NAME = "abishake98/spartanpy:0." + "$BUILD_NUMBER"
    DOCKER_CREDENTIALS = 'docker_hub_cred'
  }

  stages {
    stage('Cloning the project from GitHub'){
          steps {
            checkout([
                $class: 'GitSCM', branches: [[name: '*/main']],
                serRemoteConfigs: [[
                  url: 'git@github.com:abishake98/spartanpy.git',
                  credentialsId: 'ssh_git_cred'
                ]]
              ])
          }
        }

    stage('Build Docker Image'){
      steps {
        script {
          DOCKER_IMAGE = docker.build IMAGE_NAME
        }
      }
    }

    stage('Push to Docker Hub'){
      steps {
        script {
          docker.withRegistry('', DOCKER_CREDENTIALS){
            DOCKER_IMAGE.push()
          }
        }
      }
    }

    stage('Removing the Docker Image'){
      steps {
        sh "docker rmi $IMAGE_NAME"
      }
    }
  }
}
