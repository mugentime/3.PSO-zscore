# 🚂 Railway Deployment Guide - PSO+Zscore Trading App

## 🎯 Quick Railway Deployment

### Prerequisites
- Railway CLI installed: `curl -fsSL https://railway.app/install.sh | sh`
- Railway account created at [railway.app](https://railway.app)
- GitHub repository: `mugentime/3.PSO-zscore`

### 🚀 One-Click Deployment Steps

#### 1. Login to Railway
```bash
railway login --token e0ae87e0-75e3-4db6-bebe-8286df2b7a10
```

#### 2. Initialize Railway Project
```bash
cd C:\Users\je2al\Desktop\3.PSO-zscore
railway init
```

#### 3. Connect to GitHub Repository
```bash
railway connect mugentime/3.PSO-zscore
```

#### 4. Set Environment Variables
```bash
# Core application settings
railway variables set DEBUG=false
railway variables set LOG_LEVEL=INFO
railway variables set SECRET_KEY="your-production-secret-key"

# Binance API (start with testnet)
railway variables set BINANCE_TESTNET=true
railway variables set BINANCE_API_KEY="your-binance-api-key"
railway variables set BINANCE_SECRET_KEY="your-binance-secret-key"

# Trading configuration
railway variables set MAX_RISK_PER_TRADE=0.02
railway variables set MICRO_CAPITAL_MIN=100.0
railway variables set MICRO_CAPITAL_MAX=1000.0
```

#### 5. Deploy Application
```bash
railway up
```

#### 6. Check Deployment Status
```bash
railway status
railway logs
```

### 🌐 Railway UI Dashboard Setup

#### Access Railway Dashboard
1. Go to [railway.app/dashboard](https://railway.app/dashboard)
2. Find your "3.PSO-zscore" project
3. Click to view deployment details

#### Configure Auto-Deploy from GitHub
1. **Settings** → **Source**
2. Connect GitHub repository: `mugentime/3.PSO-zscore`
3. **Branch**: `master`
4. **Auto-deploy**: ✅ Enable
5. **Root Directory**: `/backend` (if needed)

#### Environment Variables in UI
```
Settings → Variables → Add Variables:

# Application
DEBUG = false
LOG_LEVEL = INFO
SECRET_KEY = your-production-secret-key-here
PORT = 8003

# Database (Railway will provide PostgreSQL URL)
DATABASE_URL = ${{Postgres.DATABASE_URL}}

# Binance API
BINANCE_TESTNET = true
BINANCE_API_KEY = your-binance-api-key
BINANCE_SECRET_KEY = your-binance-secret-key

# Trading
MAX_RISK_PER_TRADE = 0.02
MICRO_CAPITAL_MIN = 100.0
MICRO_CAPITAL_MAX = 1000.0
```

### 🗄️ Database Setup

#### Add PostgreSQL Database
1. **Dashboard** → **Add Service** → **Database** → **PostgreSQL**
2. Railway will automatically provide `DATABASE_URL`
3. Update `backend/app/config.py` to use PostgreSQL:

```python
# In production, use Railway's PostgreSQL
DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./trading.db")
```

#### Database Migration (if needed)
```bash
# SSH into Railway container
railway shell

# Run migrations
python -c "from app.database import engine, Base; Base.metadata.create_all(bind=engine)"
```

### 📊 Monitoring & Health Checks

#### Health Check Endpoints
```bash
# Basic health check
curl https://your-app.railway.app/health/

# Detailed system metrics
curl https://your-app.railway.app/health/detailed

# Component status
curl https://your-app.railway.app/debug/component-status

# API documentation
https://your-app.railway.app/docs
```

#### Railway Metrics
- **CPU Usage**: Monitor in Railway dashboard
- **Memory**: Track memory consumption
- **Network**: Bandwidth usage
- **Logs**: Real-time application logs

### 🔐 Security Configuration

#### Production Security Checklist
```bash
# Generate secure secret key
python -c "import secrets; print(secrets.token_urlsafe(32))"

# Set production environment variables
railway variables set SECRET_KEY="generated-secure-key"
railway variables set DEBUG=false
railway variables set BINANCE_TESTNET=true  # Start with testnet
```

#### CORS Configuration
The FastAPI app is configured with CORS for Railway:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://*.railway.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 🚀 Deployment Workflows

#### Manual Deployment
```bash
# Deploy current branch
railway up

# Deploy specific branch  
railway up --branch main

# Deploy with specific service
railway up --service backend
```

#### Automatic GitHub Deployment
- **Push to master** → Automatic deployment
- **Pull Request** → Preview deployment (if enabled)
- **GitHub Actions** → Full CI/CD pipeline

### 🔍 Debug & Troubleshooting

#### Common Issues & Solutions

**1. Build Failures**
```bash
# Check build logs
railway logs --deployment

# Verify Dockerfile
cat backend/Dockerfile

# Test locally
docker build -f backend/Dockerfile -t pso-zscore .
```

**2. Environment Variable Issues**
```bash
# List all variables
railway variables

# Check specific variable
railway variables get BINANCE_API_KEY

# Update variable
railway variables set BINANCE_API_KEY="new-value"
```

**3. Database Connection Issues**
```bash
# Check database URL
railway variables get DATABASE_URL

# Test database connection
railway shell
python -c "from app.database import engine; engine.execute('SELECT 1')"
```

**4. Port Configuration**
```bash
# Ensure PORT variable is set
railway variables set PORT=8003

# Check if app binds to correct port
railway logs | grep "port\|PORT"
```

#### Railway CLI Debug Commands
```bash
# View project details
railway status

# Stream logs in real-time
railway logs --tail

# Access Railway shell
railway shell

# Check service information
railway service

# View current variables
railway variables
```

### 📈 Performance Optimization

#### Railway Resource Limits
- **Memory**: Start with 512MB, scale as needed
- **CPU**: Monitor usage, upgrade plan if needed
- **Storage**: Persistent storage for SQLite (if used)

#### Scaling Configuration
```toml
# railway.toml
[deploy]
startCommand = "uvicorn main:app --host 0.0.0.0 --port $PORT --workers 4"
healthcheckPath = "/health/"
healthcheckTimeout = 300
```

### 🎯 Production Checklist

#### Before Going Live
- [ ] ✅ Environment variables configured
- [ ] ✅ Database connected and migrated
- [ ] ✅ Health checks passing
- [ ] ✅ Secret key generated and secured
- [ ] ✅ CORS properly configured
- [ ] ✅ SSL certificate active (automatic with Railway)
- [ ] ✅ Monitoring and logging operational
- [ ] ✅ Backup strategy in place

#### Post-Deployment Verification
```bash
# Test all endpoints
curl https://your-app.railway.app/health/
curl https://your-app.railway.app/debug/component-status
curl https://your-app.railway.app/docs

# Test API functionality
curl -X POST https://your-app.railway.app/api/pairs-trading/analyze \
  -H "Content-Type: application/json" \
  -d '{"pairs": ["BTCUSDT", "ETHUSDT"]}'
```

### 🔄 Continuous Deployment

#### GitHub Actions Integration
The project includes automatic Railway deployment via GitHub Actions:

```yaml
# .github/workflows/ci-cd.yml includes:
- Railway CLI installation
- Automatic deployment on master push
- Health checks after deployment
- Performance testing
- Deployment notifications
```

Your PSO+Zscore Trading Application is now ready for professional Railway deployment with enterprise-grade monitoring, security, and scalability! 🚀