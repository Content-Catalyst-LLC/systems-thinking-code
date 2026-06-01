package main

import "fmt"

func main() {
	pathway := []string{"Individual", "Team", "Organization", "Institution", "Network", "Socio-Ecological Region"}
	fmt.Println("Cross-scale pathway:")
	for i, step := range pathway {
		fmt.Printf("%d. %s\n", i+1, step)
	}
}
