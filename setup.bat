@echo off
REM Quick Setup Script for PSO+Zscore Live Trading Deployment

echo ===============================================================
echo    PSO+Zscore Trading Application - Setup for Live Trading
echo ===============================================================
echo.

REM Check for required tools
echo Checking prerequisites...

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo ERROR: Python not found. Please install Python 3.11+
    exit /b 1
)

where node >nul 2>nul
if %errorlevel% neq 0 (
    echo ERROR: Node.js not found. Please install Node.js 18+
    exit /b 1
)

where git >nul 2>nul
if %errorlevel% neq 0 (
    echo ERROR: Git not found. Please install Git
    exit /b 1
)

echo All prerequisites found!
echo.

REM Install Railway CLI if not present
echo Installing Railway CLI...
where railway >nul 2>nul
if %errorlevel% neq 0 (
    npm install -g @railway/cli
    if %errorlevel% neq 0 (
        echo ERROR: Failed to install Railway CLI
        exit /b 1
    )
) else (
    echo Railway CLI already installed
)

REM Install Python dependencies
echo.
echo Installing Python dependencies...
cd backend
pip install -r requirements.txt
pip install colorama pytest pytest-cov
cd ..

REM Set up environment file
echo.
echo Setting up environment configuration...
if not exist backend\.env (
    echo WARNING: backend\.env not found
    echo Please configure your Binance API keys in backend\.env
    echo.
    set /p binance_key="Enter your Binance API Key: "
    set /p binance_secret="Enter your Binance Secret Key: "
    
    REM Update the .env file with actual keys
    powershell -Command "(gc backend\.env) -replace 'your_binance_api_key_here', '%binance_key%' | Out-File backend\.env"
    powershell -Command "(gc backend\.env) -replace 'your_binance_secret_key_here', '%binance_secret%' | Out-File backend\.env"
    
    echo Environment file configured!
)

REM Test local setup
echo.
echo Testing local setup...
cd backend
python -c "import main; print('Backend imports successful!')"
if %errorlevel% neq 0 (
    echo ERROR: Backend setup failed
    exit /b 1
)
cd ..

echo.
echo ===============================================================
echo    Setup Complete!
echo ===============================================================
echo.
echo Next Steps:
echo.
echo 1. Review LIVE_TRADING_CHECKLIST.md
echo 2. Ensure Binance API keys are configured in backend\.env
echo 3. Verify BINANCE_TESTNET=false for live trading
echo 4. Run local test: python backend\main.py
echo 5. Deploy to Railway: deploy.bat
echo.
echo IMPORTANT REMINDERS:
echo - You are configuring for LIVE TRADING (real money)
echo - Start with MICRO capital phase ($100-$1000)
echo - Monitor closely after deployment
echo - Use monitor.py to track performance
echo.
echo Ready to deploy? Run: deploy.bat
echo.
pause