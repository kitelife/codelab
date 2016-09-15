package main

import "fmt"

func main() {

	index := 0

here:
	fmt.Printf("index = %d\n", index)
	index++
	if index < 10 {
		goto here
	}
}
