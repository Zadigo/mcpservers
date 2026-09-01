package main

import (
	"context"
	"os"
	"os/signal"

	"github.com/Zadigo/inpimcp/internal/app"
)

func main() {
	ctx := context.Background()
	ctx, cancel := signal.NotifyContext(ctx, os.Interrupt)
	defer cancel()
	
	app := app.NewApp(ctx)
	app.Start()
}
