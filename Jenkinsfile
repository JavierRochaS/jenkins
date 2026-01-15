pipeline {
    agent any

    environment {
        // Nombre de la imagen para organizar mejor el código
        IMAGE_NAME = "app-goles-jenkins"
    }

    stages {
        stage('1. Github (Checkout)') {
            steps {
                // Descarga el código fuente desde el repositorio
                checkout scm
            }
        }

        stage('2. SonarQube Analysis') {
            steps {
                // "Sonarqube" debe ser idéntico al nombre que pusiste en Jenkins -> System
                withSonarQubeEnv('Sonarqube') { 
                    script {
                        // Busca la herramienta configurada en Jenkins -> Tools
                        def scannerHome = tool 'sonar-scanner' 
                        
                        // Ejecuta el análisis real del código
                        sh "${scannerHome}/bin/sonar-scanner " +
                           "-Dsonar.projectKey=proyecto-goles-python " +
                           "-Dsonar.sources=. " +
                           "-Dsonar.python.version=3"
                    }
                }
            }
        }

        stage('3. Construcción Docker (Build)') {
            steps {
                echo "Construyendo imagen: ${IMAGE_NAME}:${BUILD_NUMBER}..."
                // Construye la imagen usando el Dockerfile del repositorio
                sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ."
                // Etiqueta también como 'latest' para facilitar el despliegue
                sh "docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${IMAGE_NAME}:latest"
            }
        }

        stage('4. Despliegue') {
            steps {
                echo "Iniciando despliegue del contenedor..."
                // Detenemos y eliminamos el contenedor anterior si existe para evitar conflictos
                sh "docker stop contenedor-goles || true"
                sh "docker rm contenedor-goles || true"
                
                // Lanzamos el nuevo contenedor en el puerto 5000 (ajústalo si tu app usa otro)
                sh "docker run -d --name contenedor-goles -p 5000:5000 ${IMAGE_NAME}:latest"
                echo "¡Despliegue completado con éxito!"
            }
        }
    }

    post {
        always {
            // Limpia el espacio de trabajo para no dejar archivos temporales
            cleanWs()
        }
    }
}
