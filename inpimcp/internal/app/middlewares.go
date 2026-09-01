package app

import (
	"context"
	"log"

	"github.com/modelcontextprotocol/go-sdk/mcp"
)

func loggingMiddleware() mcp.Middleware {
	return func(mh mcp.MethodHandler) mcp.MethodHandler {
		return func(ctx context.Context, method string, req mcp.Request) (result mcp.Result, err error) {
			log.Printf("→ %s", method)
			result, err = mh(ctx, method, req)
			
			if err != nil {
				log.Printf("← %s failed: %v", method, err)
			} else {
				log.Printf("← %s ok", method)
			}
			
			return result, err
		}
	}
}
