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
          docker.build 'abishake98/spartanpy'
        }
      }
    }
  }
}
