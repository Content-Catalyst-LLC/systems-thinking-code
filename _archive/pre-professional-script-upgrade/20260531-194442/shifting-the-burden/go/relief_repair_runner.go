package main

import (
	"fmt"
	"math"
)

type State struct {
	Pressure   float64
	Capacity   float64
	Dependency float64
}

func Step(state State, relief float64, repair float64) State {
	nextCapacity := math.Max(0, state.Capacity+0.7*repair-0.25*relief)
	nextDependency := math.Max(0, state.Dependency+0.015*relief-0.012*repair)
	nextPressure := math.Max(0, state.Pressure+4.0-0.4*relief-0.25*nextCapacity)
	return State{Pressure: nextPressure, Capacity: nextCapacity, Dependency: nextDependency}
}

func main() {
	state := State{Pressure: 80, Capacity: 55, Dependency: 0.3}
	for period := 0; period < 8; period++ {
		relief := 32.0 - float64(period*2)
		repair := 12.0 + float64(period*4)
		state = Step(state, relief, repair)
		fmt.Printf("period=%d pressure=%.2f capacity=%.2f dependency=%.3f\n", period, state.Pressure, state.Capacity, state.Dependency)
	}
}
