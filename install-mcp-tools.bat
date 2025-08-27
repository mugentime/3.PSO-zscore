@echo off
echo 🚀 Installing MCP Tools for PSO+Zscore Trading Application
echo ================================================================

echo 📦 Installing Node.js MCP packages globally...
call npm install -g @jasontanswe/railway-mcp
call npm install -g @playwright/mcp
call npm install -g @modelcontextprotocol/server-filesystem
call npm install -g @magicuidesign/cli
call npm install -g @sentry/mcp-server
call npm install -g @browsermcp/mcp
call npm install -g @modelcontextprotocol/server-sequential-thinking

echo 🐍 Installing Python MCP packages with UV...
call uv tool install tradingview-chart-mcp
call uv tool install task-master-ai

echo 🔧 Installing additional development tools...
call npm install -g @supabase/mcp-server-supabase
call npm install -g @apify/actors-mcp-server
call npm install -g mcp-server-code-runner

echo ✅ MCP Tools installation completed!
echo 📋 Next steps:
echo    1. Copy mcp-config.json to Claude Desktop configuration
echo    2. Restart Claude Desktop
echo    3. Test MCP tools integration

pause
