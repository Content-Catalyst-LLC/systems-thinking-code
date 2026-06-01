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
	outPath := filepath.Join("outputs", "tables", "go_learning_loop_output.csv")
	os.MkdirAll(filepath.Dir(outPath), 0755)

	file, err := os.Create(outPath)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	writer := csv.NewWriter(file)
	defer writer.Flush()

	writer.Write([]string{"period", "learning_stock", "defensive_routines"})
	learning := 34.0
	defensiveness := 42.0

	for period := 0; period <= 36; period++ {
		writer.Write([]string{
			fmt.Sprintf("%d", period),
			fmt.Sprintf("%.3f", learning),
			fmt.Sprintf("%.3f", defensiveness),
		})
		learningFlow := 0.70*4.5 + 0.68*3.8 - defensiveness*0.035
		forgetting := defensiveness * 0.025
		learning = clamp(learning+learningFlow-forgetting, 0.0, 100.0)
		defensiveness = clamp(defensiveness+1.0-0.68*2.4, 0.0, 100.0)
	}

	fmt.Println("Wrote", outPath)
}
