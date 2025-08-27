import os
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "sqlite:///./trading.db"
    
    # API Settings
    PORT: int = 8003
    DEBUG: bool = True
    SECRET_KEY: str = "your-secret-key-change-this"
    
    # Binance API
    BINANCE_API_KEY: Optional[str] = None
    BINANCE_SECRET_KEY: Optional[str] = None
    BINANCE_TESTNET: bool = True
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379"
    
    # Logging
    LOG_LEVEL: str = "INFO"
    
    # Trading
    MAX_RISK_PER_TRADE: float = 0.02  # 2%
    MICRO_CAPITAL_MIN: float = 100.0
    MICRO_CAPITAL_MAX: float = 1000.0
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()