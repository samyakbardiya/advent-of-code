package main

import (
	"os"

	"github.com/charmbracelet/log"
	"github.com/echojc/aocutil"
	"github.com/samyakbardiya/advent-of-code/2025/util"
)

func partOne(data []string) int {
	log.SetLevel(log.InfoLevel)

	totalJoltage := 0
	log.Debug("totalJoltage:", totalJoltage)

	for _, bank := range data {
		largestJoltage := -1
		log.Debug(bank)

		for i := 0; i < len(bank)-1; i++ {
			ith := string(bank[i])

			for j := i + 1; j < len(bank); j++ {
				jth := string(bank[j])

				currJoltage := util.Atoi(ith + jth)
				if currJoltage > largestJoltage {
					largestJoltage = currJoltage
				}
			}
		}

		totalJoltage += largestJoltage
	}

	return totalJoltage
}

func partTwo(data []string) int {
	log.SetLevel(log.InfoLevel)

	totalJoltage := 0

	for _, bank := range data {
		joltage := ""
		startIdx := 0
		needed := 12

		for i := range needed {
			maxIdx := startIdx
			remaining := needed - i - 1
			maxSearchIdx := len(bank) - remaining

			for j := startIdx; j < maxSearchIdx; j++ {
				if bank[j] > bank[maxIdx] {
					maxIdx = j
				}
			}

			joltage += string(bank[maxIdx])
			startIdx = maxIdx + 1
		}
		log.Debug("", "joltage", joltage)

		totalJoltage += util.Atoi(joltage)
	}

	return totalJoltage
}

func main() {
	input, err := aocutil.NewInputFromFile("session_id")
	if err != nil {
		log.Fatal(err)
	}

	data, err := input.Strings(2025, 3)
	if err != nil {
		log.Fatal(err)
	}

	if len(os.Args) > 1 && os.Args[1] == "test" {
		data = []string{
			"987654321111111",
			"811111111111119",
			"234234234234278",
			"818181911112111",
		}
	}

	log.Info("Day 03", "Part One", partOne(data))
	log.Info("Day 03", "Part Two", partTwo(data))
}
