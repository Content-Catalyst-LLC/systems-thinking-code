package main

import "fmt"

type PathwayStep struct {
	Name     string
	Pressure float64
	Stock    float64
}

func main() {
	steps := []PathwayStep{
		{"growth_pressure", 0.62, 0.70},
		{"delayed_feedback", 0.75, 0.58},
		{"buffer_depletion", 0.82, 0.44},
		{"correction", 0.68, 0.50},
	}
	for _, step := range steps {
		fmt.Printf("%s pressure=%.2f stock=%.2f\n", step.Name, step.Pressure, step.Stock)
	}
}
