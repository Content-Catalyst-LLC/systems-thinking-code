package main

import "fmt"

func resilience(delay float64, repair float64) float64 {
	value := 0.68 - 0.035*delay + 1.2*repair - 1.4*0.05
	if value < 0 {
		return 0
	}
	if value > 1 {
		return 1
	}
	return value
}

func main() {
	for delay := 3.0; delay <= 12.0; delay += 3.0 {
		fmt.Printf("delay %.1f -> resilience %.3f\n", delay, resilience(delay, 0.08))
	}
}
