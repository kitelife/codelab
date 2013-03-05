package main

import "fmt"

func getcmdargs(args ...int){
	for _,arg := range args {
		fmt.Printf("%d\n",arg)
	}
}

func main() {
	getcmdargs(100,200,101)
	println()
	getcmdargs(11,21,32)
}
