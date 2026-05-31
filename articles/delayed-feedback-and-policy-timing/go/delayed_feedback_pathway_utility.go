package main

import "fmt"

type Pathway struct {
	Name string
	LagMonths int
}

func main() {
	pathways := []Pathway{{"effect", 18}, {"information", 6}, {"decision", 4}, {"implementation", 10}}
	total := 0
	for _, p := range pathways {
		total += p.LagMonths
	}
	fmt.Printf("total_delay_months=%d\n", total)
}
