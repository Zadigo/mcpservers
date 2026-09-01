package app

import (
	"context"
	"errors"
	"fmt"
	"log"
	"net/http"
	"os"
	"time"

	"github.com/modelcontextprotocol/go-sdk/mcp"
)

type App struct {
	ctx context.Context
	errCh chan error
	server *mcp.Server
}

func(a *App) Start() {
	a.errCh = make(chan error)

	if a.server == nil {
		log.Fatal("⚠️ Server is not defined")
	}

	// Create the streamable HTTP handler to listen to
	handler := mcp.NewStreamableHTTPHandler(func(req *http.Request) *mcp.Server {
		return a.server
	}, nil)

	go func() {
		log.Print("🟢 Starting MCP server...")
		log.Print("🟢 Listening on port 8000...")
		// a.errCh <- a.server.Run(a.ctx, &mcp.StdioTransport{})
		http.ListenAndServe(":8000", handler)
	}()

	select {
	case err := <- a.errCh:
		log.Printf("🔴 An error occured: %v", err)
	case <- a.ctx.Done():
		_, cancel := context.WithTimeout(context.Background(), 5*time.Second)
		defer cancel()

		err := errors.Join(fmt.Errorf("🔴 Shutting down %s HTTP server...", os.Getenv("SERVICE_NAME")), a.ctx.Err())
		log.Printf("🔴 An error occured: %v", err)

		close(a.errCh)
	}
}


func NewApp(ctx context.Context) *App {
	app := &App{ctx: ctx}

	serverImplementation := &mcp.Implementation{
		Name: "greeter", 
		Version: "v1.0.0",
	}

	serverOptions := &mcp.ServerOptions{}
	
	app.server = mcp.NewServer(serverImplementation, serverOptions)
	app.server.AddReceivingMiddleware(loggingMiddleware())
	app.addTools()
	
	return app
}
