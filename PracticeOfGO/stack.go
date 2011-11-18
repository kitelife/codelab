package main

import "fmt"
import "strconv"
/*
type stackMethods interface {

	push(int)
	pop() int
	String()
}
*/

const maxlen = 100

type arrayfixedlen [maxlen]int

type stack struct {
	pointer int
	maxium int
	array arrayfixedlen
}

func (st *stack) push(element int) {
	if st.pointer < st.maxium {
		st.array[st.pointer] = element
		fmt.Printf("Push %d into stack\n",element)
		st.pointer ++
	}else{
		fmt.Printf("Can not push %d into stack\n",element)
	}
	return
}

func (st *stack) pop()(element int) {
	if st.pointer > 0 {
		element = st.array[st.pointer - 1]
		fmt.Printf("Pop %d outof stack\n",element)
		st.pointer --
	}else{
		fmt.Printf("Sorry, There is no element in stack\n")
	}
	return
}

func (st *stack) String() string {

	var str string
	for i := st.pointer-1; i >= 0; i-- {
		str = str + "[" +
					strconv.Itoa(i) + ":" + strconv.Itoa(st.array[i]) + "]"
	}
	return str
}

func main() {
	st := new(stack)
	st.pointer = 0
	st.maxium = maxlen
	for index := 0; index < maxlen+1; index++ {
		st.push(index + 2)
	}
//	for index := 0; index < 100; index++ {
//		st.pop()
//	}
	fmt.Printf("left content of stack: %s\n",st)
}
