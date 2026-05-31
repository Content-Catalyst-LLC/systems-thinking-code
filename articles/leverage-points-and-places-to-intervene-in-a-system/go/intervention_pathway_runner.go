// Minimal Go scaffold for intervention pathway comparison.
package main

import "fmt"

type Intervention struct {
	Name  string
	Level string
	Score float64
}

func main() {
	items := []Intervention{
		{"Reduce administrative burden", "rule", 0.82},
		{"Community feedback loop", "information_flow", 0.88},
		{"Preventive maintenance", "stock_flow", 0.74},
	}
	for _, item := range items {
		fmt.Printf("%s | %s | %.2f\n", item.Name, item.Level, item.Score)
	}
}
