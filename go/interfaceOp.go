package main

/*
某些时候，让函数直接“实现”接口能省不少事
*/

import (
	"fmt"
)

type Tester interface {
	Do()
}

type FuncDo func()

func (self FuncDo) Do() { self() }

func main() {
	var t Tester = FuncDo(func() { fmt.Println("Hello, World!") })
	t.Do()
}
