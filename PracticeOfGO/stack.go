package main

import "fmt"

type arraylen10 [10]int

type stack struct {
	pointer int
	maxium int
	array arraylen10
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

func main() {
	st := new(stack)
	st.pointer = 0
	st.maxium = 10
	for index := 0; index < 100; index++ {
		st.push(index)
	}
	for index := 0; index < 100; index++ {
		st.pop()
	}
}
