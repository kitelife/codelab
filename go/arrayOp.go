package main

// 数组是值类型,赋值和传参会复制整个数组, 不是指针
// 值拷贝行为会造成性能问题,通常会建议使用slice,或数组指针

import (
	"fmt"
)

// 数组传值
func test(x [2]int) {
	fmt.Printf("x: %p\n", &x)
	x[1] = 1000
}

// slice传结构，不传底层数据
func test2(y []int) {
	fmt.Printf("y: %p\n", &y)
	y[1] = 1000
}

// 传数组指针
func test3(z *[2]int) {
	fmt.Printf("z: %p\n", z)
	z[1] = 1001
}

func main() {
	a := [2]int{}
	fmt.Printf("a: %p\n", &a)
	test(a)
	fmt.Println(a)
	//
	b := []int{100, 200}
	fmt.Printf("b: %p\n", &b)
	test2(b)
	fmt.Println(b)
	//
	c := [2]int{1, 2}
	fmt.Printf("c: %p\n", &c)
	test3(&c)
	fmt.Println(c)
}
