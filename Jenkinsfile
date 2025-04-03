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
                TARGET="/Users/babak/Library/Application Support/Autodesk/Fusion 360/API/Scripts/test/DrawShapesAutoRun"

                echo "📁 Ensuring target directory exists..."
                mkdir -p "$TARGET"

                echo "📦 Copying script files to Fusion API folder..."
                cp DrawShapesAutoRun/DrawShapesAutoRun.py DrawShapesAutoRun/manifest.json "$TARGET/"
                '''
            }
        }

        stage('Done') {
            steps {
                echo "✅ Fusion script deployed to Scripts/test/DrawShapesAutoRun"
            }
        }
    }
}