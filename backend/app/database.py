from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean, Text, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings
import datetime

engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database Models
class Strategy(Base):
    __tablename__ = "strategies"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    pine_script = Column(Text)
    parameters = Column(JSON)
    status = Column(String, default="pending")  # pending, optimizing, backtesting, live
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

class OptimizationRun(Base):
    __tablename__ = "optimization_runs"
    
    id = Column(Integer, primary_key=True, index=True)
    strategy_id = Column(Integer, index=True)
    algorithm = Column(String)  # pso, bayesian, genetic
    status = Column(String, default="running")  # running, completed, failed
    best_params = Column(JSON)
    best_score = Column(Float)
    iterations = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    completed_at = Column(DateTime)

class Trade(Base):
    __tablename__ = "trades"
    
    id = Column(Integer, primary_key=True, index=True)
    strategy_id = Column(Integer, index=True)
    symbol = Column(String)
    side = Column(String)  # buy, sell
    quantity = Column(Float)
    price = Column(Float)
    capital_phase = Column(String)  # micro, small, medium, full
    is_live = Column(Boolean, default=False)
    pnl = Column(Float)
    executed_at = Column(DateTime, default=datetime.datetime.utcnow)

class PairCorrelation(Base):
    __tablename__ = "pair_correlations"
    
    id = Column(Integer, primary_key=True, index=True)
    pair1 = Column(String, index=True)
    pair2 = Column(String, index=True)
    correlation = Column(Float)
    zscore = Column(Float)
    status = Column(String)  # neutral, long_pair1, long_pair2
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()