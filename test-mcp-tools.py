#!/usr/bin/env python3
"""
MCP Tools Integration Test Suite for PSO+Zscore Trading Application
Tests all configured MCP tools and validates functionality
"""
import subprocess
import json
import os
import sys
from datetime import datetime
from pathlib import Path

class MCPToolsTester:
    def __init__(self):
        self.project_root = Path("C:/Users/je2al/Desktop/3.PSO-zscore")
        self.results = {}
        
    def test_npm_packages(self):
        """Test Node.js MCP packages installation"""
        npm_packages = [
            "@jasontanswe/railway-mcp",
            "@playwright/mcp", 
            "@modelcontextprotocol/server-filesystem",
            "@magicuidesign/cli",
            "@sentry/mcp-server",
            "@browsermcp/mcp",
            "@modelcontextprotocol/server-sequential-thinking",
            "@supabase/mcp-server-supabase",
            "mcp-server-code-runner"
        ]
        
        print("🔍 Testing NPM MCP packages...")
        for package in npm_packages:
            try:
                result = subprocess.run(
                    ["npm", "list", "-g", package],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                status = "✅ INSTALLED" if result.returncode == 0 else "❌ NOT FOUND"
                self.results[f"npm_{package.replace('/', '_').replace('@', '')}"] = {
                    "status": status,
                    "package": package
                }
                print(f"  {package}: {status}")
            except Exception as e:
                self.results[f"npm_{package.replace('/', '_').replace('@', '')}"] = {
                    "status": f"❌ ERROR: {str(e)}",
                    "package": package
                }
                print(f"  {package}: ❌ ERROR: {str(e)}")
                
    def test_uv_packages(self):
        """Test UV Python packages installation"""
        uv_packages = [
            "tradingview-chart-mcp",
            "task-master-ai"
        ]
        
        print("🐍 Testing UV Python packages...")
        for package in uv_packages:
            try:
                result = subprocess.run(
                    ["uv", "tool", "list"],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                status = "✅ INSTALLED" if package in result.stdout else "❌ NOT FOUND"
                self.results[f"uv_{package.replace('-', '_')}"] = {
                    "status": status,
                    "package": package
                }
                print(f"  {package}: {status}")
            except Exception as e:
                self.results[f"uv_{package.replace('-', '_')}"] = {
                    "status": f"❌ ERROR: {str(e)}",
                    "package": package
                }
                print(f"  {package}: ❌ ERROR: {str(e)}")
                
    def test_railway_connection(self):
        """Test Railway CLI connection"""
        print("🚂 Testing Railway connection...")
        try:
            # Test railway login status
            result = subprocess.run(
                ["railway", "whoami"],
                capture_output=True, 
                text=True,
                timeout=10
            )
            
            if result.returncode == 0:
                self.results["railway_connection"] = {
                    "status": "✅ CONNECTED",
                    "user": result.stdout.strip()
                }
                print(f"  Railway: ✅ CONNECTED as {result.stdout.strip()}")
            else:
                self.results["railway_connection"] = {
                    "status": "❌ NOT CONNECTED",
                    "error": result.stderr
                }
                print(f"  Railway: ❌ NOT CONNECTED")
                
        except Exception as e:
            self.results["railway_connection"] = {
                "status": f"❌ ERROR: {str(e)}",
                "error": str(e)
            }
            print(f"  Railway: ❌ ERROR: {str(e)}")
            
    def test_taskmaster_integration(self):
        """Test TaskMaster integration"""
        print("📋 Testing TaskMaster integration...")
        try:
            # Check if TaskMaster is properly configured
            tasks_file = self.project_root / ".taskmaster" / "tasks" / "tasks.json"
            if tasks_file.exists():
                with open(tasks_file, 'r') as f:
                    tasks_data = json.load(f)
                    
                task_count = len(tasks_data.get("tasks", []))
                self.results["taskmaster_integration"] = {
                    "status": f"✅ CONFIGURED",
                    "tasks_count": task_count,
                    "tasks_file": str(tasks_file)
                }
                print(f"  TaskMaster: ✅ CONFIGURED with {task_count} tasks")
            else:
                self.results["taskmaster_integration"] = {
                    "status": "❌ NOT CONFIGURED",
                    "error": "tasks.json not found"
                }
                print(f"  TaskMaster: ❌ NOT CONFIGURED")
                
        except Exception as e:
            self.results["taskmaster_integration"] = {
                "status": f"❌ ERROR: {str(e)}",
                "error": str(e)
            }
            print(f"  TaskMaster: ❌ ERROR: {str(e)}")
            
    def test_claude_desktop_config(self):
        """Test Claude Desktop MCP configuration"""
        print("🤖 Testing Claude Desktop MCP configuration...")
        
        config_file = self.project_root / "claude-desktop-mcp-config.json"
        if config_file.exists():
            try:
                with open(config_file, 'r') as f:
                    config_data = json.load(f)
                    
                server_count = len(config_data.get("mcpServers", {}))
                self.results["claude_desktop_config"] = {
                    "status": "✅ CONFIGURED",
                    "servers_count": server_count,
                    "config_file": str(config_file)
                }
                print(f"  Claude Desktop: ✅ CONFIGURED with {server_count} MCP servers")
                
                # List configured servers
                servers = list(config_data.get("mcpServers", {}).keys())
                print(f"  Configured servers: {', '.join(servers)}")
                
            except Exception as e:
                self.results["claude_desktop_config"] = {
                    "status": f"❌ INVALID CONFIG: {str(e)}",
                    "error": str(e)
                }
                print(f"  Claude Desktop: ❌ INVALID CONFIG: {str(e)}")
        else:
            self.results["claude_desktop_config"] = {
                "status": "❌ NOT FOUND",
                "error": "claude-desktop-mcp-config.json not found"
            }
            print(f"  Claude Desktop: ❌ CONFIG NOT FOUND")
            
    def test_project_structure(self):
        """Test project structure integrity"""
        print("📁 Testing project structure...")
        
        required_dirs = [
            "backend",
            "frontend", 
            ".taskmaster",
            "docs",
            "tests"
        ]
        
        required_files = [
            "README.md",
            "railway.json",
            "railway.toml",
            "mcp-config.json",
            "claude-desktop-mcp-config.json"
        ]
        
        missing_dirs = []
        missing_files = []
        
        for dir_name in required_dirs:
            if not (self.project_root / dir_name).exists():
                missing_dirs.append(dir_name)
                
        for file_name in required_files:
            if not (self.project_root / file_name).exists():
                missing_files.append(file_name)
                
        if not missing_dirs and not missing_files:
            self.results["project_structure"] = {
                "status": "✅ COMPLETE",
                "dirs_count": len(required_dirs),
                "files_count": len(required_files)
            }
            print(f"  Project Structure: ✅ COMPLETE")
        else:
            self.results["project_structure"] = {
                "status": "❌ INCOMPLETE",
                "missing_dirs": missing_dirs,
                "missing_files": missing_files
            }
            print(f"  Project Structure: ❌ INCOMPLETE")
            if missing_dirs:
                print(f"    Missing directories: {', '.join(missing_dirs)}")
            if missing_files:
                print(f"    Missing files: {', '.join(missing_files)}")
                
    def generate_report(self):
        """Generate comprehensive test report"""
        report_file = self.project_root / "mcp-tools-test-report.json"
        
        report_data = {
            "timestamp": datetime.now().isoformat(),
            "project_root": str(self.project_root),
            "test_results": self.results,
            "summary": {
                "total_tests": len(self.results),
                "passed": len([r for r in self.results.values() if "✅" in str(r.get("status", ""))]),
                "failed": len([r for r in self.results.values() if "❌" in str(r.get("status", ""))])
            }
        }
        
        with open(report_file, 'w') as f:
            json.dump(report_data, f, indent=2)
            
        print(f"\n📊 Test Report Generated: {report_file}")
        return report_data
        
    def run_all_tests(self):
        """Run all MCP tools tests"""
        print("🧪 PSO+Zscore MCP Tools Integration Test Suite")
        print("=" * 60)
        
        self.test_npm_packages()
        print()
        self.test_uv_packages()
        print()
        self.test_railway_connection()
        print()
        self.test_taskmaster_integration()
        print()
        self.test_claude_desktop_config()
        print()
        self.test_project_structure()
        print()
        
        report = self.generate_report()
        
        print("\n" + "=" * 60)
        print("📈 TEST SUMMARY")
        print("=" * 60)
        print(f"Total Tests: {report['summary']['total_tests']}")
        print(f"Passed: {report['summary']['passed']} ✅")
        print(f"Failed: {report['summary']['failed']} ❌")
        
        if report['summary']['failed'] == 0:
            print("\n🎉 ALL TESTS PASSED! MCP tools are ready for use.")
        else:
            print(f"\n⚠️  {report['summary']['failed']} tests failed. Review the report for details.")
            
        return report

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "install":
        print("🚀 Installing MCP tools...")
        subprocess.run(["C:/Users/je2al/Desktop/3.PSO-zscore/install-mcp-tools.bat"], shell=True)
        print("\n")
    
    tester = MCPToolsTester()
    tester.run_all_tests()

if __name__ == "__main__":
    main()
