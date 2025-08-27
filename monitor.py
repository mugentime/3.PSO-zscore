import requests
import json
import time
from datetime import datetime
from colorama import init, Fore, Style
import os

# Initialize colorama for Windows
init(autoreset=True)

class TradingMonitor:
    def __init__(self, base_url="http://localhost:8003"):
        self.base_url = base_url
        self.is_production = os.getenv("RAILWAY_ENVIRONMENT") == "production"
        
    def check_health(self):
        """Check application health status"""
        try:
            response = requests.get(f"{self.base_url}/health/", timeout=5)
            if response.status_code == 200:
                data = response.json()
                return True, data
            return False, None
        except Exception as e:
            return False, str(e)
    
    def check_trading_status(self):
        """Check trading configuration and status"""
        try:
            response = requests.get(f"{self.base_url}/api/config/trading-status", timeout=5)
            if response.status_code == 200:
                return response.json()
            return None
        except:
            return None
    
    def get_metrics(self):
        """Get trading metrics"""
        try:
            response = requests.get(f"{self.base_url}/api/metrics", timeout=5)
            if response.status_code == 200:
                return response.json()
            return None
        except:
            return None
    
    def display_status(self):
        """Display comprehensive trading status"""
        print("\n" + "="*60)
        print(f"{Fore.CYAN}PSO+Zscore Trading Monitor - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*60)
        
        # Health Check
        healthy, health_data = self.check_health()
        if healthy:
            print(f"{Fore.GREEN}✓ Application Status: ONLINE")
            if isinstance(health_data, dict):
                print(f"  Version: {health_data.get('version', 'N/A')}")
                print(f"  Uptime: {health_data.get('uptime', 'N/A')}")
        else:
            print(f"{Fore.RED}✗ Application Status: OFFLINE")
            print(f"  Error: {health_data}")
            return
        
        # Trading Configuration
        print(f"\n{Fore.YELLOW}Trading Configuration:")
        trading_status = self.check_trading_status()
        if trading_status:
            testnet = trading_status.get('binance_testnet', True)
            if testnet:
                print(f"{Fore.BLUE}  Mode: TESTNET (Paper Trading)")
            else:
                print(f"{Fore.RED}  Mode: LIVE TRADING (Real Money)")
            
            print(f"  Capital Phase: {trading_status.get('capital_phase', 'N/A')}")
            print(f"  Initial Capital: ${trading_status.get('initial_capital', 0):,.2f}")
            print(f"  Max Risk Per Trade: {trading_status.get('max_risk_per_trade', 0)*100:.1f}%")
            print(f"  Trading Enabled: {trading_status.get('trading_enabled', False)}")
        
        # Metrics
        print(f"\n{Fore.CYAN}Performance Metrics:")
        metrics = self.get_metrics()
        if metrics:
            print(f"  Total Trades: {metrics.get('total_trades', 0)}")
            print(f"  Win Rate: {metrics.get('win_rate', 0)*100:.1f}%")
            print(f"  Profit Factor: {metrics.get('profit_factor', 0):.2f}")
            print(f"  Current Drawdown: {metrics.get('current_drawdown', 0)*100:.1f}%")
            print(f"  Sharpe Ratio: {metrics.get('sharpe_ratio', 0):.2f}")
        
        # Warnings
        if not testnet:
            print(f"\n{Fore.RED}{'='*60}")
            print(f"{Fore.RED}⚠️  LIVE TRADING ACTIVE - REAL MONEY AT RISK")
            print(f"{Fore.RED}{'='*60}")

def monitor_loop(interval=60):
    """Continuous monitoring loop"""
    monitor = TradingMonitor()
    
    print(f"{Fore.GREEN}Starting PSO+Zscore Trading Monitor...")
    print(f"Checking every {interval} seconds. Press Ctrl+C to stop.\n")
    
    try:
        while True:
            monitor.display_status()
            time.sleep(interval)
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Monitoring stopped.")

def check_deployment():
    """Check Railway deployment status"""
    railway_url = os.getenv("RAILWAY_STATIC_URL")
    if railway_url:
        print(f"{Fore.GREEN}Railway Deployment URL: {railway_url}")
        monitor = TradingMonitor(base_url=railway_url)
        monitor.display_status()
    else:
        print(f"{Fore.YELLOW}No Railway deployment detected. Checking local...")
        monitor = TradingMonitor()
        monitor.display_status()

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "loop":
            interval = int(sys.argv[2]) if len(sys.argv) > 2 else 60
            monitor_loop(interval)
        elif sys.argv[1] == "deployment":
            check_deployment()
    else:
        # Single check
        monitor = TradingMonitor()
        monitor.display_status()
        
        print(f"\n{Fore.YELLOW}Usage:")
        print("  python monitor.py          # Single status check")
        print("  python monitor.py loop 60  # Monitor every 60 seconds")
        print("  python monitor.py deployment # Check Railway deployment")