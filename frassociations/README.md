## Commands

```Shell

# Start the MCP server
fastmcp run app.py:app

# Preview and test your app tools locally without a full MCP host
fastmcp dev apps app.py

# Start the Huey task manager

# Start the inspector
npx @modelcontextprotocol/inspector uv --directory /path/to/.venv/bin run fastmcp run /path/to/app.py:mcp
```

## Claude

```JSON

"French Associations": {
  "command": "~/.local/bin/uv",
  "args": [
    "run",
    "--project",
    "path/to/frelectedofficials",
    "fastmcp",
    "run",
    "path/to/app.py:mcp"
  ],
  "env": {}
}
```
