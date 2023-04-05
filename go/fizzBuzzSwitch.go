package main

import "fmt"

func main() {

	for nu := 1; nu <= 100; nu++ {
		switch {
		case (nu%3 == 0) && (nu%5 == 0):
			fmt.Printf("FizzBuzz\n")
		case nu%3 == 0:
			fmt.Printf("Fizz\n")
		case nu%5 == 0:
			fmt.Printf("Buzz\n")
		default:
			fmt.Printf("%d\n", nu)
		}
	}
}
