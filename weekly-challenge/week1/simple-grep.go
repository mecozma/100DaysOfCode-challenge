/*
Given a filename and a string on the commandline, print all lines from the file
that contain the string.
Example: grep world input.txt
input.txt
    Hello world,
    today is Monday
    and I say hello
    to the world.
Output:
    Hello world,
    to the world.
*/
package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	// Check if the right number of arguments is passed.
	if len(os.Args) < 3 {
		fmt.Println("Please provide the search string and the source" +
			" file")
		return
	}
	// Declare and assign the word to search for variable.
	search := os.Args[1]
	// Open the file and check if there are no errors.
	file, err := os.Open(os.Args[2])
	if err != nil {
		log.Fatal(err)
	}
	// Close file after all the processes ended.
	defer file.Close()

	// Initialize and assign a new scanner.
	scanner := bufio.NewScanner(file)

	// Initialised a slice to hold each line in the input file.
	var textLines []string

	// Iterate over the scanner and append each line to the textLine slice.
	for scanner.Scan() {
		textLines = append(textLines, scanner.Text())
	}
	// Check if the scanner is returning an error and log it.
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	/* Iterate over the textLines slice and check if it contains the
	wanted word. */
	for _, eachLine := range textLines {
		ll := strings.ToLower(eachLine)
		if strings.Contains(ll, search) {
			fmt.Println(eachLine)
		}
	}

}
