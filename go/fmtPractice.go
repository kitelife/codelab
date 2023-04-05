package main

import "fmt"

func main() {
	foo := "This is a simple string"
	fmt.Printf("%v\n", foo)
	fmt.Printf("%T\n", foo)
	fmt.Printf("%#v\n", foo)

	type InnerNode struct {
		X string
	}

	type Node struct {
		A string
		B int
		C InnerNode
	}
	c := InnerNode{
		X: "Hello",
	}
	n := Node{
		A: "world",
		B: 100,
		C: c,
	}

	fmt.Printf("%+v\n", n)
	fmt.Printf("%v\n", n)
	fmt.Printf("%#v\n", n)
	fmt.Printf("%T\n", n)
}
