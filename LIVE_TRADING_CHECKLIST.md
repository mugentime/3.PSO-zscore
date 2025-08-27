# 🚨 PSO+Zscore Live Trading Safety Checklist

## ⚠️ CRITICAL: You are about to enable LIVE TRADING with REAL MONEY

### Pre-Deployment Checklist

#### 1. API Configuration
- [ ] Binance API Key is set and valid
- [ ] Binance Secret Key is set and valid
- [ ] API permissions are correctly configured (Trading enabled)
- [ ] IP whitelist is configured (if using)
- [ ] **BINANCE_TESTNET=false** is intentional

#### 2. Risk Management Settings
- [ ] MAX_RISK_PER_TRADE is set (recommended: 2% or less)
- [ ] Stop-loss percentages are configured
- [ ] Daily loss limits are set
- [ ] Position sizing is configured
- [ ] Capital phase is set to MICRO ($100-$1000)

#### 3. Capital Deployment
- [ ] Starting with MICRO capital phase ($100-$1000)
- [ ] Understand the capital scaling phases:
  - MICRO: $100 - $1,000
  - SMALL: $1,000 - $10,000
  - MEDIUM: $10,000 - $100,000
  - FULL: $100,000+
- [ ] Initial capital amount is set appropriately
- [ ] Prepared for potential losses

#### 4. System Testing
- [ ] Backtesting completed with positive results
- [ ] Paper trading tested on testnet
- [ ] All unit tests pass
- [ ] Health checks are working
- [ ] Monitoring systems are active

#### 5. Railway Configuration
- [ ] Railway token is valid: `e0ae87e0-75e3-4db6-bebe-8286df2b7a10`
- [ ] Railway API key is set: `00a98eb4-3969-4e8e-8b0f-c333090ac1d1`
- [ ] Environment variables are set in Railway dashboard
- [ ] GitHub secrets are configured

#### 6. Security
- [ ] No API keys in code or public repositories
- [ ] Using encrypted connections
- [ ] Non-root user in Docker container
- [ ] Rate limiting enabled
- [ ] Security headers configured

#### 7. Monitoring & Alerts
- [ ] Health check endpoint working
- [ ] Logging configured
- [ ] Error tracking set up (Sentry optional)
- [ ] Email/Slack alerts configured
- [ ] Performance metrics accessible

#### 8. Trading Strategy
- [ ] Z-Score thresholds tested and validated
- [ ] PSO optimization parameters tuned
- [ ] Correlation thresholds appropriate
- [ ] Lookback periods validated
- [ ] Strategy performs well in different market conditions

#### 9. Emergency Procedures
- [ ] Know how to stop trading immediately
- [ ] Railway rollback procedure understood
- [ ] Contact information for support ready
- [ ] Backup of all configurations

#### 10. Legal & Compliance
- [ ] Understand tax implications of trading
- [ ] Comply with local regulations
- [ ] Keep records of all trades
- [ ] Understand exchange terms of service

---

## 🚀 Deployment Commands

### Local Testing First
```bash
# Test locally with testnet
cd backend
python main.py

# Run monitoring
python monitor.py loop 60
```

### Deploy to Railway
```bash
# Windows
deploy.bat

# Linux/Mac
./deploy.sh

# Or manually
railway login --token e0ae87e0-75e3-4db6-bebe-8286df2b7a10
railway up
railway logs --tail
```

### Post-Deployment Verification
```bash
# Check deployment status
railway status

# Monitor logs
railway logs --tail

# Run health check
python monitor.py deployment
```

---

## 🛑 Emergency Stop Procedures

### 1. Immediate Trading Halt
```bash
# Set in Railway dashboard immediately:
TRADING_ENABLED=false
AUTO_TRADING_ENABLED=false
```

### 2. Rollback Deployment
```bash
railway rollback
```

### 3. Scale to Zero
```bash
railway scale 0
```

---

## 📊 Monitoring URLs

- Railway Dashboard: https://railway.app/dashboard
- Application Logs: `railway logs --tail`
- Health Check: `https://your-app.railway.app/health/`
- Metrics: `https://your-app.railway.app/api/metrics`

---

## ⚡ Quick Reference

### Environment Variables to Set in Railway
```
BINANCE_API_KEY=your_actual_api_key
BINANCE_SECRET_KEY=your_actual_secret_key
BINANCE_TESTNET=false
CAPITAL_PHASE=MICRO
INITIAL_CAPITAL=1000
TRADING_ENABLED=true
AUTO_TRADING_ENABLED=false
```

### Critical Commands
```bash
# Deploy
railway up

# Monitor
railway logs --tail

# Stop
railway scale 0

# Rollback
railway rollback
```

---

## 📝 Final Confirmation

**By proceeding with deployment where BINANCE_TESTNET=false:**

- ✅ I understand this enables LIVE TRADING
- ✅ I understand REAL MONEY is at risk
- ✅ I have completed all checklist items above
- ✅ I am starting with MICRO capital ($100-$1000)
- ✅ I will monitor the system closely
- ✅ I understand how to stop trading immediately if needed

---

**Deployment Date:** _______________
**Deployed By:** _______________
**Initial Capital:** $_______________
**Risk Tolerance:** _______________

---

⚠️ **REMEMBER:** Start small, monitor closely, and scale gradually based on proven performance.