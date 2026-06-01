package main

import "fmt"

func clamp(v float64) float64 {
	if v < 0 { return 0 }
	if v > 100 { return 100 }
	return v
}

func main() {
	risk := 31.0
	governance := 52.0
	fmt.Println("period,risk,governance")
	for period := 0; period <= 12; period++ {
		fmt.Printf("%d,%.3f,%.3f\n", period, risk, governance)
		risk = clamp(risk + 2.2 - governance*0.035)
		governance = clamp(governance + 1.1)
	}
}
