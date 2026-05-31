package main

import "fmt"

type Flow struct {
	Name      string
	Direction string
	Rate      float64
}

func netChange(flows []Flow) float64 {
	total := 0.0
	for _, flow := range flows {
		if flow.Direction == "inflow" {
			total += flow.Rate
		} else {
			total -= flow.Rate
		}
	}
	return total
}

func main() {
	flows := []Flow{
		{"reliable_service", "inflow", 3.2},
		{"unresolved_harm", "outflow", 2.6},
		{"repair_action", "inflow", 1.1},
	}
	fmt.Printf("net social stock change: %.2f\n", netChange(flows))
}
