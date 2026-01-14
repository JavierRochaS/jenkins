pipeline {
    agent any

    stages {
        stage('1. Descarga de Código') {
            steps {
                checkout scm
            }
        }

        stage('2. Construcción (Build)') {
            steps {
                echo 'Creando imagen de Docker...'
                sh "docker build -t app-goles-jenkins:${env.BUILD_NUMBER} ."
            }
        }

        stage('3. Ejecución (Run)') {
            steps {
                echo 'Iniciando el contenedor para prueba técnica...'
                // Detenemos y borramos cualquier contenedor anterior con el mismo nombre para evitar conflictos
                sh "docker rm -f contenedor-goles || true"
                
                // Ejecutamos el contenedor en modo "detached" (-d) para que Jenkins no se quede trabado
                sh "docker run -d --name contenedor-goles app-goles-jenkins:${env.BUILD_NUMBER}"
            }
        }

        stage('4. Verificación de Logs') {
            steps {
                echo 'Verificando que la App inició correctamente:'
                // Esperamos 5 segundos para que la app cargue y vemos los logs
                sleep 5
                sh "docker logs contenedor-goles"
            }
        }
    }

    post {
        always {
            echo 'Limpieza final: eliminando contenedor de prueba...'
            sh "docker stop contenedor-goles || true"
            sh "docker rm contenedor-goles || true"
            cleanWs()
        }
    }
}
