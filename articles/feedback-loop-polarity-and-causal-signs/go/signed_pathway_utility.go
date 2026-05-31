package main

import "fmt"

func loopPolarity(signs []int) string {
	product := 1
	for _, sign := range signs {
		product *= sign
	}
	if product > 0 {
		return "reinforcing"
	}
	return "balancing"
}

func main() {
	fmt.Println("Loop polarity:", loopPolarity([]int{1, 1, -1}))
}
