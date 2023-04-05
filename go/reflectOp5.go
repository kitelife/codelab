package main

import (
	"fmt"
	"reflect"
)

// 利用Make、New等函数，可实现近似泛型操作

var (
	Int    = reflect.TypeOf(0)
	String = reflect.TypeOf("")
)

func Make(T reflect.Type, fptr interface{}) {
	// 实际创建slice的包装函数
	swap := func(in []reflect.Value) []reflect.Value {
		// --- 省略算法内容 --- //

		// 返回和类型匹配的 slice 对象
		return []reflect.Value{
			reflect.MakeSlice(
				reflect.SliceOf(T), // slice Type
				int(in[0].Int()),   // len
				int(in[1].Int()),   // cap
			),
		}
	}
	// 传入的是函数变量指针，因为我们要将变量指向 swap 函数
	fn := reflect.ValueOf(fptr).Elem()

	// 获取函数指针类型，生成所需 swap function Value
	v := reflect.MakeFunc(fn.Type(), swap)

	// 修改函数指针实际指向，也就是swap
	fn.Set(v)
}

func main() {
	var makeints func(int, int) []int
	var makestrings func(int, int) []string

	// 用相同算法，生成不同类型创建函数
	Make(Int, &makeints)
	Make(String, &makestrings)

	// 按实际类型使用
	x := makeints(5, 10)
	fmt.Printf("%#v\n", x)

	s := makestrings(3, 10)
	fmt.Printf("cap: %d\n", cap(s))
	fmt.Printf("len: %d\n", len(s))
	fmt.Printf("%#v\n", s)
}
