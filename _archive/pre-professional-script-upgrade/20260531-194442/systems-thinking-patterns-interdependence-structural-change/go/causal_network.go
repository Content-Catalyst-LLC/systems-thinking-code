package main

import "fmt"

type Edge struct {
	From     string
	To       string
	Polarity string
}

func main() {
	edges := []Edge{
		{"Learning", "Adaptive Capacity", "+"},
		{"Adaptive Capacity", "Resilience", "+"},
		{"Disruption Pressure", "Capacity", "-"},
		{"Public Trust", "Cooperation", "+"},
		{"Administrative Burden", "Public Trust", "-"},
	}

	outDegree := map[string]int{}

	for _, edge := range edges {
		outDegree[edge.From]++
		if _, exists := outDegree[edge.To]; !exists {
			outDegree[edge.To] = 0
		}
	}

	fmt.Println("Causal network out-degree:")
	for node, degree := range outDegree {
		fmt.Printf("%s: %d\n", node, degree)
	}
}
