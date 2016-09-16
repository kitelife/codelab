package main

// 用channel实现信号量（semaphore）

import (
	"fmt"
	"sync"
)

func main() {
	wg := sync.WaitGroup{}
	wg.Add(3)

	sem := make(chan int, 1)

	for i := 0; i < 3; i++ {
		go func(id int) {
			defer wg.Done()

			sem <- 1 // 向sem发送数据，阻塞或者成功

			for x := 0; x < 3; x++ {
				fmt.Println(id, x)
			}

			<-sem // 接收数据，使得其他阻塞 goroutine 可以发送数据
		}(i)
	}

	wg.Wait()
}
