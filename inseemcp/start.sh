#!/bin/bash

root_dir="$(pwd)"
directory="$root_dir/.venv/bin"

npx @modelcontextprotocol/inspector uv --directory "$directory" run fastmcp run "$root_dir/app.py:mcp"
