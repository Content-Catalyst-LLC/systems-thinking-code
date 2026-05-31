package main

import "fmt"

func main() {
    stages := []string{"signal", "reporting", "decision", "implementation", "visible_effect"}
    for i, stage := range stages {
        fmt.Printf("%d: %s\n", i+1, stage)
    }
}
