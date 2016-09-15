package main

import "fmt"

func main() {

	list := []string{"a", "b", "c", "d", "e", "f"}
	for k, v := range list {
		fmt.Printf("list[%d] = %s\n", k, v)
	}
}
