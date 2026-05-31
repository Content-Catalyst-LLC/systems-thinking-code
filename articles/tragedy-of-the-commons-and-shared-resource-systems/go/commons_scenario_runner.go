package main

import "fmt"

func main() {
    stock := 1000.0
    capacity := 1400.0
    regenRate := 0.22
    annualUse := 120.0
    for year := 0; year < 25; year++ {
        regeneration := regenRate * stock * (1.0 - stock/capacity)
        if regeneration < 0 {
            regeneration = 0
        }
        stock = stock + regeneration - annualUse
        if stock < 0 {
            stock = 0
        }
    }
    fmt.Printf("Final synthetic commons stock: %.2f\n", stock)
}
