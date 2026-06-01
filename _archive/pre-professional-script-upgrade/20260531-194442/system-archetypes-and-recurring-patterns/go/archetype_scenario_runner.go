package main

import (
	"fmt"
	"math"
)

func limitsToGrowth(x, r, k float64) float64 {
	return x + r*x*(1-x/k)
}

func main() {
	x := 8.0
	r := 0.32
	k := 100.0

	fmt.Println("time,state")
	for t := 0; t <= 30; t++ {
		fmt.Printf("%d,%.4f\n", t, x)
		x = limitsToGrowth(x, r, k)
		x = math.Max(0, x)
	}
}
