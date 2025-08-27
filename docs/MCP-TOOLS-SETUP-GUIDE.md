# 🛠️ MCP Tools Configuration Guide - PSO+Zscore Trading App

## 🎯 Overview
This guide covers the complete setup and configuration of Claude MCP (Model Context Protocol) tools for your PSO+Zscore Trading Application. MCP tools provide direct integration between Claude and your development environment.

## 📋 MCP Tools Inventory

### 🚂 Infrastructure & Deployment
- **@jasontanswe/railway-mcp** - Enhanced Railway deployment (146+ tools)
- **@sentry/mcp-server** - Error monitoring and debugging
- **@supabase/mcp-server-supabase** - Database operations

### 🌐 Browser Automation & Testing  
- **@playwright/mcp** - Playwright browser automation
- **@browsermcp/mcp** - Advanced browser control
- **mcp-server-code-runner** - Code execution and testing

### 📊 Trading & Analytics
- **tradingview-chart-mcp** - TradingView chart analysis
- **task-master-ai** - Project task management

### 🎨 Development & UI
- **@magicuidesign/cli** - UI component generation
- **@modelcontextprotocol/server-filesystem** - File operations
- **@modelcontextprotocol/server-sequential-thinking** - Problem solving

## 🚀 Quick Setup

### 1. Install All MCP Tools
```bash
# Run the automated installer
./install-mcp-tools.bat

# Or install manually:
npm install -g @jasontanswe/railway-mcp @playwright/mcp @magicuidesign/cli
uv tool install tradingview-chart-mcp task-master-ai
```

### 2. Configure Claude Desktop
```bash
# Copy the optimized configuration
copy claude-desktop-mcp-config.json %APPDATA%\Claude\claude_desktop_config.json

# Or manually place in Claude Desktop config location:
# Windows: %APPDATA%\Claude\claude_desktop_config.json
# macOS: ~/Library/Application Support/Claude/claude_desktop_config.json
# Linux: ~/.config/claude/claude_desktop_config.json
```

### 3. Test MCP Tools Integration
```bash
# Run comprehensive test suite
python test-mcp-tools.py

# Or test with installation
python test-mcp-tools.py install
```

### 4. Restart Claude Desktop
- Close Claude Desktop completely
- Restart Claude Desktop 
- Verify MCP tools are loaded (check status indicators)

## 🔧 Configuration Details

### Railway Integration
```json
{
  "railway-enhanced": {
    "command": "npx",
    "args": ["@jasontanswe/railway-mcp"],
    "env": {
      "RAILWAY_TOKEN": "e0ae87e0-75e3-4db6-bebe-8286df2b7a10"
    }
  }
}
```

**Available Commands:**
- Deploy applications
- Manage environment variables
- View logs and metrics
- Scale services
- Manage databases

### TaskMaster Integration
```json
{
  "taskmaster": {
    "command": "uv",
    "args": [
      "tool", "run", "task-master-ai",
      "--project-root", "C:\\Users\\je2al\\Desktop\\3.PSO-zscore"
    ],
    "env": {
      "ANTHROPIC_API_KEY": "YOUR_ANTHROPIC_API_KEY_HERE"
    }
  }
}
```

**Available Commands:**
- Create and manage tasks
- Generate development plans
- Track project progress
- Run research queries
- Optimize workflows

### TradingView Integration  
```json
{
  "tradingview": {
    "command": "uv",
    "args": ["tool", "run", "tradingview-chart-mcp"]
  }
}
```

**Available Commands:**
- Generate chart snapshots
- Analyze technical indicators
- Fetch market data
- Create trading signals

### Browser Automation
```json
{
  "playwright": {
    "command": "npx",
    "args": ["@playwright/mcp"],
    "env": {
      "PLAYWRIGHT_BROWSERS_PATH": "0"
    }
  }
}
```

**Available Commands:**
- Automate web interactions
- Run integration tests
- Capture screenshots
- Extract web data

## 🧪 Testing & Validation

### Run Test Suite
The `test-mcp-tools.py` script validates:

1. **Package Installation** - Verifies all MCP packages are installed
2. **Railway Connection** - Tests Railway CLI authentication
3. **TaskMaster Integration** - Validates project configuration
4. **Claude Desktop Config** - Checks MCP configuration syntax
5. **Project Structure** - Ensures all required files exist

