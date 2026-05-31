package main

import "fmt"

func main() {
    scenarios := map[string]float64{
        "status_quo":                    0.48,
        "documentation_only":            0.58,
        "memory_authority_integration":  0.86,
    }
    for name, score := range scenarios {
        fmt.Printf("%s projected_memory_score=%.2f\n", name, score)
    }
}
