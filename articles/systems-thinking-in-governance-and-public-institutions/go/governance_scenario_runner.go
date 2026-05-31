package main

import "fmt"

func main() {
    scenarios := map[string]float64{
        "status_quo": 0.49,
        "burden_reduction": 0.62,
        "capacity_building": 0.67,
        "participatory_learning_governance": 0.81,
    }
    for name, score := range scenarios {
        fmt.Printf("%s public_value_score=%.2f\n", name, score)
    }
}
