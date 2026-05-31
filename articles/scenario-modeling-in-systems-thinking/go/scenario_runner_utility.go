package main

import (
	"fmt"
)

type Scenario struct {
	Name           string
	CapacityGrowth float64
	DemandGrowth   float64
}

func main() {
	scenarios := []Scenario{
		{"baseline", 0.01, 0.03},
		{"early_prevention", 0.03, 0.025},
		{"stress_case", 0.00, 0.05},
	}

	for _, s := range scenarios {
		margin := s.CapacityGrowth - s.DemandGrowth
		fmt.Printf("%s robustness margin: %.3f\n", s.Name, margin)
	}
}
