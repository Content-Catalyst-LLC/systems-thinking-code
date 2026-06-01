package main

import (
	"encoding/csv"
	"fmt"
	"os"
	"path/filepath"
)

func clamp(value, low, high float64) float64 {
	if value < low {
		return low
	}
	if value > high {
		return high
	}
	return value
}

func main() {
	outPath := filepath.Join("outputs", "tables", "go_stock_flow_output.csv")
	os.MkdirAll(filepath.Dir(outPath), 0755)

	file, err := os.Create(outPath)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	writer := csv.NewWriter(file)
	defer writer.Flush()

	writer.Write([]string{"period", "backlog"})
	backlog := 58.0
	capacity := 46.0
	for period := 0; period <= 24; period++ {
		writer.Write([]string{fmt.Sprintf("%d", period), fmt.Sprintf("%.3f", backlog)})
		service := capacity * 0.42
		backlog = clamp(backlog+3.2-service, 0.0, 200.0)
	}

	fmt.Println("Wrote", outPath)
}
