@echo off
cd /d C:\Users\je2al\Desktop\3.PSO-zscore

echo Deploying PSO+Zscore with LIVE TRADING...
railway link
railway up --detach

echo.
echo Deployment started!
echo Check status with: railway status
echo View logs with: railway logs
pause