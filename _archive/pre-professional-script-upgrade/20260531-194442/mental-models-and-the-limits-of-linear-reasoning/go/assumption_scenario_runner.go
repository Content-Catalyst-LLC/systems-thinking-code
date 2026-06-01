package main

import "fmt"

func main() {
    scenarios := map[string]float64{
        "linear_pressure_only": 0.36,
        "feedback_aware_diagnosis": 0.70,
        "boundary_critique_added": 0.81,
        "participatory_system_model": 0.88,
    }
    for name, score := range scenarios {
        fmt.Printf("%s overall_score=%.2f\n", name, score)
    }
}
