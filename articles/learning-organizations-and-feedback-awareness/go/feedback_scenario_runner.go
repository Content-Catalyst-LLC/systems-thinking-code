package main

import "fmt"

func main() {
    scenarios := []string{"survey_only", "feedback_aware_redesign", "repair_oriented_learning"}
    for _, scenario := range scenarios {
        fmt.Println("Running learning scenario:", scenario)
    }
}
