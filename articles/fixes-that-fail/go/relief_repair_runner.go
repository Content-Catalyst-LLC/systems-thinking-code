package main

import "fmt"

func main() {
	problem := 100.0
	capacity := 1.0
	for period := 0; period < 10; period++ {
		fix := 0.55 * problem / 130.0
		if fix > 1.0 {
			fix = 1.0
		}
		repair := 0.65
		capacity += 0.05*repair - 0.05*fix
		problem += 7.0 - 25.0*fix - 10.0*capacity
		if problem < 0 {
			problem = 0
		}
		fmt.Printf("period=%d problem=%.2f capacity=%.3f fix=%.3f\n", period, problem, capacity, fix)
	}
}
