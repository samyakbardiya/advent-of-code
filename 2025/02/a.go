package main

import (
	"fmt"
	"io"
	"log"
	"math"
	"strconv"
	"strings"

	"github.com/echojc/aocutil"
	"github.com/samyakbardiya/advent-of-code/2025/util"
)

func countDigits(a int) int {
	if a == 0 {
		return 1
	}
	return int(math.Log10(math.Abs(float64(a)))) + 1
}

func splitByLength(s string, length int) []string {
	var result []string
	for i := 0; i < len(s); i += length {
		end := i + length
		if end > len(s) {
			end = len(s)
		}
		result = append(result, s[i:end])
	}
	return result
}

func partOne(ids []string) int {
	invalidIds := 0

	for _, idRange := range ids {
		idRange = strings.TrimSpace(idRange)
		idRangeParts := strings.Split(idRange, "-")

		start := util.Atoi(idRangeParts[0])
		end := util.Atoi(idRangeParts[1])

		for i := start; i <= end; i++ {
			s := strconv.Itoa(i)
			length := countDigits(i)
			mid := length / 2

			subStart := s[:mid]
			subEnd := s[mid:]
			if subStart == subEnd {
				invalidIds += i
			}
		}
	}

	return invalidIds
}

func partTwo(ids []string) int {
	invalidIds := 0

	for _, idRange := range ids {
		idRange = strings.TrimSpace(idRange)
		idRangeParts := strings.Split(idRange, "-")

		startIDRange := util.Atoi(idRangeParts[0])
		endIDRange := util.Atoi(idRangeParts[1])
		log.Printf("%v to %v:\n", startIDRange, endIDRange)

		for id := startIDRange; id <= endIDRange; id++ {
			log.Printf("\t%v: ", id)

			idStr := strconv.Itoa(id)
			length := countDigits(id)
			midLength := length / 2

			isInvalid := false
			for subStrLen := 1; subStrLen <= midLength; subStrLen++ {
				chunks := splitByLength(idStr, subStrLen)
				areAllChunksSame := true
				for i := 1; i < len(chunks); i++ {
					if chunks[i-1] != chunks[i] {
						areAllChunksSame = false
						log.Printf("%v, ", chunks)
						break
					}
				}
				if areAllChunksSame {
					isInvalid = true
					break
				}
			}
			log.Println()

			if isInvalid {
				log.Printf("=== %v ===\n", id)
				invalidIds += id
			}
		}

		log.Println()
	}

	return invalidIds
}

func a() {
	log.SetOutput(io.Discard)

	input, err := aocutil.NewInputFromFile("session_id")
	if err != nil {
		log.Fatal(err)
	}

	data, err := input.Strings(2025, 2)
	if err != nil {
		log.Fatal(err)
	}

	ids := strings.Split(data[0], ",")

	// ids = []string{
	// 	"11-22",
	// 	"95-115",
	// 	"998-1012",
	// 	"1188511880-1188511890",
	// 	"222220-222224",
	// 	"1698522-1698528",
	// 	"446443-446449",
	// 	"38593856-38593862",
	// 	"565653-565659",
	// 	"824824821-824824827",
	// 	"2121212118-2121212124",
	// }

	fmt.Printf("Part One: %v\n", partOne(ids))
	fmt.Printf("Part Two: %v\n", partTwo(ids))
}
