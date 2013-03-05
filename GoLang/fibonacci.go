package main

import "fmt"

func Fibonacci(value int) []int {
	x := make([]int, value)
	x[0], x[1] = 1, 1
	for n := 2; n < value; n++ {
		x[n] = x[n-1] + x[n-2]
	}
	return x
}

func main() {

	for index, term := range Fibonacci(20) {
		fmt.Printf("%v: %v\n",index, term)
	}
}
