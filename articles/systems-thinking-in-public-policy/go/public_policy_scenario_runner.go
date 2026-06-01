package main
import "fmt"
func clamp(v float64) float64 { if v < 0 { return 0 }; if v > 100 { return 100 }; return v }
func nextOutcome(outcome, effort, burden, capacity float64) float64 { return clamp(outcome + 0.2*effort - 0.25*burden + 0.1*capacity) }
func main() { fmt.Printf("Synthetic policy outcome: %.2f
", nextOutcome(42, 35, 24, 55)) }
