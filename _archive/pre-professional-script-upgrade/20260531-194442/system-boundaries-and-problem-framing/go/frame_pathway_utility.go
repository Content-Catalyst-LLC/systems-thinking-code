package main

import "fmt"

var framePathways = map[string][]string{
	"Technical Frame":     {"Repair", "Optimize", "Standardize"},
	"Institutional Frame": {"Coordinate", "Fund", "Govern", "Account"},
	"Justice Frame":      {"Include", "Redistribute", "Repair", "Protect"},
	"Ecological Frame":   {"Restore", "Conserve", "Adapt", "Regenerate"},
}

func main() {
	for frame, pathways := range framePathways {
		fmt.Printf("%s -> %v\n", frame, pathways)
	}
}
