from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from app.database import get_db, PairCorrelation
from pydantic import BaseModel
from typing import List, Optional
import structlog
import numpy as np

router = APIRouter()
logger = structlog.get_logger()

class PairsAnalysisRequest(BaseModel):
    pairs: List[str]
    timeframe: str = "4h"
    lookback_days: int = 30
    zscore_threshold: float = 2.0

class PairAnalysis(BaseModel):
    pair1: str
    pair2: str
    correlation: float
    zscore: float
    signal: str  # "long_pair1", "long_pair2", "neutral"
    strength: str  # "strong", "medium", "weak"

class PairsAnalysisResponse(BaseModel):
    analysis: List[PairAnalysis]
    summary: dict

@router.post("/analyze", response_model=PairsAnalysisResponse)
async def analyze_pairs(
    request: PairsAnalysisRequest,
    db: Session = Depends(get_db)
):
    """Analyze cryptocurrency pairs for statistical arbitrage opportunities"""
    try:
        logger.info(
            "Starting pairs analysis",
            pairs=request.pairs,
            timeframe=request.timeframe,
            lookback_days=request.lookback_days
        )
        
        analysis_results = []
        
        # Generate all possible pair combinations
        for i, pair1 in enumerate(request.pairs):
            for j, pair2 in enumerate(request.pairs):
                if i < j:  # Avoid duplicates
                    # Mock analysis - in real implementation, fetch historical data
                    # and calculate actual correlations and z-scores
                    correlation = np.random.uniform(0.3, 0.95)
                    zscore = np.random.uniform(-3.0, 3.0)
                    
                    # Determine signal based on z-score threshold
                    if zscore > request.zscore_threshold:
                        signal = "long_pair2"  # pair1 is overvalued relative to pair2
                    elif zscore < -request.zscore_threshold:
                        signal = "long_pair1"  # pair2 is overvalued relative to pair1
                    else:
                        signal = "neutral"
                    
                    # Determine signal strength
                    abs_zscore = abs(zscore)
                    if abs_zscore > request.zscore_threshold * 1.5:
                        strength = "strong"
                    elif abs_zscore > request.zscore_threshold:
                        strength = "medium"
                    else:
                        strength = "weak"
                    
                    pair_analysis = PairAnalysis(
                        pair1=pair1,
                        pair2=pair2,
                        correlation=round(correlation, 4),
                        zscore=round(zscore, 4),
                        signal=signal,
                        strength=strength
                    )
                    analysis_results.append(pair_analysis)
                    
                    # Update database with correlation data
                    existing_pair = db.query(PairCorrelation).filter(
                        PairCorrelation.pair1 == pair1,
                        PairCorrelation.pair2 == pair2
                    ).first()
                    
                    if existing_pair:
                        existing_pair.correlation = correlation
                        existing_pair.zscore = zscore
                        existing_pair.status = signal
                    else:
                        new_pair = PairCorrelation(
                            pair1=pair1,
                            pair2=pair2,
                            correlation=correlation,
                            zscore=zscore,
                            status=signal
                        )
                        db.add(new_pair)
                    
                    db.commit()
        
        # Generate summary statistics
        strong_signals = [p for p in analysis_results if p.strength == "strong" and p.signal != "neutral"]
        medium_signals = [p for p in analysis_results if p.strength == "medium" and p.signal != "neutral"]
        
        summary = {
            "total_pairs": len(analysis_results),
            "strong_signals": len(strong_signals),
            "medium_signals": len(medium_signals),
            "avg_correlation": round(np.mean([p.correlation for p in analysis_results]), 4),
            "max_abs_zscore": round(max([abs(p.zscore) for p in analysis_results]), 4),
            "arbitrage_opportunities": len([p for p in analysis_results if abs(p.zscore) > request.zscore_threshold])
        }
        
        logger.info("Pairs analysis completed", summary=summary)
        
        return PairsAnalysisResponse(
            analysis=analysis_results,
            summary=summary
        )
        
    except Exception as e:
        logger.error("Pairs analysis failed", error=str(e))
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/correlations")
async def get_correlations(db: Session = Depends(get_db)):
    """Get current pair correlations from database"""
    correlations = db.query(PairCorrelation).order_by(
        PairCorrelation.updated_at.desc()
    ).limit(100).all()
    
    return [
        {
            "pair1": corr.pair1,
            "pair2": corr.pair2,
            "correlation": corr.correlation,
            "zscore": corr.zscore,
            "signal": corr.status,
            "updated_at": corr.updated_at
        }
        for corr in correlations
    ]

@router.get("/opportunities")
async def get_arbitrage_opportunities(
    min_zscore: float = 2.0,
    min_correlation: float = 0.5,
    db: Session = Depends(get_db)
):
    """Get current arbitrage opportunities based on z-score and correlation thresholds"""
    opportunities = db.query(PairCorrelation).filter(
        PairCorrelation.correlation >= min_correlation,
        PairCorrelation.zscore.abs() >= min_zscore
    ).order_by(
        PairCorrelation.zscore.abs().desc()
    ).limit(20).all()
    
    return [
        {
            "pair1": opp.pair1,
            "pair2": opp.pair2,
            "correlation": opp.correlation,
            "zscore": opp.zscore,
            "signal": opp.status,
            "strength": "strong" if abs(opp.zscore) > min_zscore * 1.5 else "medium",
            "updated_at": opp.updated_at
        }
        for opp in opportunities
    ]