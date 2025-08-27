# PSO+Zscore Trading Application

## 🎯 Project Overview

Pine Script Optimizer + Z-Score Pairs Trading Application is an enterprise-grade algorithmic trading platform that combines advanced particle swarm optimization (PSO) with statistical arbitrage strategies.

## 🚀 Key Features

- **AI-Powered Pine Script Optimization**: Bayesian optimization, genetic algorithms, PSO
- **Statistical Arbitrage**: Z-score mean reversion on cryptocurrency pairs
- **Real Capital Testing**: Progressive scaling from $100 to $100,000+
- **Enterprise Infrastructure**: 99.9% uptime with Railway deployment
- **Target Performance**: 20-35% annual returns with <15% max drawdown

## 🏗️ Architecture

### Frontend (React TypeScript)
- Modern UI with Material-UI components
- Real-time trading dashboard
- Strategy management interface
- Performance visualization

### Backend (FastAPI Python)
- High-performance async API
- Real-time data processing
- Multi-exchange integration
- AI/ML optimization engines

## 🔧 Tech Stack

- **Frontend**: React 18+ TypeScript, Material-UI, WebSockets
- **Backend**: FastAPI, SQLAlchemy, PostgreSQL, Redis
- **Deployment**: Railway with GitHub Actions CI/CD
- **Monitoring**: Claude MCP integration, structured logging
- **Testing**: Jest, pytest, Playwright automation

## 🚀 Quick Start

### Prerequisites
- Node.js 18+
- Python 3.11+
- Railway CLI
- GitHub CLI

### Development Setup

```bash
# Clone repository
git clone https://github.com/mugentime/3.PSO-zscore.git
cd 3.PSO-zscore

# Install frontend dependencies
cd frontend
npm install
cd ..

# Install backend dependencies
cd backend
pip install -r requirements.txt
cd ..

# Start development servers
# Terminal 1: Backend
cd backend && python main.py

# Terminal 2: Frontend  
cd frontend && npm start
```

## 📊 Performance Targets

### Financial KPIs
- **Annual Return**: 20-35% with real capital
- **Sharpe Ratio**: >1.5 across all phases
- **Maximum Drawdown**: <15%
- **Win Rate**: >60% profitable trades

### Technical KPIs
- **System Uptime**: 99.9%+ during trading hours
- **API Response**: <100ms for trading operations
- **Data Processing**: 1M+ ticks per second

## 🔄 Capital Deployment Phases

1. **Micro Capital**: $100-$1,000 (Real money validation)
2. **Small Capital**: $1,000-$10,000 (Performance scaling)
3. **Medium Capital**: $10,000-$100,000 (Risk validation)
4. **Full Capital**: $100,000+ (Production deployment)

## 📈 Trading Strategies

### Pine Script Optimization
- Multi-objective parameter tuning
- Walk-forward validation
- Strategy robustness testing
- Automated backtesting

### Z-Score Pairs Trading
- Statistical arbitrage opportunities
- 100+ cryptocurrency pairs monitoring
- Dynamic hedge ratio calculations
- Market-neutral positioning

## 🛡️ Security & Risk Management

- Encrypted API keys and secure authentication
- Position sizing with stop-loss automation
- Maximum 1-2% risk per trade during testing
- Circuit breakers and daily loss limits
- Comprehensive audit logging

## 🚢 Deployment

### Railway Deployment
```bash
# Login to Railway
railway login --token YOUR_TOKEN

# Deploy application
railway up

# Check deployment status
railway status
```

### Environment Variables
```bash
BINANCE_API_KEY=your_binance_api_key
BINANCE_SECRET_KEY=your_binance_secret_key  
BINANCE_TESTNET=true
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
```

## 🔍 Monitoring & Debug

- Real-time performance metrics
- Claude MCP integration for AI-powered debugging
- Structured logging with audit trails
- Health check endpoints
- Automated alerting system

## 📚 Documentation

- [API Documentation](./docs/api.md)
- [Trading Strategies](./docs/strategies.md)
- [Deployment Guide](./docs/deployment.md)
- [Development Workflow](./docs/development.md)

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Create Pull Request

## 📄 License

This project is proprietary software for algorithmic trading.

## 📞 Contact

- GitHub: [@mugentime](https://github.com/mugentime)
- Project: [3.PSO-zscore](https://github.com/mugentime/3.PSO-zscore)

---

**⚠️ Risk Warning**: Trading involves significant financial risk. Past performance does not guarantee future results. Only trade with capital you can afford to lose.