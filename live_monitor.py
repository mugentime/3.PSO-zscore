import requests
import json
from datetime import datetime
import time

# Your Railway deployment URL (update this with your actual URL)
# Based on your project ID, it should be something like:
BASE_URL = "https://pso-zscore-production-cd88.up.railway.app"

def check_deployment():
    """Check the live deployment status"""
    print("="*60)
    print(f"PSO+Zscore LIVE TRADING Monitor")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)
    
    endpoints = [
        ("/health/", "Health Check"),
        ("/api/config/trading-status", "Trading Configuration"),
        ("/api/metrics", "Performance Metrics"),
    ]
    
    for endpoint, name in endpoints:
        try:
            print(f"\n📍 Checking {name}...")
            response = requests.get(f"{BASE_URL}{endpoint}", timeout=10)
            
            if response.status_code == 200:
                print(f"✅ {name}: ONLINE")
                data = response.json()
                
                if "trading-status" in endpoint:
                    testnet = data.get('binance_testnet', True)
                    if not testnet:
                        print("🔴 LIVE TRADING ACTIVE - Real Money")
                    else:
                        print("🔵 TESTNET Mode")
                    print(f"   Capital Phase: {data.get('capital_phase', 'N/A')}")
                    print(f"   Trading Enabled: {data.get('trading_enabled', False)}")
                
                elif "metrics" in endpoint:
                    print(f"   Total Trades: {data.get('total_trades', 0)}")
                    print(f"   Win Rate: {data.get('win_rate', 0)*100:.1f}%")
                    print(f"   Current P&L: ${data.get('current_pnl', 0):,.2f}")
                
                elif "health" in endpoint:
                    print(f"   Status: {data.get('status', 'N/A')}")
                    print(f"   Version: {data.get('version', 'N/A')}")
                    
            else:
                print(f"⚠️ {name}: Status {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            print(f"❌ {name}: Cannot connect - Check if URL is correct")
            print(f"   URL tried: {BASE_URL}{endpoint}")
        except requests.exceptions.Timeout:
            print(f"⏱️ {name}: Timeout")
        except Exception as e:
            print(f"❌ {name}: Error - {e}")
    
    print("\n" + "="*60)
    print("Railway Project URL:")
    print("https://railway.com/project/cd882d82-3b5a-41ba-882f-37e8b961224e")
    print("="*60)

def monitor_continuous(interval=30):
    """Monitor continuously"""
    print(f"Starting continuous monitoring every {interval} seconds...")
    print("Press Ctrl+C to stop\n")
    
    while True:
        check_deployment()
        print(f"\n⏰ Next check in {interval} seconds...")
        time.sleep(interval)

if __name__ == "__main__":
    import sys
    
    # First, try to find the actual deployment URL
    print("📡 Checking Railway Deployment...")
    print("Project ID: cd882d82-3b5a-41ba-882f-37e8b961224e")
    print("\nNote: Update BASE_URL in this script with your actual Railway URL")
    print("You can find it in the Railway dashboard under 'Deployments'\n")
    
    if len(sys.argv) > 1 and sys.argv[1] == "loop":
        interval = int(sys.argv[2]) if len(sys.argv) > 2 else 30
        monitor_continuous(interval)
    else:
        check_deployment()
        print("\nUsage:")
        print("  python live_monitor.py          # Single check")
        print("  python live_monitor.py loop 30  # Monitor every 30 seconds")