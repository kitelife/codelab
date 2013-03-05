package main

import "fmt"
import "time"

var c chan int

func ready(w string, sec int) {
	time.Sleep(int64(sec) * 1e9)
	fmt.Println(w, "is ready!")
	c <- 1
}

func main() {
	c = make(chan int)
	go ready("Tea", 2)
	go ready("Coffee", 1)
	fmt.Println("I'm waiting, but not too long")
	ch1, ch2 := <-c
	ch3, ch4 := <-c
	fmt.Printf("ch1=%v, ch2=%v\n",ch1,ch2)
	fmt.Printf("ch3=%v, ch4=%v\n",ch3,ch4)
}