### Expected Test Results
```bash
🧪 PSO+Zscore MCP Tools Integration Test Suite
============================================================

🔍 Testing NPM MCP packages...
  @jasontanswe/railway-mcp: ✅ INSTALLED
  @playwright/mcp: ✅ INSTALLED
  @magicuidesign/cli: ✅ INSTALLED
  # ... more packages

🐍 Testing UV Python packages...
  tradingview-chart-mcp: ✅ INSTALLED
  task-master-ai: ✅ INSTALLED

🚂 Testing Railway connection...
  Railway: ✅ CONNECTED as your-email@domain.com

📋 Testing TaskMaster integration...
  TaskMaster: ✅ CONFIGURED with 15 tasks

🤖 Testing Claude Desktop MCP configuration...
  Claude Desktop: ✅ CONFIGURED with 10 MCP servers

📁 Testing project structure...
  Project Structure: ✅ COMPLETE

============================================================
📈 TEST SUMMARY
============================================================
Total Tests: 25
Passed: 25 ✅ 
Failed: 0 ❌

🎉 ALL TESTS PASSED! MCP tools are ready for use.
```

## 🚨 Troubleshooting

### Common Issues

#### 1. NPM Package Installation Failures
```bash
# Clear npm cache
npm cache clean --force

# Install with verbose logging
npm install -g @jasontanswe/railway-mcp --verbose

# Check global npm path
npm list -g --depth=0
```

#### 2. UV Tool Installation Failures  
```bash
# Update UV
uv self update

# Install with specific Python version
uv tool install tradingview-chart-mcp --python 3.11

# List installed tools
uv tool list
```

#### 3. Railway Connection Issues
```bash
# Re-login with token
railway login --token e0ae87e0-75e3-4db6-bebe-8286df2b7a10

# Check authentication status
railway whoami

# Verify project connection
railway status
```

#### 4. Claude Desktop Not Loading MCP Tools
1. **Check configuration file location:**
   ```bash
   # Windows
   type "%APPDATA%\Claude\claude_desktop_config.json"
   
   # Verify JSON syntax
   python -m json.tool claude-desktop-mcp-config.json
   ```

2. **Restart Claude Desktop completely:**
   - Close all Claude windows
   - End Claude processes in Task Manager
   - Restart Claude Desktop

3. **Check MCP server status:**
   - Look for MCP indicators in Claude interface
   - Test individual tools with simple commands

#### 5. Permission Issues (Windows)
```bash
# Run as Administrator
# Set execution policy for PowerShell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Check PATH variables
echo $env:PATH
```

### Debug Commands

```bash
# Test individual MCP servers
npx @jasontanswe/railway-mcp --help
uv tool run tradingview-chart-mcp --version
npx @playwright/mcp --version

# Check environment variables
echo $RAILWAY_TOKEN
echo $ANTHROPIC_API_KEY

# Validate JSON configuration
python -c "import json; print(json.load(open('claude-desktop-mcp-config.json')))"

# Test filesystem access
npx @modelcontextprotocol/server-filesystem "C:\Users\je2al\Desktop\3.PSO-zscore" --help
```

## 🎯 Usage Examples

### Railway Deployment
```
Claude: "Deploy the PSO+Zscore app to Railway"
# Uses @jasontanswe/railway-mcp to handle deployment
```

### Task Management
```  
Claude: "Show me the next task in the development plan"
# Uses task-master-ai to query TaskMaster
```

### Trading Analysis
```
Claude: "Generate a BTCUSDT 4-hour chart snapshot"  
# Uses tradingview-chart-mcp to create chart
```

### Browser Testing
```
Claude: "Test the frontend React app in Chrome"
# Uses @playwright/mcp for automated testing
```

### UI Development
```
Claude: "Create a trading dashboard component"
# Uses @magicuidesign/cli for UI generation
```

## 📊 Success Metrics

When properly configured, you should have:

✅ **10+ MCP servers** active in Claude Desktop  
✅ **Railway integration** for seamless deployment  
✅ **TaskMaster integration** for project management  
✅ **TradingView integration** for market analysis  
✅ **Browser automation** for testing  
✅ **File system access** for code operations  
✅ **Real-time debugging** capabilities  
✅ **Automated deployment** pipeline  
✅ **UI component generation** tools  
✅ **Code execution** environment  

## 🔄 Maintenance

### Weekly Tasks
- Update MCP packages: `npm update -g && uv tool upgrade --all`
- Test MCP functionality: `python test-mcp-tools.py`
- Review Claude Desktop logs for errors
- Verify Railway connection: `railway whoami`

### Monthly Tasks  
- Review and optimize MCP configurations
- Update Claude Desktop if new version available
- Audit and rotate API keys
- Performance review of MCP integrations

## 🎉 Next Steps

With MCP tools configured, you can now:

1. **Continue with Task 3:** Configure Railway deployment pipeline
2. **Use Claude + MCP** for accelerated development
3. **Deploy automatically** via Railway integration  
4. **Manage tasks** through TaskMaster integration
5. **Generate charts** with TradingView integration
6. **Test applications** with browser automation
7. **Create UI components** with MagicUI integration

Your PSO+Zscore trading application now has **enterprise-grade Claude integration** for professional development workflows! 🚀

