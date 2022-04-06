pipeline {
  agent any

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
          DOCKER_IMAGE = docker.build 'abishake98/spartanpy'
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
