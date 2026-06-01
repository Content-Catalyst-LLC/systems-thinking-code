package main

import "fmt"

func clamp(x float64) float64 {
	if x < 0 { return 0 }
	if x > 100 { return 100 }
	return x
}

func main() {
	congestion := 50.0
	affordability := 42.0
	infrastructure := 60.0
	displacement := 45.0
	for year := 0; year <= 30; year++ {
		congestion = clamp(congestion + 0.5 + displacement*0.01 - affordability*0.005)
		affordability = clamp(affordability + 0.4 - congestion*0.012 - displacement*0.008)
		infrastructure = clamp(infrastructure + 0.55 - 1.1 - congestion*0.01)
		displacement = clamp(displacement + congestion*0.006 - affordability*0.004)
	}
	resilience := clamp((100-congestion)*0.25 + affordability*0.25 + infrastructure*0.30 + (100-displacement)*0.20)
	fmt.Printf("Urban scenario runner: congestion=%.2f affordability=%.2f infrastructure=%.2f displacement=%.2f resilience=%.2f\n", congestion, affordability, infrastructure, displacement, resilience)
}
