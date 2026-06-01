package main
import "fmt"
func nextStock(stock, regeneration, extraction, degradation float64) float64 { v := stock + regeneration - extraction - degradation; if v < 0 { return 0 }; return v }
func main() { fmt.Printf("Synthetic sustainability stock: %.2f
", nextStock(100, 4.2, 2.7, 0.4)) }
