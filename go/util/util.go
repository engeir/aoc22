package util

import (
	"io/ioutil"
	"strings"
)


// Read the input file for a given day.
func ReadInput(day string) []string {
    data, err := ioutil.ReadFile("./../../input/day" + day + ".txt")
    if err != nil {
        panic(err)
    }
    contents := string(data)
    lines := strings.Split(contents, "\n")
    return lines
}
