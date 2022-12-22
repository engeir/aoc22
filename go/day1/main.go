package main

import (
	"fmt"
	"sort"
	"strconv"

	"github.com/engeir/aoc22/go/util"
)

func part1() {
	lines := util.ReadInput("1")
	sorted := count_segments(lines)
	highest := find_highest_individual(sorted)
	fmt.Println(highest) // 71124
}

func part2() {
	lines := util.ReadInput("1")
	sorted := count_segments(lines)
	combined := find_sum_of_top_three(sorted)
	fmt.Println(combined) // 204639
}

func count_segments(all_calories []string) []int {
	var individual_cals []int
	sum_cal := 0
	for _, line := range all_calories {
		if line == "" {
			individual_cals = append(individual_cals, sum_cal)
			sum_cal = 0
		} else {
			add, err := strconv.Atoi(line)
			if err != nil {
				panic(err)
			}
			sum_cal += add
		}
	}
	individual_cals = append(individual_cals, sum_cal)
	sort.Ints(individual_cals)
	return individual_cals
}

func find_highest_individual(sorted_list []int) int {
	return sorted_list[len(sorted_list)-1]
}

func find_sum_of_top_three(sorted_list []int) int {
	sum := 0
	length := len(sorted_list)
	for _, v := range sorted_list[length-3:] {
		sum += v
	}
	return sum
}

func main() {
	part1()
	part2()
}
