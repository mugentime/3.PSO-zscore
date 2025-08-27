import os
import subprocess
import sys
import time

# Set Railway token
os.environ['RAILWAY_TOKEN'] = 'e0ae87e0-75e3-4db6-bebe-8286df2b7a10'

# Change to project directory
os.chdir(r'C:\Users\je2al\Desktop\3.PSO-zscore')

print("=" * 60)
print("PSO+Zscore LIVE TRADING Deployment")
print("BINANCE_TESTNET = false")
print("=" * 60)
print()

# Try to deploy
print("Attempting deployment to Railway...")
try:
    # First try to link/create project
    result = subprocess.run(['railway', 'link'], 
                          capture_output=True, 
                          text=True, 
                          env=os.environ)
    
    if result.returncode != 0:
        print("Creating new Railway project...")
        result = subprocess.run(['railway', 'init'], 
                              capture_output=True, 
                              text=True,
                              env=os.environ)
        
        if result.returncode != 0:
            print(f"Init output: {result.stdout}")
            print(f"Init error: {result.stderr}")
    
    # Now deploy
    print("\nDeploying application...")
    result = subprocess.run(['railway', 'up', '--detach'], 
                          capture_output=True, 
                          text=True,
                          env=os.environ)
    
    if result.returncode == 0:
        print("✓ Deployment initiated successfully!")
        print(result.stdout)
        
        # Get status
        print("\nChecking deployment status...")
        result = subprocess.run(['railway', 'status'], 
                              capture_output=True, 
                              text=True,
                              env=os.environ)
        print(result.stdout)
        
    else:
        print(f"Deployment failed: {result.stderr}")
        print("\nTrying alternative deployment method...")
        
        # Try with explicit service
        result = subprocess.run(['railway', 'up', '--service', 'pso-zscore'], 
                              capture_output=True, 
                              text=True,
                              env=os.environ)
        print(result.stdout)
        
except Exception as e:
    print(f"Error: {e}")
    print("\nPlease ensure Railway CLI is installed:")
    print("npm install -g @railway/cli")

print("\n" + "=" * 60)
print("Deployment process completed")
print("Check your Railway dashboard: https://railway.app/dashboard")
print("=" * 60)