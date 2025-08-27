@echo off
echo ==================================================
echo PSO+Zscore LIVE TRADING Deployment
echo ==================================================
echo.

cd /d C:\Users\je2al\Desktop\3.PSO-zscore

echo Setting Railway Token...
set RAILWAY_TOKEN=e0ae87e0-75e3-4db6-bebe-8286df2b7a10

echo.
echo Deploying to Railway...
railway up

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo If deployment failed, please:
    echo 1. Login to Railway: railway login
    echo 2. Link your project: railway link
    echo 3. Run this script again
    pause
    exit /b 1
)

echo.
echo Deployment initiated!
echo.
echo Checking status...
railway status

echo.
echo View logs with: railway logs
echo.
pause