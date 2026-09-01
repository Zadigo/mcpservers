package tests

import (
	"context"
	"testing"
	"time"

	"github.com/Zadigo/inpimcp/internal/app"
)

func TestServer(t *testing.T) {
	ctx, cancel := context.WithTimeout(t.Context(), 60 * time.Second)
	defer cancel()
	
	server := app.NewApp(ctx)

	t.Run("should start server", func(t *testing.T) {
		server.Start()
	})
}
