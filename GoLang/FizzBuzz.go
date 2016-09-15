package main

import "fmt"

func main() {

	for number := 1; number <= 100; number++ {
		if (number%3 == 0) && (number%5 == 0) {
			fmt.Printf("FizzBuzz\n")
			continue
		}
		if number%3 == 0 {
			fmt.Printf("Fizz\n")
			continue
		}
		if number%5 == 0 {
			fmt.Printf("Buzz\n")
			continue
		} else {
			fmt.Printf("%d\n", number)
		}

	}
}
