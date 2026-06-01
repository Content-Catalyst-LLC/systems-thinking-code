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
	outPath := filepath.Join("outputs", "tables", "go_overshoot_output.csv")
	os.MkdirAll(filepath.Dir(outPath), 0755)

	file, err := os.Create(outPath)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	writer := csv.NewWriter(file)
	defer writer.Flush()

	writer.Write([]string{"period", "resource_stock", "consumption", "regeneration"})
	resource := 82.0
	for period := 0; period <= 36; period++ {
		consumption := clamp(0.62*9.0+max(0.0, 70.0-resource)*0.04, 0.0, 100.0)
		regeneration := clamp(0.50*6.0+2.5, 0.0, 100.0)
		writer.Write([]string{
			fmt.Sprintf("%d", period),
			fmt.Sprintf("%.3f", resource),
			fmt.Sprintf("%.3f", consumption),
			fmt.Sprintf("%.3f", regeneration),
		})
		resource = clamp(resource-consumption+regeneration, 0.0, 100.0)
	}

	fmt.Println("Wrote", outPath)
}

func max(a, b float64) float64 {
	if a > b {
		return a
	}
	return b
}
