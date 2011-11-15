package main

import "fmt"

func main() {

	a := func() {
		println("Hello")
	}
	a()    //璋冪鍑芥
	fmt.Printf("%T\n",a)
}
