package main

import "fmt"

func main() {
	graph := map[string][]string{
		"resource_flow":           {"institutional_capacity"},
		"institutional_capacity": {"response_delay"},
		"response_delay":         {"public_trust"},
		"public_trust":           {"service_demand"},
		"service_demand":         {"response_delay"},
	}

	fmt.Println("Causal network adjacency list")
	for source, targets := range graph {
		fmt.Printf("%s -> %v\n", source, targets)
	}
}
