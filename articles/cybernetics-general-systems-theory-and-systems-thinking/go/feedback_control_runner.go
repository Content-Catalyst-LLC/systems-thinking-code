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

func abs(value float64) float64 {
	if value < 0 {
		return -value
	}
	return value
}

func main() {
	outPath := filepath.Join("outputs", "tables", "go_feedback_control_output.csv")
	os.MkdirAll(filepath.Dir(outPath), 0755)

	file, err := os.Create(outPath)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	writer := csv.NewWriter(file)
	defer writer.Flush()

	writer.Write([]string{"period", "system_state", "error_signal", "control_action"})
	state := 46.0
	goal := 70.0

	for period := 0; period <= 36; period++ {
		errorSignal := goal - state
		controlAction := clamp(abs(errorSignal)*0.42, 0.0, 100.0)
		writer.Write([]string{
			fmt.Sprintf("%d", period),
			fmt.Sprintf("%.3f", state),
			fmt.Sprintf("%.3f", errorSignal),
			fmt.Sprintf("%.3f", controlAction),
		})
		direction := 1.0
		if errorSignal < 0 {
			direction = -1.0
		}
		state = clamp(state+direction*controlAction*0.18-1.2, 0.0, 100.0)
	}

	fmt.Println("Wrote", outPath)
}
