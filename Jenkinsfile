pipeline {
  agent any

  environment {
    IMAGE_NAME = "abishake98/spartanpy:0." + "$BUILD_NUMBER"
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
          docker.withRegistry('', 'docker_hub_cred'){
            DOCKER_IMAGE.push()
          }
        }
      }
    }
  }
}
