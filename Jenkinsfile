pipeline {
    agent any

    environment {
        // Nombre de la imagen Docker que vamos a crear
        IMAGE_NAME = "app-goles-jenkins"
    }

    stages {
        stage('1. Github (Checkout)') {
            steps {
                // Descarga el código del repositorio
                checkout scm
            }
        }

        stage('2. SonarQube Analysis') {
            steps {
                // "Sonarqube" debe coincidir con el nombre en Jenkins > System (tu Imagen 2)
                withSonarQubeEnv('Sonarqube') { 
                    script {
                        // Busca la herramienta configurada en Jenkins > Tools
                        def scannerHome = tool 'sonar-scanner' 
                        
                        // Forzamos el uso del token en el comando para evitar el error de "Not Authorized"
                        sh "${scannerHome}/bin/sonar-scanner " +
                           "-Dsonar.projectKey=proyecto-goles-python " +
                           "-Dsonar.sources=. " +
                           "-Dsonar.language=py"
                    }
                }
            }
        }

        stage('3. Construcción Docker (Build)') {
            steps {
                echo "Construyendo imagen: ${IMAGE_NAME}:${BUILD_NUMBER}..."
                sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ."
                sh "docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${IMAGE_NAME}:latest"
            }
        }

        stage('4. Despliegue') {
            steps {
                echo "Desplegando contenedor..."
                // Limpieza de contenedores previos para evitar errores de nombre ocupado
                sh "docker stop contenedor-goles || true"
                sh "docker rm contenedor-goles || true"
                
                // Ejecución del nuevo contenedor
                sh "docker run -d --name contenedor-goles -p 5000:5000 ${IMAGE_NAME}:latest"
                echo "Aplicación disponible en http://localhost:5000"
            }
        }
    }

    post {
        always {
            // Limpia el workspace al finalizar
            cleanWs()
        }
    }
}
