package main

import "fmt"

func main() {
	dependencies := map[string]float64{
		"water_utility_on_power_grid": 0.70,
		"hospital_on_power_grid":      0.55,
		"telecom_on_power_grid":       0.60,
	}
	threshold := 0.50
	for name, load := range dependencies {
		status := "absorbs"
		if load > threshold {
			status = "fails"
		}
		fmt.Printf("%s load=%.2f threshold=%.2f status=%s\n", name, load, threshold, status)
	}
}
