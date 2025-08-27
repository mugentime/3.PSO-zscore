#!/bin/bash

# PSO+Zscore Trading Application - Railway Deployment Script
# ⚠️ WARNING: This deployment enables LIVE TRADING with REAL MONEY

echo "═══════════════════════════════════════════════════════════════"
echo "   PSO+Zscore Trading Application - Railway Deployment"
echo "   LIVE TRADING CONFIGURATION"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "⚠️  WARNING: LIVE TRADING ENABLED"
echo "    - BINANCE_TESTNET = false"
echo "    - Real money will be at risk"
echo "    - Ensure all API keys are properly configured"
echo ""
read -p "Are you sure you want to deploy with LIVE TRADING? (yes/no): " confirmation

if [ "$confirmation" != "yes" ]; then
    echo "Deployment cancelled."
    exit 1
fi

# Login to Railway with the provided token
echo ""
echo "🔐 Logging into Railway..."
railway login --token e0ae87e0-75e3-4db6-bebe-8286df2b7a10

if [ $? -ne 0 ]; then
    echo "❌ Failed to login to Railway"
    exit 1
fi

echo "✅ Successfully logged into Railway"

# Check if project exists or create new one
echo ""
echo "📦 Checking Railway project..."
railway status 2>/dev/null

if [ $? -ne 0 ]; then
    echo "Creating new Railway project..."
    railway init
fi

# Run tests before deployment
echo ""
echo "🧪 Running pre-deployment tests..."
cd backend
python -m pytest tests/ -v

if [ $? -ne 0 ]; then
    echo "❌ Tests failed. Fix issues before deploying."
    exit 1
fi
cd ..

echo "✅ All tests passed"

# Deploy to Railway
echo ""
echo "🚀 Deploying to Railway..."
railway up

if [ $? -ne 0 ]; then
    echo "❌ Deployment failed"
    exit 1
fi

echo ""
echo "✅ Deployment successful!"
echo ""

# Get deployment URL
echo "📌 Getting deployment information..."
railway status

# Show deployment URL
echo ""
echo "🌐 Your application is deployed!"
echo "   Check your application at the Railway dashboard:"
echo "   https://railway.app/dashboard"
echo ""

# Health check
echo "🏥 Running health check..."
APP_URL=$(railway variables get RAILWAY_STATIC_URL 2>/dev/null)

if [ ! -z "$APP_URL" ]; then
    sleep 5
    curl -s "${APP_URL}/health/" | python -m json.tool
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ Health check passed!"
    else
        echo ""
        echo "⚠️  Health check failed or pending. Check Railway logs."
    fi
fi

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "   Deployment Complete!"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "📊 Next Steps:"
echo "   1. Check Railway dashboard for deployment status"
echo "   2. Monitor logs: railway logs --tail"
echo "   3. Set environment variables in Railway dashboard"
echo "   4. Verify Binance API connectivity"
echo "   5. Start with MICRO capital phase ($100-$1000)"
echo ""
echo "⚠️  IMPORTANT REMINDERS:"
echo "   - Live trading is enabled (BINANCE_TESTNET=false)"
echo "   - Start with small capital for validation"
echo "   - Monitor performance closely"
echo "   - Set stop-loss limits appropriately"
echo ""