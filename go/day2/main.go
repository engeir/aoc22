package main

import (
	"errors"
	"fmt"

	"github.com/engeir/aoc22/go/util"
)

func part1() {
	lines := util.ReadInput("2")
	values := 0
	for _, line := range lines {
		val, err := rules1(line)
		if err != nil {
			panic(err)
		}
		values += val
	}
	fmt.Println(values) // 11767
}

func part2() {
	lines := util.ReadInput("2")
	values := 0
	for _, line := range lines {
		val, err := rules2(line)
		if err != nil {
			panic(err)
		}
		values += val
	}
	fmt.Println(values) // 13886
}

func rules1(value string) (int, error) {
	switch value {
	case "A X":
		return 3 + 1, nil
	case "A Y":
		return 6 + 2, nil
	case "A Z":
		return 0 + 3, nil
	case "B X":
		return 0 + 1, nil
	case "B Y":
		return 3 + 2, nil
	case "B Z":
		return 6 + 3, nil
	case "C X":
		return 6 + 1, nil
	case "C Y":
		return 0 + 2, nil
	case "C Z":
		return 3 + 3, nil
	case "":
		return 0, nil
	default:
		fmt.Println(value)
		return 0, errors.New("What is this value: " + value)
	}
}

func rules2(value string) (int, error) {
	switch value {
	case "A X":
		return 0 + 3, nil
	case "A Y":
		return 3 + 1, nil
	case "A Z":
		return 6 + 2, nil
	case "B X":
		return 0 + 1, nil
	case "B Y":
		return 3 + 2, nil
	case "B Z":
		return 6 + 3, nil
	case "C X":
		return 0 + 2, nil
	case "C Y":
		return 3 + 3, nil
	case "C Z":
		return 6 + 1, nil
	case "":
		return 0, nil
	default:
		fmt.Println(value)
		return 0, errors.New("What is this value: " + value)
	}
}

func main() {
	part1()
	part2()
}
