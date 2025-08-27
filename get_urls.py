# -*- coding: utf-8 -*-
import requests
import json
import sys

# Set UTF-8 encoding for Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Railway Project Details
PROJECT_ID = "cd882d82-3b5a-41ba-882f-37e8b961224e"
SERVICE_ID = "9ef5f530-f52a-4f81-aaf4-5669174c3e59"
ENVIRONMENT_ID = "f17be55a-922a-4d0f-acc0-98aebc48d677"

print("="*60)
print("PSO+Zscore Trading Application URLs")
print("="*60)
print()

# Railway Dashboard URLs
print("Railway Dashboard URLs:")
print(f"Project Dashboard: https://railway.app/project/{PROJECT_ID}")
print(f"Service Dashboard: https://railway.app/project/{PROJECT_ID}/service/{SERVICE_ID}")
print(f"Full Dashboard: https://railway.app/project/{PROJECT_ID}/service/{SERVICE_ID}?environmentId={ENVIRONMENT_ID}")
print()

# Common Railway deployment URL patterns
print("Your App URL (check Railway dashboard for exact URL):")
print("Common patterns:")
print("  - https://pso-zscore-production.up.railway.app")
print("  - https://3pso-zscore-production.up.railway.app")  
print("  - https://web-production-[hash].up.railway.app")
print()

print("To find your exact app URL:")
print("1. Open Railway dashboard (link above)")
print("2. Look for 'Deployment URL' or 'Public URL'")
print("3. It will be shown at the top of your service page")
print()

# Test common URLs
test_urls = [
    "https://pso-zscore-production.up.railway.app",
    "https://3pso-zscore-production.up.railway.app",
    "https://pso-zscore.up.railway.app",
    "https://web-production-cd88.up.railway.app",
]

print("Testing possible URLs...")
found = False
for url in test_urls:
    try:
        response = requests.get(f"{url}/health/", timeout=3)
        if response.status_code == 200:
            print(f"FOUND WORKING URL: {url}")
            print(f"   Status: {response.json().get('status', 'Active')}")
            
            print()
            print("="*60)
            print("YOUR DEPLOYMENT URLs:")
            print(f"App URL: {url}")
            print(f"Health Check: {url}/health/")
            print(f"API Docs: {url}/docs")
            print(f"Pairs Trading: {url}/api/pairs-trading/analyze")
            print(f"Optimization: {url}/api/optimization/start")
            print(f"Metrics: {url}/api/metrics")
            print("="*60)
            found = True
            break
    except:
        print(f"Not accessible: {url}")

if not found:
    print()
    print("Could not automatically detect the URL.")
    print("Please check your Railway dashboard for the exact URL.")
    print("The deployment URL is shown at the top of your service page.")