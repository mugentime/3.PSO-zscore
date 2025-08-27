#!/usr/bin/env python3
"""
MCP Tools Integration Test Suite for PSO+Zscore Trading Application
Simple version without Unicode characters for Windows compatibility
"""
import subprocess
import json
import os
import sys
from datetime import datetime
from pathlib import Path

def test_npm_mcp_tools():
    """Test if NPM MCP packages are installed"""
    print("[NPM] Testing NPM MCP packages...")
    
    packages = [
        "@jasontanswe/railway-mcp",
        "@playwright/mcp", 
        "@modelcontextprotocol/server-filesystem",
        "@magicuidesign/cli",
        "@sentry/mcp-server",
        "@browsermcp/mcp"
    ]
    
    results = {}
    for package in packages:
        try:
            result = subprocess.run(
                ["npm", "list", "-g", package],
                capture_output=True,
                text=True,
                timeout=10
            )
            status = "[OK] INSTALLED" if result.returncode == 0 else "[FAIL] NOT FOUND"
            print(f"  {package}: {status}")
            results[package] = status
        except Exception as e:
            print(f"  {package}: [ERROR] {str(e)}")
            results[package] = f"[ERROR] {str(e)}"
            
    return results

def test_uv_tools():
    """Test if UV tools are installed"""
    print("[UV] Testing UV Python packages...")
    
    packages = ["tradingview-chart-mcp", "task-master-ai"]
    results = {}
    
    for package in packages:
        try:
            result = subprocess.run(
                ["uv", "tool", "list"],
                capture_output=True,
                text=True,
                timeout=10
            )
            status = "[OK] INSTALLED" if package in result.stdout else "[FAIL] NOT FOUND"
            print(f"  {package}: {status}")
            results[package] = status
        except Exception as e:
            print(f"  {package}: [ERROR] {str(e)}")
            results[package] = f"[ERROR] {str(e)}"
            
    return results

def test_railway_connection():
    """Test Railway CLI connection"""
    print("[RAILWAY] Testing Railway connection...")
    
    try:
        result = subprocess.run(
            ["railway", "whoami"],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            user = result.stdout.strip()
            print(f"  Railway: [OK] CONNECTED as {user}")
            return {"railway": f"[OK] CONNECTED as {user}"}
        else:
            print("  Railway: [FAIL] NOT CONNECTED")
            return {"railway": "[FAIL] NOT CONNECTED"}
            
    except Exception as e:
        print(f"  Railway: [ERROR] {str(e)}")
        return {"railway": f"[ERROR] {str(e)}"}

def test_project_structure():
    """Test project structure"""
    print("[PROJECT] Testing project structure...")
    
    project_root = Path("C:/Users/je2al/Desktop/3.PSO-zscore")
    
    required_files = [
        "mcp-config.json",
        "claude-desktop-mcp-config.json", 
        "railway.json",
        "railway.toml"
    ]
    
    required_dirs = [
        "backend",
        "frontend",
        ".taskmaster",
        "docs"
    ]
    
    missing = []
    
    for file_name in required_files:
        if not (project_root / file_name).exists():
            missing.append(f"FILE: {file_name}")
            
    for dir_name in required_dirs:
        if not (project_root / dir_name).exists():
            missing.append(f"DIR: {dir_name}")
            
    if not missing:
        print("  Project structure: [OK] COMPLETE")
        return {"project_structure": "[OK] COMPLETE"}
    else:
        print(f"  Project structure: [FAIL] Missing: {', '.join(missing)}")
        return {"project_structure": f"[FAIL] Missing: {', '.join(missing)}"}

def test_claude_config():
    """Test Claude Desktop configuration"""
    print("[CLAUDE] Testing Claude Desktop MCP configuration...")
    
    config_file = Path("C:/Users/je2al/Desktop/3.PSO-zscore/claude-desktop-mcp-config.json")
    
    if not config_file.exists():
        print("  Claude config: [FAIL] Config file not found")
        return {"claude_config": "[FAIL] Config file not found"}
        
    try:
        with open(config_file, 'r') as f:
            config_data = json.load(f)
            
        server_count = len(config_data.get("mcpServers", {}))
        servers = list(config_data.get("mcpServers", {}).keys())
        
        print(f"  Claude config: [OK] {server_count} MCP servers configured")
        print(f"  Servers: {', '.join(servers)}")
        
        return {"claude_config": f"[OK] {server_count} servers: {', '.join(servers)}"}
        
    except Exception as e:
        print(f"  Claude config: [ERROR] {str(e)}")
        return {"claude_config": f"[ERROR] {str(e)}"}

def main():
    """Run all tests"""
    print("=" * 60)
    print("PSO+Zscore MCP Tools Integration Test Suite")
    print("=" * 60)
    
    all_results = {}
    
    # Run all tests
    all_results.update(test_npm_mcp_tools())
    print()
    all_results.update(test_uv_tools())
    print()
    all_results.update(test_railway_connection())
    print()
    all_results.update(test_project_structure())
    print()
    all_results.update(test_claude_config())
    
    # Generate summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    total_tests = len(all_results)
    passed = len([r for r in all_results.values() if "[OK]" in r])
    failed = len([r for r in all_results.values() if "[FAIL]" in r or "[ERROR]" in r])
    
    print(f"Total Tests: {total_tests}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    
    if failed == 0:
        print("\n[SUCCESS] All tests passed! MCP tools are ready for use.")
    else:
        print(f"\n[WARNING] {failed} tests failed. Check the details above.")
        
    # Save results
    report_file = Path("C:/Users/je2al/Desktop/3.PSO-zscore/mcp-test-results.json")
    report_data = {
        "timestamp": datetime.now().isoformat(),
        "summary": {"total": total_tests, "passed": passed, "failed": failed},
        "results": all_results
    }
    
    with open(report_file, 'w') as f:
        json.dump(report_data, f, indent=2)
        
    print(f"\nTest report saved to: {report_file}")

if __name__ == "__main__":
    main()
