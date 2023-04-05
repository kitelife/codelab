package main

import (
	"exec"
	"flag"
	"fmt"
	"os"
	"strings"
)

func main() {
	outfile := flag.String("o", "a.out", "specify the name of output file")
	infile := flag.String("i", "", "specify the input file")
	flag.Usage = func() {

		fmt.Fprintf(os.Stderr, "Usage: %s [OPTIONS] [name ...]\n", os.Args[0])
		flag.PrintDefaults()
	}
	flag.Parse()
	if *infile == "" {

		flag.Usage()
	} else {
		cmd := exec.Command("8g", *infile)
		buf, err := cmd.Output()
		fmt.Printf("%s\n", string(buf))
		if err == nil {
			linkfile := strings.Replace(*infile, ".go", ".8", -1)
			cmd = exec.Command("8l", "-o", *outfile, linkfile)
			buf, err = cmd.Output()
			fmt.Printf("%s\n", string(buf))
		}
	}
}
