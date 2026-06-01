package main

import "fmt"

func clamp(x, low, high float64) float64 {
	if x < low { return low }
	if x > high { return high }
	return x
}

func main() {
	engagement := 55.0
	risk := 22.0
	trust := 72.0
	for t := 0; t < 36; t++ {
		engagement = clamp(engagement + 3.0 - risk*0.02, 0, 100)
		risk = clamp(risk + engagement*0.035 - trust*0.025, 0, 100)
		trust = clamp(trust - risk*0.05 + 1.1, 0, 100)
	}
	fmt.Printf("platform feedback runner: engagement=%.3f risk=%.3f trust=%.3f\n", engagement, risk, trust)
}
