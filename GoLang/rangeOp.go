package main

import (
	"fmt"
)

/*
range 会复制对象

建议改用引用类型,其底层数据不会被复制

引用类型：slice、map、channel
*/

func main() {
	//
	a := [3]int{0, 1, 2}
	for i, v := range a { // index、value 都是从复制品中取出。

		if i == 0 {
			a[1], a[2] = 999, 999
			fmt.Println(a)
		}

		a[i] = v + 100
	}

	fmt.Println(a)

	//
	s := []int{1, 2, 3, 4, 5}
	for i, v := range s { // 复制 struct slice { pointer, len, cap }。
		if i == 0 {
			s = s[:3]  // 对 slice 的修改,不会影响 range
			s[2] = 100 // 对底层数据的修改
		}
		fmt.Printf("%d %d\n", i, v)
	}
}
