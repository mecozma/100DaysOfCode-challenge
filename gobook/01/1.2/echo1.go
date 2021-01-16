// Echo1 prints its command-line arguments.
package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	var sep string
	for i := 0; i < len(os.Args); i++ {
		sep = " "
		fmt.Println(strconv.Itoa(i) + sep + os.Args[i])
	}
}
