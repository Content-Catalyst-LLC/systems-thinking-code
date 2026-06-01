package main

import (
	"fmt"
	"math"
)

func forcing(co2 float64) float64 {
	return 5.35 * math.Log(co2/280.0)
}

func main() {
	co2 := 420.0
	emissions := 40.0
	temp := 1.2
	heat := 0.0
	feedback := 1.28
	for year := 0; year <= 80; year++ {
		emissions *= 0.96
		co2 += (emissions / 7.8) * 0.55
		f := forcing(co2)
		heat += f * 0.035
		target := 0.78 * f * feedback
		temp += 0.10*(target-temp) + heat*0.006
	}
	fmt.Printf("Final synthetic CO2 ppm: %.2f\n", co2)
	fmt.Printf("Final synthetic temperature anomaly: %.3f C\n", temp)
}
