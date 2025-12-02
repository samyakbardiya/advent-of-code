package main

import (
	"fmt"
	"log"
	"strconv"

	"github.com/echojc/aocutil"
)

func b() {
	input, err := aocutil.NewInputFromFile("session_id")
	if err != nil {
		log.Fatal(err)
	}

	data, err := input.Strings(2025, 1)
	if err != nil {
		log.Fatal(err)
	}

	// data = []string{
	// 	"L68",
	// 	"L30",
	// 	"R48",
	// 	"L5",
	// 	"R60",
	// 	"L55",
	// 	"L1",
	// 	"L99",
	// 	"R14",
	// 	"L82",
	// }

	zeroes := 0
	clicks := 0
	dial := 99950

	for _, ins := range data {
		n, err := strconv.Atoi(ins[1:])
		if err != nil {
			log.Fatal(err)
		}

		var next int
		if ins[0] == 'L' {
			next = dial - n
		} else {
			next = dial + n
		}

		delta := (next / 100) - (dial / 100)
		if delta < 0 {
			delta = -delta
		}
		log.Printf("%v = %v - %v", delta, (next / 100), (dial / 100))
		clicks += delta

		dial = next
		if dial%100 == 0 {
			zeroes++
		}
	}

	fmt.Println(zeroes, clicks)
}
