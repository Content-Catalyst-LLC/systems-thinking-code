package main

import "fmt"

func main() {
	paths := [][]string{
		{"resource_flow", "institutional_capacity", "response_delay", "public_trust"},
		{"maintenance_backlog", "institutional_capacity", "response_delay", "public_trust"},
		{"stress_load", "adaptive_capacity", "institutional_capacity", "response_delay"},
	}

	fmt.Println("causal_pathways")
	for _, path := range paths {
		for i, node := range path {
			if i > 0 {
				fmt.Print(" -> ")
			}
			fmt.Print(node)
		}
		fmt.Println()
	}
}
