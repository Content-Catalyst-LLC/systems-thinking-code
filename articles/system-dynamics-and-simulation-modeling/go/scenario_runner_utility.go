package main

import (
    "fmt"
    "os"
)

func main() {
    scenario := "baseline"
    if len(os.Args) > 1 {
        scenario = os.Args[1]
    }
    fmt.Println("System dynamics scenario runner scaffold")
    fmt.Printf("Scenario: %s\n", scenario)
    fmt.Println("Extend this utility to load scenario CSV files and execute model runs.")
}
