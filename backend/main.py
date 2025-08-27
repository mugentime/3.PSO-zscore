from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import uvicorn
import structlog
from app.config import settings
from app.database import engine, Base
from app.routers import health, optimization, pairs_trading, debug

# Configure structured logging
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.processors.JSONRenderer()
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
)

logger = structlog.get_logger()

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="PSO+Zscore Trading API",
    description="Pine Script Optimizer + Z-Score Pairs Trading Application",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://*.railway.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security
security = HTTPBearer()

# Include routers
app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(optimization.router, prefix="/api/optimization", tags=["optimization"])
app.include_router(pairs_trading.router, prefix="/api/pairs-trading", tags=["pairs-trading"])
app.include_router(debug.router, prefix="/debug", tags=["debug"])

@app.on_event("startup")
async def startup_event():
    logger.info("PSO+Zscore Trading API starting up", version="1.0.0")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("PSO+Zscore Trading API shutting down")

@app.get("/")
async def root():
    return {
        "message": "PSO+Zscore Trading API",
        "version": "1.0.0",
        "status": "operational",
        "docs": "/docs"
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=settings.PORT,
        reload=settings.DEBUG,
        log_config=None  # Use structlog instead
    )