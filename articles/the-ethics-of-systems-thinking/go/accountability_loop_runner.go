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
	outPath := filepath.Join("outputs", "tables", "go_accountability_loop_output.csv")
	os.MkdirAll(filepath.Dir(outPath), 0755)

	file, err := os.Create(outPath)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	writer := csv.NewWriter(file)
	defer writer.Flush()

	writer.Write([]string{"period", "accountability_index", "repair_stock", "cumulative_harm"})
	accountability := 42.0
	repair := 28.0
	harm := 60.0

	for period := 0; period <= 36; period++ {
		writer.Write([]string{
			fmt.Sprintf("%d", period),
			fmt.Sprintf("%.3f", accountability),
			fmt.Sprintf("%.3f", repair),
			fmt.Sprintf("%.3f", harm),
		})
		accountability = clamp(accountability+2.1, 0.0, 100.0)
		repair = clamp(repair+1.8, 0.0, 100.0)
		harm = clamp(harm-0.08*repair+0.02*(100.0-accountability), 0.0, 100.0)
	}

	fmt.Println("Wrote", outPath)
}
