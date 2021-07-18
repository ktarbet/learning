package main

import (
	"fmt"
	"math"
)

func f(x float64) float64 {
	return 3*math.Pow(x, 3) - 5
}

func Newton(f func(float64) float64, guess float64) float64 {
	x := guess
	max_iterations := 20
	tolerance := 0.001
	dx := 0.00001
	for i := 0; i < max_iterations; i++ {
		//		fmt.Println("x=", x, ", y= ", f(x))

		if math.Abs(f(x)) < tolerance {
			break
		}
		m := (f(x+dx) - f(x)) / dx
		x = x - f(x)/m
	}
	return x
}

func main() {

	x := Newton(f, 0.1)
	fmt.Println("x=", x)
	fmt.Println("y=", f(x))

	fmt.Println()
}
