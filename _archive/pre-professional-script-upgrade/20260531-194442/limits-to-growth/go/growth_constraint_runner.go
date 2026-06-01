// Growth constraint runner scaffold.
package main

import "fmt"

func main() {
    scale := 100.0
    rate := 0.13
    capacity := 260.0
    for year := 0; year <= 20; year++ {
        pressure := scale / capacity
        fmt.Printf("year=%02d scale=%.2f pressure=%.3f\n", year, scale, pressure)
        scale += rate * scale * (1 - scale/capacity)
    }
}
