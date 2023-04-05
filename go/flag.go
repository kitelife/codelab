package main

import (
	"flag"
	"fmt"
	"os"
)

func main() {

	dnssec := flag.Bool("dnssec", false, "Request DNSSEC records")
	port := flag.String("port", "53", "Set the query port")
	flag.Usage = func() {
		fmt.Fprintf(os.Stderr, "Usage: %s [OPTIONS] [name ...]\n", os.Args[0])
		flag.PrintDefaults()
	}
	flag.Parse()
	fmt.Printf("dnssec: %v\n", *dnssec)
	fmt.Printf("port: %v\n", *port)
	flag.Usage()
}
