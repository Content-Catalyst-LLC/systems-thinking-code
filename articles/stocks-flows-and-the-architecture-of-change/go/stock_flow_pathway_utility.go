package main

import "fmt"

type Flow struct {
	Name string
	Rate float64
	Kind string
}

func main() {
	flows := []Flow{{"trust_building", 4.0, "inflow"}, {"trust_erosion", 5.0, "outflow"}}
	net := 0.0
	for _, flow := range flows {
		if flow.Kind == "inflow" {
			net += flow.Rate
		} else {
			net -= flow.Rate
		}
	}
	fmt.Printf("net stock change: %.2f\n", net)
}
