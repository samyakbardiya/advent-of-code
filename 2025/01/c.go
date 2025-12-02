package main

import (
	"fmt"
	"log"
	"strconv"

	"github.com/echojc/aocutil"
)

func c() {
	input, err := aocutil.NewInputFromFile("session_id")
	if err != nil {
		log.Fatal(err)
	}

	data, err := input.Strings(2025, 1)
	if err != nil {
		log.Fatal(err)
	}

	data = []string{
		"L68",
		"L30",
		"R48",
		"L5",
		"R60",
		"L55",
		"L1",
		"L99",
		"R14",
		"L82",
	}

	dial := 50
	zeroes := 0
	clicks := 0

	for _, ins := range data {
		turn, err := strconv.Atoi(ins[1:])
		if err != nil {
			log.Fatal(err)
		}

		div := turn / 100
		clicks += div

		switch ins[0] {
		case 'L':
			delta := dial - turn
			if dial != 0 && delta <= 0 {
				clicks++
			}
			dial = delta % 100
		case 'R':
			delta := dial + turn
			if delta >= 100 {
				clicks++
			}
			dial = delta % 100
		}

		if dial == 0 {
			zeroes++
			clicks++
		}
	}

	fmt.Println(zeroes, clicks)
}
