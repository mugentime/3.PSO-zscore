@echo off
REM PSO+Zscore Trading Application - Quick Start Script for Windows

echo 🚀 Starting PSO+Zscore Trading Application...

REM Check if we're in the correct directory
if not exist "README.md" goto :wrong_dir
if not exist "backend" goto :wrong_dir

echo 🔧 Setting up backend environment...
cd backend

REM Create .env file if it doesn't exist
if not exist ".env" (
    echo 📝 Creating .env file from template...
    copy .env.example .env
    echo ⚠️  Please update .env with your actual API keys
)

REM Install Python dependencies
echo 📦 Installing Python dependencies...
pip install -r requirements.txt

REM Start backend server
echo 🔥 Starting FastAPI backend server...
start "PSO+Zscore Backend" python main.py

REM Wait for backend to start
timeout /t 5

REM Test backend health
echo 🔍 Testing backend health...
curl -f http://localhost:8003/health/ >nul 2>&1
if errorlevel 1 (
    echo ❌ Backend health check failed
    exit /b 1
) else (
    echo ✅ Backend is healthy!
)

REM Check if frontend exists and has dependencies
cd ..\frontend
if exist "package.json" (
    echo 📦 Installing frontend dependencies...
    call npm install
    
    echo 🎨 Starting React frontend...
    start "PSO+Zscore Frontend" npm start
    
    echo ✅ Application started successfully!
    echo 🌐 Frontend: http://localhost:3000
    echo 🔗 Backend API: http://localhost:8003
    echo 📚 API Docs: http://localhost:8003/docs
) else (
    echo 📝 Frontend not fully set up yet. Backend running at http://localhost:8003
    echo 🔗 API Docs: http://localhost:8003/docs
)

echo 🔧 Press any key to stop services and exit...
pause >nul

REM Kill backend process (simplified - in production use proper process management)
taskkill /f /im python.exe /fi "WINDOWTITLE eq PSO+Zscore Backend" 2>nul
taskkill /f /im node.exe /fi "WINDOWTITLE eq PSO+Zscore Frontend" 2>nul

echo 🛑 Services stopped.
exit /b 0

:wrong_dir
echo ❌ Please run this script from the project root directory
pause
exit /b 1