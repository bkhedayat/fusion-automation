pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                echo "🔄 Cloning repository..."
                checkout scm
            }
        }

        stage('Run Fusion Script Deployment') {
            steps {
                echo "🚀 Deploying Fusion 360 script..."
                sh '''
                mkdir -p "$HOME/Library/Application Support/Autodesk/webdeploy/production/YOUR_ADDIN_FOLDER/DrawShapesAutoRun"
                cp DrawShapesAutoRun/* "$HOME/Library/Application Support/Autodesk/Autodesk Fusion 360/API/Scripts/test/DrawShapesAutoRun/"
                '''
            }
        }

        stage('Done') {
            steps {
                echo "✅ Script deployed! Launch Fusion 360 to run."
            }
        }
    }
}