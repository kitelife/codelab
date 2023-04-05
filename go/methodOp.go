package main

/*
根据调用者不同，方法分为两种表现形式：

instance.method(args...) ---> <type>.func(instance, args...)

前者称为 method value, 后者 method expression

两者都可像普通函数那样赋值和传参，
区别在于method value绑定实例，而method expression则须显式传参

需要注意, method value 会复制 receiver
*/

import (
	"fmt"
)

type User struct {
	id   int
	name string
}

func (self *User) Test() {
	fmt.Printf("%p, %v\n", self, self)
}

func main() {
	u := User{1, "Tom"}
	u.Test()

	mValue := u.Test
	mValue() // 隐式传递 receiver

	mExpression := (*User).Test
	mExpression(&u) // 显式传递 receiver
}
