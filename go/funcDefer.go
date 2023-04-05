package main

import (
	"fmt"
)

func println(params ...interface{}) {
	paramNum := len(params)
	for index, param := range params {
		fmt.Printf("%v", param)
		if index < paramNum-1 {
			fmt.Printf(" ")
		}
	}
	fmt.Println()
}

func add(x, y int) (z int) {
	defer func() {
		println(z) // 输出: 203
	}()

	z = x + y
	return z + 200 // 执行顺序: (z = z + 200) -> (call defer) -> (ret)
}

func main() {
	println(add(1, 2)) // 输出: 203
}
