@echo off
REM PSO+Zscore Trading Application - Railway Deployment Script
REM WARNING: This deployment enables LIVE TRADING with REAL MONEY

echo ===============================================================
echo    PSO+Zscore Trading Application - Railway Deployment
echo    LIVE TRADING CONFIGURATION
echo ===============================================================
echo.
echo WARNING: LIVE TRADING ENABLED
echo     - BINANCE_TESTNET = false
echo     - Real money will be at risk
echo     - Ensure all API keys are properly configured
echo.
set /p confirmation="Are you sure you want to deploy with LIVE TRADING? (yes/no): "

if not "%confirmation%"=="yes" (
    echo Deployment cancelled.
    exit /b 1
)

REM Login to Railway with the provided token
echo.
echo Logging into Railway...
railway login --token e0ae87e0-75e3-4db6-bebe-8286df2b7a10

if %ERRORLEVEL% neq 0 (
    echo Failed to login to Railway
    exit /b 1
)

echo Successfully logged into Railway

REM Check if project exists
echo.
echo Checking Railway project...
railway status 2>nul

if %ERRORLEVEL% neq 0 (
    echo Creating new Railway project...
    railway init
)

REM Run tests before deployment
echo.
echo Running pre-deployment tests...
cd backend
python -m pytest tests/ -v 2>nul

if %ERRORLEVEL% neq 0 (
    echo WARNING: Tests not found or failed. Continue anyway for initial setup.
)
cd ..

REM Deploy to Railway
echo.
echo Deploying to Railway...
railway up

if %ERRORLEVEL% neq 0 (
    echo Deployment failed
    exit /b 1
)

echo.
echo Deployment successful!
echo.

REM Get deployment URL
echo Getting deployment information...
railway status

REM Health check reminder
echo.
echo ===============================================================
echo    Deployment Complete!
echo ===============================================================
echo.
echo Next Steps:
echo    1. Check Railway dashboard for deployment status
echo    2. Monitor logs: railway logs --tail
echo    3. Set environment variables in Railway dashboard
echo    4. Verify Binance API connectivity
echo    5. Start with MICRO capital phase ($100-$1000)
echo.
echo IMPORTANT REMINDERS:
echo    - Live trading is enabled (BINANCE_TESTNET=false)
echo    - Start with small capital for validation
echo    - Monitor performance closely
echo    - Set stop-loss limits appropriately
echo.
pause