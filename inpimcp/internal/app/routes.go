package app

import (
	"github.com/Zadigo/inpimcp/internal/tools"
	"github.com/modelcontextprotocol/go-sdk/mcp"
)

type TestInput struct {
	firstName string
}

func (a *App) addTools() {
	baseTools := &tools.BaseTools{}
	baseTools.SetServer(a.ctx, a.server)
	
	schema := map[string]any{
		"type":       "object",
		"properties": map[string]any{},
	}
	
	a.server.AddTool(&mcp.Tool{Name: "Great", Description: "Say hi", InputSchema: schema}, baseTools.SimpleTool)
}
