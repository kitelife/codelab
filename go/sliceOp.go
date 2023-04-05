package main

import (
	"fmt"
)

func main() {
	//
	var x []int
	fmt.Printf("x: %v\n", x)
	fmt.Printf("len x: %d\n", len(x))
	fmt.Printf("cap x: %d\n", cap(x))
	//
	x2 := make([]int, 0, 10)
	fmt.Printf("x2: %v\n", x2)
	fmt.Printf("len x2: %d\n", len(x2))
	fmt.Printf("cap x2: %d\n", cap(x2))
	// 写不写省略号都一样
	y := [...]int{1, 2, 3, 4, 5}
	fmt.Printf("y: %v\n", y)
	//
	z := []int{100, 1, 2, 10}
	z[1] = z[1] + 1
	fmt.Printf("z: %v\n", z)

	s1 := []int{0, 1, 2, 3, 8: 100}
	fmt.Println(s1, len(s1), cap(s1))
	s2 := make([]int, 6, 8)
	fmt.Println(s2, len(s2), cap(s2))
	s3 := make([]int, 6)
	fmt.Println(s3, len(s3), cap(s3))
}
