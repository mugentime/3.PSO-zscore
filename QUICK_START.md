# PSO+Zscore Trading Application - Quick Start Guide

## 🚀 Immediate Next Steps

### Step 1: Initialize Project Structure
```bash
cd C:\Users\je2al\Desktop\3.PSO-zscore

# Create basic structure
mkdir frontend backend docs tests
mkdir frontend/src frontend/public frontend/src/components
mkdir backend/app backend/app/api backend/app/services backend/app/models
mkdir backend/tests

# Initialize git
git init
git remote add origin https://github.com/mugentime/3.PSO-zscore.git
```

### Step 2: Set Up Backend
```bash
cd backend

# Create requirements.txt
cat > requirements.txt << EOF
fastapi==0.115.5
uvicorn[standard]==0.32.1
python-binance==1.0.19
pandas==2.2.3
numpy==2.0.2
scikit-learn==1.5.2
optuna==4.1.0
sqlalchemy==2.0.36
alembic==1.14.0
psycopg2-binary==2.9.10
redis==5.2.1
celery==5.4.0
pydantic==2.10.3
python-jose[cryptography]==3.3.0
python-multipart==0.0.12
pytest==8.3.4
pytest-asyncio==0.24.0
pytest-cov==6.0.0
python-dotenv==1.0.1
structlog==24.4.0
sentry-sdk==2.19.2
prometheus-client==0.21.1
EOF

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt

# Create main.py
cat > main.py << 'EOF'
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="PSO+Zscore Trading API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "pso-zscore-api"}

@app.get("/")
async def root():
    return {"message": "PSO+Zscore Trading API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)
EOF
```

### Step 3: Set Up Frontend
```bash
cd ../frontend

# Create React app with TypeScript
npx create-react-app . --template typescript

# Install additional dependencies
npm install @mui/material @emotion/react @emotion/styled
npm install @mui/icons-material @mui/x-data-grid
npm install axios react-router-dom
npm install socket.io-client
npm install recharts
npm install --save-dev @types/react-router-dom

# Update package.json proxy
# Add to package.json:
# "proxy": "http://localhost:8003",
```

### Step 4: Configure Railway Deployment
```bash
# Create railway.json in root
cat > railway.json << EOF
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "DOCKERFILE",
    "dockerfilePath": "backend/Dockerfile"
  },
  "deploy": {
    "numReplicas": 1,
    "healthcheckPath": "/health",
    "healthcheckTimeout": 100,
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
EOF

# Create backend/Dockerfile
cat > backend/Dockerfile << EOF
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8003

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003"]
EOF
```

### Step 5: GitHub Actions CI/CD
```bash
# Create .github/workflows/deploy.yml
mkdir -p .github/workflows
cat > .github/workflows/deploy.yml << 'EOF'
name: Deploy to Railway

on:
  push:
    branches: [master, main]
  pull_request:
    branches: [master, main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          
      - name: Install dependencies
        run: |
          cd backend
          pip install -r requirements.txt
          
      - name: Run tests
        run: |
          cd backend
          pytest tests/ -v --cov=app
          
  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.event_name == 'push'
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Deploy to Railway
        uses: bervProject/railway-deploy@main
        env:
          RAILWAY_TOKEN: ${{ secrets.RAILWAY_TOKEN }}
EOF
```

### Step 6: Environment Variables
```bash
# Create backend/.env
cat > backend/.env << EOF
# Binance API (Testnet first!)
BINANCE_API_KEY=your_testnet_api_key
BINANCE_SECRET_KEY=your_testnet_secret_key
BINANCE_TESTNET=true

# Database
DATABASE_URL=postgresql://user:password@localhost/pso_zscore

# Security
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Railway
RAILWAY_TOKEN=e0ae87e0-75e3-4db6-bebe-8286df2b7a10

# Monitoring
SENTRY_DSN=your_sentry_dsn_here
EOF
```

### Step 7: Test Local Setup
```bash
# Terminal 1 - Start backend
cd backend
python main.py
# Should see: INFO: Uvicorn running on http://0.0.0.0:8003

# Terminal 2 - Start frontend
cd frontend
npm start
# Should open: http://localhost:3000

# Test API
curl http://localhost:8003/health
# Should return: {"status":"healthy","service":"pso-zscore-api"}
```

### Step 8: Deploy to Railway
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login with token
railway login --token e0ae87e0-75e3-4db6-bebe-8286df2b7a10

# Initialize project
railway link

# Deploy
railway up

# Check deployment
railway status
railway logs
```

### Step 9: Configure MCP Tools
```bash
# Install MCP tools globally
npm install -g @railway/mcp-server
npm install -g @playwright/mcp
npm install -g @modelcontextprotocol/server-filesystem
npm install -g @magicuidesign/cli
uv tool install tradingview-chart-mcp

# Test MCP tools
npx @railway/mcp-server --help
```

### Step 10: Verify Everything Works
```bash
# Check GitHub repo
git add .
git commit -m "Initial project setup"
git push origin master

# Should trigger:
# ✅ GitHub Actions workflow
# ✅ Automated tests
# ✅ Railway deployment
# ✅ Health check passes

# Access deployed app
# https://your-app.railway.app/health
```

## 📋 Taskmaster Commands

```bash
# View all tasks
tm get-tasks

# Start working on first task
tm set-status --id 1 --status in-progress

# Check next task
tm next

# Update task progress
tm update-task --id 1 --prompt "Completed GitHub setup, working on Railway"

# Add notes to a task
tm update-task --id 1 --append --prompt "Railway deployment successful, URL: xxx"

# Complete a task
tm set-status --id 1 --status done

# View task details
tm get-task --id 1
```

## ✅ Success Checklist

- [ ] Project structure created
- [ ] Backend API running locally
- [ ] Frontend React app running
- [ ] Database configured
- [ ] GitHub repository connected
- [ ] Railway deployment working
- [ ] CI/CD pipeline active
- [ ] MCP tools installed
- [ ] Environment variables set
- [ ] Health checks passing

## 🚨 Common Issues & Solutions

### Issue: Railway deployment fails
```bash
# Check logs
railway logs

# Verify environment variables
railway variables

# Redeploy
railway up --detach
```

### Issue: Database connection error
```bash
# Start PostgreSQL locally
# Update DATABASE_URL in .env
# Run migrations
cd backend
alembic init alembic
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

### Issue: Binance API authentication fails
```bash
# Get testnet credentials from:
# https://testnet.binance.vision/

# Update .env with testnet keys
# Set BINANCE_TESTNET=true
```

## 📞 Next Actions

1. **Complete Task #1**: Infrastructure setup ✅
2. **Start Task #2**: Configure MCP tools
3. **Begin Task #3**: Build FastAPI structure
4. **Work on Task #4**: Create React frontend

Use `tm next` to always see the next priority task!

---
*Ready to build! Start with the steps above and track progress with Taskmaster.*