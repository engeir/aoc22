package main

import (
	"fmt"
	"strings"

	"github.com/engeir/aoc22/go/util"
)

func part1() {
	lines := util.ReadInput("3")
	sum := 0
	for _, line := range lines {
		if len(line) != 0 {
			common := find_common_character(line)
			priority := lookup_table(common)
			sum += priority
		}
	}
	fmt.Println(sum) // 8202
}

func part2() {
	lines := util.ReadInput("3")
	sum := 0
	for i := 0; i < len(lines); i += 3 {
		var section []string
		if i > len(lines)-3 {
			section = lines[i:]
		} else {
			section = lines[i : i+3]
		}
		if len(section) == 3 {
			badge := find_badges(section)
			priority := lookup_table(badge)
			sum += priority
		}
	}
	fmt.Println(sum) // 2864
}

func find_common_character(chars string) string {
	p1 := chars[:len(chars)/2]
	p2 := chars[len(chars)/2:]
	for _, p := range p1 {
		if strings.Contains(p2, string(p)) {
			return string(p)
		}
	}
	return "None"
}

func lookup_table(common string) int {
	alph := "abcdefghijklmnopqrstovwxyz"
	idx := strings.Index(alph, strings.ToLower(common))
	var adder int
	if strings.ToLower(common) == common {
		adder = 1
	} else {
		adder = 27
	}
	return idx + adder
}

func find_badges(char_slice []string) string {
	for _, c := range char_slice[0] {
		if strings.Index(char_slice[1], string(c)) == -1 {
            continue
		} else if strings.Index(char_slice[2], string(c)) == -1 {
            continue
		} else {
			return string(c)
		}
	}
	return "Fail"
}

func main() {
	part1()
	part2()
}
