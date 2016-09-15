package main

import "fmt"
import "reflect"

type Person struct {
	Name string "namestr" //"namestr" is tag , and Name's first character must be upper for function Set
	age  int
}

func show(i interface{}) {
	switch t := i.(type) {
	case *Person:
		to := reflect.TypeOf(i)
		v := reflect.ValueOf(i)
		tag := to.Elem().Field(0).Tag
		name := v.Elem().Field(0).String()
		fmt.Printf("type is %v\nvalue is %v\ntag of field0 is %v\nname of field0 is %v\n", to, v, tag, name)
	default:
		fmt.Printf("Not Person Type")
	}
}

func Set(i interface{}) {
	switch i.(type) {
	case *Person:
		r := reflect.ValueOf(i)
		r.Elem().Field(0).
			SetString("Albert Einstein")
	default:
		fmt.Printf("Not Person type, so can not set")
	}
}

func main() {
	p1 := new(Person)
	Set(p1)
	show(p1)
}
