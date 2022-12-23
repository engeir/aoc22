package main

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/engeir/aoc22/go/util"
)

func two_regions_to_one(regions string) []string {
	splits := strings.Split(regions, ",")
	r1 := splits[0]
	r2 := splits[1]
	b1 := strings.Split(r1, "-")[0]
	t1 := strings.Split(r1, "-")[1]
	b1i, _ := strconv.Atoi(b1)
	t1i, _ := strconv.Atoi(t1)
	b2 := strings.Split(r2, "-")[0]
	t2 := strings.Split(r2, "-")[1]
	b2i, _ := strconv.Atoi(b2)
	t2i, _ := strconv.Atoi(t2)
	var b3 string
	var t3 string
	if b1i < b2i {
		b3 = b1
	} else {
		b3 = b2
	}
	if t1i > t2i {
		t3 = t1
	} else {
		t3 = t2
	}
	return []string{r1, r2, b3 + "-" + t3}
}

func full_overlap(regions []string) bool {
	if regions[0] == regions[2] || regions[1] == regions[2] {
		return true
	}
	return false
}

func partial_overlap(regions []string) bool {
	b1 := strings.Split(regions[0], "-")[0]
	t1 := strings.Split(regions[0], "-")[1]
	b1i, _ := strconv.Atoi(b1)
	t1i, _ := strconv.Atoi(t1)
	b2 := strings.Split(regions[1], "-")[0]
	t2 := strings.Split(regions[1], "-")[1]
	b2i, _ := strconv.Atoi(b2)
	t2i, _ := strconv.Atoi(t2)
	b3 := strings.Split(regions[2], "-")[0]
	t3 := strings.Split(regions[2], "-")[1]
	if (b1 == b3 && t2 == t3 && t1i < b2i) || (b2 == b3 && t1 == t3 && t2i < b1i) {
		return false
	}
	return true
}

func part1() {
	lines := util.ReadInput("4")
	sum := 0
	for _, line := range lines {
		if len(line) > 0 {
			region_slice := two_regions_to_one(line)
			out := full_overlap(region_slice)
			if out {
				sum++
			}
		}
	}
	fmt.Println(sum) // 450
}

func part2() {
	lines := util.ReadInput("4")
	sum := 0
	for _, line := range lines {
		if len(line) > 0 {
			region_slice := two_regions_to_one(line)
			out := partial_overlap(region_slice)
			if out {
				sum++
			}
		}
	}
	fmt.Println(sum) // 837
}

func main() {
	part1()
	part2()
}
