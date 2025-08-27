from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from pydantic import BaseModel
from typing import Dict, Any, List
import structlog
import json
import time
import os

router = APIRouter()
logger = structlog.get_logger()

# In-memory storage for debug logs (in production, use Redis or database)
debug_logs = []

class DebugAnalysisRequest(BaseModel):
    component: str
    error_type: str
    additional_context: Dict[str, Any] = {}

class ComponentStatus(BaseModel):
    name: str
    status: str
    last_check: float
    details: Dict[str, Any] = {}

@router.get("/component-status")
async def get_component_status(db: Session = Depends(get_db)):
    """Get status of all system components"""
    components = []
    
    # Database status
    try:
        db.execute("SELECT 1")
        db_status = ComponentStatus(
            name="database",
            status="healthy",
            last_check=time.time(),
            details={"type": "SQLite", "connection": "active"}
        )
    except Exception as e:
        db_status = ComponentStatus(
            name="database",
            status="unhealthy",
            last_check=time.time(),
            details={"error": str(e)}
        )
    components.append(db_status)
    
    # Binance API status
    api_key = os.getenv("BINANCE_API_KEY")
    binance_status = ComponentStatus(
        name="binance_api",
        status="configured" if api_key else "not_configured",
        last_check=time.time(),
        details={
            "testnet": os.getenv("BINANCE_TESTNET", "true"),
            "api_key_present": bool(api_key)
        }
    )
    components.append(binance_status)
    
    # Optimization engines status
    opt_status = ComponentStatus(
        name="optimization_engines",
        status="ready",
        last_check=time.time(),
        details={
            "algorithms": ["bayesian", "pso", "genetic"],
            "status": "initialized"
        }
    )
    components.append(opt_status)
    
    return {
        "components": components,
        "overall_status": "healthy" if all(c.status in ["healthy", "ready", "configured"] for c in components) else "degraded",
        "timestamp": time.time()
    }

@router.get("/metrics")
async def get_system_metrics():
    """Get system performance metrics"""
    try:
        import psutil
        
        # CPU and memory metrics
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        
        # Process-specific metrics
        process = psutil.Process()
        process_memory = process.memory_info()
        
        return {
            "system": {
                "cpu_percent": cpu_percent,
                "memory_percent": memory.percent,
                "memory_available_gb": round(memory.available / (1024**3), 2),
                "disk_percent": round((disk.used / disk.total) * 100, 2),
                "uptime_hours": round((time.time() - psutil.boot_time()) / 3600, 2)
            },
            "process": {
                "memory_rss_mb": round(process_memory.rss / (1024**2), 2),
                "memory_vms_mb": round(process_memory.vms / (1024**2), 2),
                "cpu_percent": process.cpu_percent(),
                "threads": process.num_threads()
            },
            "timestamp": time.time()
        }
    except ImportError:
        return {
            "error": "psutil not available",
            "timestamp": time.time()
        }

@router.post("/analyze")
async def analyze_component(request: DebugAnalysisRequest):
    """Analyze specific component issues using Claude MCP integration"""
    
    analysis_prompt = f"""
    Analyzing {request.component} with error type: {request.error_type}
    Additional context: {json.dumps(request.additional_context, indent=2)}
    
    Please provide:
    1. Potential root causes
    2. Debugging steps
    3. Recommended fixes
    4. Prevention strategies
    """
    
    # Log the debug analysis request
    debug_entry = {
        "timestamp": time.time(),
        "component": request.component,
        "error_type": request.error_type,
        "context": request.additional_context,
        "analysis_requested": True
    }
    debug_logs.append(debug_entry)
    
    # Keep only last 1000 debug entries
    if len(debug_logs) > 1000:
        debug_logs[:] = debug_logs[-1000:]
    
    logger.info(
        "Debug analysis requested",
        component=request.component,
        error_type=request.error_type
    )
    
    # TODO: Integrate with Claude MCP for actual AI-powered analysis
    # For now, return structured debugging guidance
    
    analysis_results = {
        "component": request.component,
        "error_type": request.error_type,
        "analysis": {
            "potential_causes": _get_potential_causes(request.component, request.error_type),
            "debugging_steps": _get_debugging_steps(request.component),
            "recommended_fixes": _get_recommended_fixes(request.component, request.error_type),
            "prevention_strategies": _get_prevention_strategies(request.component)
        },
        "timestamp": time.time()
    }
    
    return analysis_results

@router.get("/logs")
async def get_debug_logs(limit: int = 50):
    """Get recent debug logs"""
    return {
        "logs": debug_logs[-limit:] if debug_logs else [],
        "total_logs": len(debug_logs),
        "timestamp": time.time()
    }

@router.delete("/logs")
async def clear_debug_logs():
    """Clear debug logs"""
    global debug_logs
    log_count = len(debug_logs)
    debug_logs.clear()
    
    logger.info("Debug logs cleared", previous_count=log_count)
    
    return {
        "message": f"Cleared {log_count} debug log entries",
        "timestamp": time.time()
    }

def _get_potential_causes(component: str, error_type: str) -> List[str]:
    """Get potential causes for component errors"""
    causes_map = {
        "binance_client": {
            "connection_failed": [
                "Invalid API credentials",
                "Network connectivity issues",
                "Binance API rate limits exceeded",
                "Testnet vs mainnet configuration mismatch"
            ],
            "order_failed": [
                "Insufficient balance",
                "Invalid symbol or quantity",
                "Market conditions (price movement)",
                "Position size limits exceeded"
            ]
        },
        "optimization_engine": {
            "convergence_failed": [
                "Poor parameter bounds",
                "Insufficient data quality",
                "Objective function issues",
                "Algorithm hyperparameters need tuning"
            ]
        }
    }
    
    return causes_map.get(component, {}).get(error_type, ["Unknown component/error combination"])

def _get_debugging_steps(component: str) -> List[str]:
    """Get debugging steps for component"""
    steps_map = {
        "binance_client": [
            "Check API key and secret configuration",
            "Verify network connectivity to binance.com",
            "Check rate limiting and request timestamps",
            "Validate symbol names and market hours"
        ],
        "optimization_engine": [
            "Verify input data quality and completeness",
            "Check parameter bounds and constraints",
            "Monitor convergence metrics and iterations",
            "Validate objective function calculations"
        ]
    }
    
    return steps_map.get(component, ["Check component logs and configuration"])

def _get_recommended_fixes(component: str, error_type: str) -> List[str]:
    """Get recommended fixes for specific errors"""
    fixes_map = {
        "binance_client": {
            "connection_failed": [
                "Verify API credentials in environment variables",
                "Check BINANCE_TESTNET setting matches API keys",
                "Implement exponential backoff for rate limits",
                "Add connection timeout and retry logic"
            ]
        }
    }
    
    return fixes_map.get(component, {}).get(error_type, ["Review component documentation"])

def _get_prevention_strategies(component: str) -> List[str]:
    """Get prevention strategies for component"""
    strategies_map = {
        "binance_client": [
            "Implement comprehensive error handling",
            "Add monitoring and alerting for API failures",
            "Use connection pooling and keep-alive",
            "Implement circuit breaker pattern"
        ],
        "optimization_engine": [
            "Add data validation before optimization",
            "Implement early stopping criteria",
            "Monitor and log optimization progress",
            "Use cross-validation for robustness"
        ]
    }
    
    return strategies_map.get(component, ["Implement monitoring and logging"])