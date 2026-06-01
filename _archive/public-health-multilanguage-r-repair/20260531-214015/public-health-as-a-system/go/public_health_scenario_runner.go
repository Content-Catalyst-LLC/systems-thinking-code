package main

import "fmt"

func main() {
    susceptible := 99820.0
    infected := 180.0
    recovered := 0.0
    population := 100000.0
    beta := 0.39
    gamma := 0.20
    prevention := 0.42

    for week := 0; week <= 52; week++ {
        effectiveBeta := beta * (1.0 - prevention)
        newInfections := effectiveBeta * susceptible * infected / population
        if newInfections > susceptible { newInfections = susceptible }
        recoveries := gamma * infected
        if recoveries > infected { recoveries = infected }
        susceptible -= newInfections
        infected += newInfections - recoveries
        recovered += recoveries
    }

    fmt.Printf("Final infected: %.3f; recovered: %.3f\n", infected, recovered)
}
