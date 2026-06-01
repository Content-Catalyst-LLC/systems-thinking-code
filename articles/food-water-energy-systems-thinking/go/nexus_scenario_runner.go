package main

import "fmt"

func main() {
	groundwater := 1000.0
	recharge := 28.0
	withdrawal := 55.0 * 1.18
	fmt.Println("year,groundwater")
	for year := 0; year <= 30; year++ {
		groundwater += recharge - withdrawal
		if groundwater < 0 {
			groundwater = 0
		}
		fmt.Printf("%d,%.3f\n", year, groundwater)
	}
}
