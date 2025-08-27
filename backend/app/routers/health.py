from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
import structlog
import time
import psutil
import os

router = APIRouter()
logger = structlog.get_logger()

@router.get("/")
async def health_check():
    """Basic health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": time.time(),
        "version": "1.0.0"
    }

@router.get("/detailed")
async def detailed_health_check(db: Session = Depends(get_db)):
    """Detailed health check with system metrics"""
    try:
        # Test database connection
        db.execute("SELECT 1")
        db_status = "connected"
    except Exception as e:
        logger.error("Database health check failed", error=str(e))
        db_status = "failed"
    
    # System metrics
    memory = psutil.virtual_memory()
    cpu_percent = psutil.cpu_percent(interval=1)
    disk = psutil.disk_usage('/')
    
    return {
        "status": "healthy",
        "timestamp": time.time(),
        "version": "1.0.0",
        "database": db_status,
        "system": {
            "cpu_percent": cpu_percent,
            "memory_percent": memory.percent,
            "disk_percent": (disk.used / disk.total) * 100,
            "uptime": time.time() - psutil.boot_time()
        },
        "environment": {
            "debug": os.getenv("DEBUG", "false"),
            "testnet": os.getenv("BINANCE_TESTNET", "true")
        }
    }

@router.get("/live")
async def liveness_probe():
    """Kubernetes/Docker liveness probe"""
    return {"status": "alive"}

@router.get("/ready")
async def readiness_probe(db: Session = Depends(get_db)):
    """Kubernetes/Docker readiness probe"""
    try:
        db.execute("SELECT 1")
        return {"status": "ready"}
    except Exception:
        raise HTTPException(status_code=503, detail="Database not ready")