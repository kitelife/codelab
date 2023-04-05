package main

import "fmt"

func main() {

	for i := 0; i < 5; i++ {
		defer fmt.Printf("%d\n", i)
	}
	for i := 0; i < 5; i++ {
		fmt.Printf("%d\n", i)
	}
}
