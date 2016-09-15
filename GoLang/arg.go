package main

import "fmt"

func main() {
	showArg(1, 2, 3)
}

func showArg(arg ...int) {
	for _, n := range arg {
		fmt.Printf("And the number is: %d\n", n)
	}
}
