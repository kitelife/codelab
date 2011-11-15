package main

import "fmt"

func main() {
	f64Slice := []float64{123.0,3131.312,32}
	fmt.Printf("%v\n",avg(f64Slice))
}

func avg(f64Slice []float64)(average float64) {
	sum := 0.0
	for _, v := range f64Slice {
		sum += v
	}
	average = sum / float64(len(f64Slice))
	return
}
