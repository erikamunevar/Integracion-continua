pipeline {
    agent any

    stages {

        stage('Clonar Repositorio') {
    steps {
        git branch: 'main',
            url: 'https://github.com/erikamunevar/Integracion-continua.git'
            }
        }

        stage('Verificar Archivos') {
            steps {
                echo 'Validando proyecto'
            }
        }

        stage('Construcción') {
            steps {
                echo 'Construcción exitosa'
            }
        }

        stage('Despliegue') {
            steps {
                echo 'Despliegue completado'
            }
        }
    }
}
