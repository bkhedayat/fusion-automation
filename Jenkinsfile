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
                TARGET="$HOME/Library/Application Support/Autodesk/Fusion 360/API/AddIns/DrawShapesAutoRun"
                echo "📁 Ensuring target directory exists..."
                mkdir -p "$TARGET"
                echo "📦 Copying script files to Add-In folder..."
                cp DrawShapesAutoRun.py manifest.json "$TARGET/"
                '''
            }
        }

        stage('Done') {
            steps {
                echo "✅ Fusion Add-In deployed. Restart Fusion to auto-run."
            }
        }
    }
}