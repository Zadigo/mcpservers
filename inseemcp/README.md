# INSEE MCP

This repository contains the code for the INSEE MCP (Model Context Protocol) application. The MCP is a framework for building and deploying machine learning models in a standardized way.

You can read more on the API by going to the [README](./components/resources/data/README.md) file.

## Commands

You can run the following commands to start the server, preview and test your app tools locally, and start the Huey task manager and inspector.

```Shell

# Start the MCP server
fastmcp run app.py:app

# Preview and test your app tools locally without a full MCP host
fastmcp dev apps app.py

# Start the Huey task manager

# Start the inspector
npx @modelcontextprotocol/inspector uv --directory /path/to/.venv/bin run fastmcp run /path/to/app.py:mcp
```

## Integration with LLMs

## Claude

```JSON
"INSEE MCP": {
  "command": "~/.local/bin/uv",
  "args": [
    "run",
    "--project",
    "path/to/inseemcp",
    "fastmcp",
    "run",
    "path/to/app.py:mcp"
  ],
  "env": {}
}
```
