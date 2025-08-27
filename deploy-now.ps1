# PSO+Zscore Live Trading Deployment Script
Set-Location "C:\Users\je2al\Desktop\3.PSO-zscore"

# Set Railway Token
$env:RAILWAY_TOKEN = "e0ae87e0-75e3-4db6-bebe-8286df2b7a10"

Write-Host "Deploying PSO+Zscore Trading Application..." -ForegroundColor Cyan
Write-Host "LIVE TRADING ENABLED - BINANCE_TESTNET=false" -ForegroundColor Yellow

# Try to deploy
railway up

if ($LASTEXITCODE -ne 0) {
    Write-Host "Deployment requires project linking. Running railway init..." -ForegroundColor Yellow
    railway init
    railway up
}

Write-Host "Checking deployment status..." -ForegroundColor Green
railway status

Write-Host "Getting logs..." -ForegroundColor Green
railway logs --tail 20