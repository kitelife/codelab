package main

import "exec"
import "fmt"

func main() {
	cmd := exec.Command("/bin/ls", "-l")
	buf, err := cmd.Output()
	fmt.Printf("%s\n", string(buf))
}
