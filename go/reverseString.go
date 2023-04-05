package main

import "fmt"

/*
func main() {
	s := "foobar"
	a := []byte(s)
	// Reverse a
	for i, j := 0, len(a)-1; i < j; i, j = i+1, j-1 {
		a[i], a[j] = a[j], a[i]
	}
	fmt.Printf("%s\n", string(a))
}
*/
func main() {

	str := "foobar"
	length := len(str)

	reverseStr := make([]byte, length)

	for index := 0; index < length; index++ {
		reverseStr[index] = str[length-1-index]
	}

	fmt.Printf("str is %s\n", str)
	fmt.Printf("reverseStr is %s\n", reverseStr)
}
