package main

//  简单工厂模式打包并发任务和 channel。

import (
	"fmt"
	"math/rand"
	"time"
)

func NewTest() chan int {
	c := make(chan int)
	rand.Seed(time.Now().UnixNano())

	go func() {
		time.Sleep(time.Second)
		c <- rand.Int()
	}()

	return c
}

func main() {
	t := NewTest()
	fmt.Println(<-t) // 等待goroutine结束返回
}
