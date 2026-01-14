pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Jenkins descarga el código de GitHub automáticamente
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                echo 'Construyendo la imagen desde el código de GitHub...'
                sh "docker build -t app-goles-jenkins:${env.BUILD_NUMBER} ."
            }
        }

        stage('Validación') {
            steps {
                sh "docker images | grep app-goles-jenkins"
            }
        }
    }
    
    post {
        always {
            echo 'Limpiando espacio de trabajo...'
            cleanWs()
        }
    }
}
