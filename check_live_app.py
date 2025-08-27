# -*- coding: utf-8 -*-
import requests
import json
from datetime import datetime
import sys

# Fix Windows encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Your LIVE deployment URL
BASE_URL = "https://3pso-zscore-production.up.railway.app"

print("="*60)
print("PSO+Zscore LIVE Trading Application")
print("URL: " + BASE_URL)
print("="*60)
print()

# Check health
print("Checking deployment status...")
try:
    response = requests.get(f"{BASE_URL}/health/", timeout=10)
    if response.status_code == 200:
        print("Application is ONLINE!")
        health_data = response.json()
        print(f"   Status: {health_data.get('status', 'N/A')}")
        print(f"   Timestamp: {health_data.get('timestamp', 'N/A')}")
    else:
        print(f"Health check returned status: {response.status_code}")
        print(f"Response: {response.text}")
except Exception as e:
    print(f"Error checking health: {e}")

print()
print("="*60)
print("Your Live Trading URLs:")
print("="*60)
print(f"Main App:        {BASE_URL}/")
print(f"API Docs:        {BASE_URL}/docs")
print(f"Health Check:    {BASE_URL}/health/")
print(f"Metrics:         {BASE_URL}/api/metrics")
print(f"Pairs Trading:   {BASE_URL}/api/pairs-trading/analyze")
print(f"Optimization:    {BASE_URL}/api/optimization/start")
print(f"Trading Status:  {BASE_URL}/api/config/trading-status")
print("="*60)

# Let's also open the API docs
print()
print("Opening API documentation in browser...")
import webbrowser
webbrowser.open(f"{BASE_URL}/docs")