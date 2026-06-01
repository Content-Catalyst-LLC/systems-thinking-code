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
	outPath := filepath.Join("outputs", "tables", "go_social_diffusion_output.csv")
	os.MkdirAll(filepath.Dir(outPath), 0755)

	file, err := os.Create(outPath)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	writer := csv.NewWriter(file)
	defer writer.Flush()

	writer.Write([]string{"period", "adoption"})
	adoption := 18.0
	for period := 0; period <= 24; period++ {
		writer.Write([]string{fmt.Sprintf("%d", period), fmt.Sprintf("%.3f", adoption)})
		diffusion := 0.70 * adoption * (100.0 - adoption) / 100.0 * 0.08
		learning := 0.82 * 1.5
		resistance := 0.34 * adoption * 0.025
		adoption = clamp(adoption+diffusion+learning-resistance, 0.0, 100.0)
	}

	fmt.Println("Wrote", outPath)
}
