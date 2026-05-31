package main

import "fmt"

type Edge struct {
	Source string
	Target string
	Sign   int
}

func main() {
	edges := []Edge{
		{"Public Trust", "Cooperation", 1},
		{"Cooperation", "Service Performance", 1},
		{"Service Performance", "Public Trust", 1},
	}
	fmt.Println("Causal pathway utility scaffold")
	for _, e := range edges {
		label := "+"
		if e.Sign < 0 {
			label = "-"
		}
		fmt.Printf("%s --%s--> %s\n", e.Source, label, e.Target)
	}
}
