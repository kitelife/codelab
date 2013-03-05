package main

import "fmt"

func main() {

	fmt.Printf("%d\n",Factorial(10))
}

func Factorial(x int) (result int) {
	if x == 0{
		result = 1
	}else {
		result = x * Factorial(x-1)
	}
	return
}
