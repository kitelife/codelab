package main

import "fmt"

func main() {
	result1,result2 := sort(7,2)
	fmt.Printf("%d,%d\n",result1,result2)
	result1,result2 = sort(2,7)
	fmt.Printf("%d,%d\n",result1,result2)
	result1,result2 = sort(10,10)
	fmt.Printf("%d,%d\n",result1,result2)
}

func sort(arg1,arg2 int)(first,second int) {
	switch{
		case arg1 <= arg2:
			first,second = arg1,arg2
		case arg1 > arg2:
			first,second = arg2,arg1
	}
	return
}
