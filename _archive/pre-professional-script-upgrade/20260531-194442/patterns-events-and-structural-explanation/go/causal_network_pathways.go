package main

import "fmt"

type Edge struct {
	Source string
	Target string
	Sign   string
}

func main() {
	edges := []Edge{
		{"maintenance_backlog", "response_delay", "+"},
		{"response_delay", "public_trust", "-"},
		{"workload_pressure", "institutional_capacity", "-"},
		{"institutional_capacity", "response_delay", "-"},
		{"structural_risk", "event_frequency", "+"},
	}

	for _, edge := range edges {
		fmt.Printf("%s --(%s)--> %s\n", edge.Source, edge.Sign, edge.Target)
	}
}
