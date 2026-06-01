package main
import "fmt"
func nextOutcome(outcome, effort, burden, capacity float64) float64 { v := outcome + 0.2*effort - 0.25*burden + 0.1*capacity; if v < 0 { return 0 }; if v > 100 { return 100 }; return v }
func main() { fmt.Printf("Synthetic policy outcome: %.2f
", nextOutcome(42, 35, 24, 55)) }
