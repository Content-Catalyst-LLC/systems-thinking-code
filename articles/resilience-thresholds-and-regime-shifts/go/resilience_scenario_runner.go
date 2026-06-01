package main

import "fmt"

func clamp(v, low, high float64) float64 {
	if v < low { return low }
	if v > high { return high }
	return v
}

func main() {
	resilience := 78.0
	pressure := 35.0
	for year := 0; year <= 20; year++ {
		pressure += 2.3
		resilience = clamp(resilience + 1.4 - 2.1 - pressure*0.02, 0, 100)
		margin := resilience - pressure
		regime := "recoverable"
		if margin <= 0 { regime = "shifted" } else if margin <= 10 { regime = "near_threshold" }
		fmt.Printf("%02d resilience=%.2f pressure=%.2f margin=%.2f regime=%s\n", year, resilience, pressure, margin, regime)
	}
}
