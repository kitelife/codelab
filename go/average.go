package main

import "fmt"

func main() {

	float64Slice := []float64{100, 3, 89, 34131}
	/*
		var sum float64
		sum = 0.0
		for _,value := range float64Slice {
			sum += value
		}
		average := sum / float64(len(float64Slice))
		fmt.Printf("average:%v\n",average)
	*/
	sum, ave := 0.0, 0.0
	switch len(float64Slice) {
	case 0:
		ave = 0
	default:
		for _, v := range float64Slice {
			sum += v
		}
		ave = sum / float64(len(float64Slice))
	}
	fmt.Printf("ave: %v\n", ave)
}
