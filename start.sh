#!/bin/bash

# PSO+Zscore Trading Application - Quick Start Script

echo "🚀 Starting PSO+Zscore Trading Application..."

# Check if Railway CLI is installed
if ! command -v railway &> /dev/null; then
    echo "📥 Installing Railway CLI..."
    curl -fsSL https://railway.app/install.sh | sh
    export PATH="$HOME/.railway/bin:$PATH"
fi

# Check if we're in the correct directory
if [ ! -f "README.md" ] || [ ! -d "backend" ]; then
    echo "❌ Please run this script from the project root directory"
    exit 1
fi

echo "🔧 Setting up backend environment..."
cd backend

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "📝 Creating .env file from template..."
    cp .env.example .env
    echo "⚠️  Please update .env with your actual API keys"
fi

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Start backend server
echo "🔥 Starting FastAPI backend server..."
python main.py &
BACKEND_PID=$!

# Wait for backend to start
sleep 5

# Test backend health
echo "🔍 Testing backend health..."
if curl -f http://localhost:8003/health/ > /dev/null 2>&1; then
    echo "✅ Backend is healthy!"
else
    echo "❌ Backend health check failed"
    kill $BACKEND_PID
    exit 1
fi

# Check if frontend exists and has dependencies
cd ../frontend
if [ -f "package.json" ]; then
    echo "📦 Installing frontend dependencies..."
    npm install
    
    echo "🎨 Starting React frontend..."
    npm start &
    FRONTEND_PID=$!
    
    echo "✅ Application started successfully!"
    echo "🌐 Frontend: http://localhost:3000"
    echo "🔗 Backend API: http://localhost:8003"
    echo "📚 API Docs: http://localhost:8003/docs"
    
    # Keep script running
    echo "🔧 Press Ctrl+C to stop all services"
    trap "echo '🛑 Stopping services...'; kill $BACKEND_PID $FRONTEND_PID; exit" SIGINT
    wait
else
    echo "📝 Frontend not fully set up yet. Backend running at http://localhost:8003"
    echo "🔧 Press Ctrl+C to stop backend"
    trap "echo '🛑 Stopping backend...'; kill $BACKEND_PID; exit" SIGINT
    wait $BACKEND_PID
fi