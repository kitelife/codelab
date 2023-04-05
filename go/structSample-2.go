/**
 * Created with IntelliJ IDEA.
 * User: xiayf
 * Date: 13-8-17
 * Time: 下午1:06
 * To change this template use File | Settings | File Templates.
 */
package main

import "fmt"

type Human struct {
	name   string
	age    int
	weight int
}

/*
当匿名字段是一个struct的时候，那么这个struct所拥有的全部字段都被隐式地引入了当前定义的这个struct
*/

type Student struct {
	Human      // 匿名字段，那么默认Student就包含了Human的所有字段
	speciality string
}

func main() {
	mark := Student{Human{"Mark", 25, 120}, "Computer Science"}

	fmt.Println("His name is ", mark.name)
	fmt.Println("His age is ", mark.age)
	fmt.Println("His weight is ", mark.weight)
	fmt.Println("His speciality is ", mark.speciality)

	mark.speciality = "AI"
	fmt.Println("Mark changed his speciality")
	fmt.Println("His speciality is ", mark.speciality)

	fmt.Println("Mark become old")
	mark.age = 46
	fmt.Println("His age is ", mark.age)

	fmt.Println("Mark is not an athlet anymore")
	mark.weight += 60
	fmt.Println("His weight is ", mark.weight)
}
