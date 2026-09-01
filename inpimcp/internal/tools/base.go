package tools

import (
	"context"

	"github.com/modelcontextprotocol/go-sdk/mcp"
)

type Input struct {
	Name string `json:"name" jsonschema:"the name of the person to greet"`
}

type Output struct {
	Greeting string `json:"greeting" jsonschema:"the greeting to tell to the user"`
}

type BaseTools struct {
	ctx context.Context
	server *mcp.Server
}

func(b *BaseTools) SetServer(ctx context.Context, server *mcp.Server) {
	b.ctx = ctx
	b.server = server
}

func(b *BaseTools) SimpleTool(ctx context.Context, ctr *mcp.CallToolRequest) (*mcp.CallToolResult, error) {
	return nil, nil
}
