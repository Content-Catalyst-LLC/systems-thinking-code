package main

import "fmt"

func main() {
    scenarios := map[string]float64{
        "overtime_only":          0.82,
        "hiring_without_redesign": 0.70,
        "full_capacity_redesign":  0.38,
    }
    for name, risk := range scenarios {
        fmt.Printf("%s projected_burnout_risk=%.2f\n", name, risk)
    }
}
