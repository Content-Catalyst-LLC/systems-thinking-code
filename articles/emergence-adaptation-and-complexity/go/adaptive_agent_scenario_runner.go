package main

import "fmt"

func clamp01(x float64) float64 {
	if x < 0 { return 0 }
	if x > 1 { return 1 }
	return x
}

func main() {
	agents := 40
	states := make([]float64, agents)
	for i := range states { states[i] = float64((i*17)%100) / 100.0 }
	for t := 0; t < 20; t++ {
		next := make([]float64, agents)
		for i := range states {
			left := states[(i-1+agents)%agents]
			right := states[(i+1)%agents]
			local := (left + right) / 2.0
			next[i] = clamp01(states[i] + 0.18*(local-states[i]))
		}
		states = next
	}
	sum := 0.0
	for _, v := range states { sum += v }
	fmt.Printf("Go adaptive scenario final mean: %.4f\n", sum/float64(agents))
}
