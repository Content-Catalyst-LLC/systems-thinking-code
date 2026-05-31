package main

import "fmt"

type Edge struct {
	From string
	To   string
	Sign int
}

func main() {
	edges := []Edge{{"policy pressure", "actor adaptation", 1}, {"actor adaptation", "intended effect", -1}}
	for _, e := range edges {
		fmt.Printf("%s -> %s sign=%d\n", e.From, e.To, e.Sign)
	}
}
