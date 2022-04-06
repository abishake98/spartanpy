pipeline {
  agent any

  environment {
    IMAGE_NAME = "abishake98/spartanpy:0." + "$BUILD_NUMBER"
    DOCKER_CREDENTIALS = 'docker_hub_cred'
  }

  stages {
    stage('Cloning the project '){
      steps {
        git branch: 'main',
        url: 'https://github.com/abishake98/spartanpy.git'
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
  }
}
