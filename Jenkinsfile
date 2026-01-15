pipeline {
    agent any

    environment {
        // Definimos el nombre de la imagen para no repetir código
        IMAGE_NAME = "app-goles-jenkins"
    }

    stages {
        stage('1. Github (Checkout)') {
            steps {
                // Descarga el código del repo configurado
                checkout scm
            }
        }

        stage('2. SonarQube Analysis') {
            steps {
                script {
                    // Aquí es donde se hace el análisis de calidad
                    echo "Iniciando análisis de código en SonarQube..."
                    // Si ya configuraste el server en Jenkins, se usa:
                    // scannerHome = tool 'SonarScanner'
                    // withSonarQubeEnv('SonarQube') { ... }
                }
            }
        }

        stage('3. Construcción Docker (Build)') {
            steps {
                echo "Construyendo imagen Docker: ${IMAGE_NAME}:${BUILD_NUMBER}..."
                sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ."
                sh "docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${IMAGE_NAME}:latest"
            }
        }

        stage('4. Despliegue') {
            steps {
                echo "Desplegando contenedor..."
                // Borramos el contenedor anterior si existe para evitar conflictos de nombre
                sh "docker stop contenedor-goles || true"
                sh "docker rm contenedor-goles || true"
                
                // Arrancamos el nuevo contenedor
                sh "docker run -d --name contenedor-goles -p 5000:5000 ${IMAGE_NAME}:latest"
                echo "Aplicación desplegada en http://localhost:5000"
            }
        }
    }

    post {
        always {
            echo "Limpiando el espacio de trabajo..."
            cleanWs()
        }
    }
}
