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
	outPath := filepath.Join("outputs", "tables", "go_complexity_scenario_output.csv")
	os.MkdirAll(filepath.Dir(outPath), 0755)

	file, err := os.Create(outPath)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	writer := csv.NewWriter(file)
	defer writer.Flush()

	writer.Write([]string{"period", "readiness", "harm", "learning"})
	readiness := 34.0
	harm := 62.0
	learning := 36.0

	for period := 0; period <= 36; period++ {
		writer.Write([]string{
			fmt.Sprintf("%d", period),
			fmt.Sprintf("%.3f", readiness),
			fmt.Sprintf("%.3f", harm),
			fmt.Sprintf("%.3f", learning),
		})
		learning = clamp(learning+2.0-harm*0.01, 0.0, 100.0)
		readiness = clamp(readiness+learning*0.05-harm*0.03, 0.0, 100.0)
		harm = clamp(harm-readiness*0.04+0.8, 0.0, 100.0)
	}

	fmt.Println("Wrote", outPath)
}
