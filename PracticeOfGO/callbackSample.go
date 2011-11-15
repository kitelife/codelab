package main

import "fmt"

func main() {
	callback(5,printit)
}

func printit(x int) {
	fmt.Printf("value is %v\n", x)
}

func callback(y int, f func(int)) {
	f(y)
}
