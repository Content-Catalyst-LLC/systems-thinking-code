package main

import "fmt"

func classifyLoop(negativeLinks int) string {
	if negativeLinks%2 == 0 {
		return "reinforcing"
	}
	return "balancing"
}

func main() {
	fmt.Println("negative_links,loop_type")
	for i := 0; i <= 5; i++ {
		fmt.Printf("%d,%s\n", i, classifyLoop(i))
	}
}
