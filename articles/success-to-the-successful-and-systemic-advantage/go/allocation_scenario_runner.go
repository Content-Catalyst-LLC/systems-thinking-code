package main

import "fmt"

func main() {
    performanceWeight := 0.45
    needWeight := 0.30
    improvementWeight := 0.20
    score := performanceWeight*40 + needWeight*85 + improvementWeight*65
    fmt.Printf("need_adjusted_allocation_score=%.2f\n", score)
}
