package main

import (
	"fmt"
	"unsafe"
)

func main() {
	d := struct {
		s string
		x int
	}{"abc", 100}

	p := uintptr(unsafe.Pointer(&d)) // *struct -> Pointer -> uintptr
	p += unsafe.Offsetof(d.x)        // uintptr + offset
	p2 := unsafe.Pointer(p)          // Pointer -> *int
	px := (*int)(p2)                 // d.x = 200
	*px = 200

	fmt.Printf("%#v\n", d)
}
