package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {
	sentence := "asSASA ddd dsjkdsjs dk"
	//number := 0
	/*
		for pos, char := range sentence {
			if char !=' ' {
				number ++
			}
		}
		fmt.Printf("number=%d\n",number)
		Rune, width := utf8.DecodeRuneInString(sentence)
		fmt.Printf("Rune=%v, width=%v\n",Rune,width)
	*/
	fmt.Printf("String %s\nLength: %d, Runes: %d\n", sentence,
		len([]byte(sentence)), utf8.RuneCount([]byte(sentence)))
	sliceStr := []byte(sentence)
	sliceStr[4], sliceStr[5], sliceStr[6] = 'a', 'b', 'c'
	sentence = string(sliceStr)
	fmt.Printf("changed sentence is %s\n", sentence)
}
