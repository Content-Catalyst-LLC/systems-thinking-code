// Paradigm scenario runner scaffold.
// Run with: go run paradigm_scenario_runner.go

package main

import "fmt"

type Paradigm struct {
	Name       string
	Access     float64
	Dignity    float64
	Burden     float64
	Resilience float64
}

func Score(p Paradigm) float64 {
	return 0.3*p.Access + 0.3*p.Dignity + 0.3*p.Resilience - 0.2*p.Burden
}

func main() {
	paradigms := []Paradigm{
		{"throughput", 0.45, 0.30, 0.80, 0.35},
		{"dignity", 0.78, 0.82, 0.30, 0.65},
		{"stewardship", 0.70, 0.74, 0.35, 0.90},
	}
	for _, p := range paradigms {
		fmt.Printf("%s score %.3f\n", p.Name, Score(p))
	}
}
