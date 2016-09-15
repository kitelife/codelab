package main

import (
	"bufio"
	"fmt"
	"net"
)

func main() {

	l, err := net.Listen("tcp", "127.0.0.1:8053")
	if err != nil {
		fmt.Printf("Failure to listen: %s\n", err.String())
	}
	for {
		//如果希望使用并发处理连接，可将Echo函数的调用方式改为goroutine.
		if c, err := l.Accept(); err == nil {
			Echo(c)
		}
	}
}

func Echo(c net.Conn) {

	defer c.Close()
	line, err := bufio.NewReader(c).ReadString('\n')
	if err != nil {
		fmt.Printf("Failure to read: %s\n", err.String())
		return
	}
	_, err = c.Write([]byte(line))
	if err != nil {
		fmt.Printf("Failure to write: %s\n", err.String())
		return
	}
}
