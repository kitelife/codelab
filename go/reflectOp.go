package main

import (
	"fmt"
	"reflect"
)

type User struct {
	Username string
}

type Admin struct {
	User
	title string
}

func main() {
	var u Admin
	t := reflect.TypeOf(u)

	for i, n := 0, t.NumField(); i < n; i++ {
		f := t.Field(i)
		fmt.Println(f.Name, f.Type)
	}

	// 如果是指针，应该先使用Elem方法获取目标类型，指针本身是没有字段成员的
	uP := new(Admin)
	tP := reflect.TypeOf(uP)
	if tP.Kind() == reflect.Ptr {
		tP = tP.Elem()
	}
	for i, n := 0, t.NumField(); i < n; i++ {
		f := tP.Field(i)
		fmt.Println(f.Name, f.Type)
	}
}
