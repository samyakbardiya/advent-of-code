package main

import (
	"fmt"
	"log"
	"strconv"
	"strings"

	"github.com/echojc/aocutil"
)

func d() {
	input, err := aocutil.NewInputFromFile("session_id")
	if err != nil {
		log.Fatal(err)
	}

	data, err := input.Strings(2025, 1)
	if err != nil {
		log.Fatal(err)
	}

	// data = []string{
	// 	"R0",
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

	dial := 50
	ansA := 0
	ansB := 0

	for _, ins := range data {
		ins = strings.TrimSpace(ins)

		dir := ins[0]
		turn, err := strconv.Atoi(ins[1:])
		if err != nil {
			log.Fatal(err)
		}

		var newDial int
		switch dir {
		case 'L':
			newDial = dial - turn
			if newDial < 0 {
				ansB += -newDial / 100
				if dial > 0 {
					ansB += 1
				}
			} else if newDial == 0 {
				ansB += 1
			}
		case 'R':
			newDial = dial + turn
			ansB += newDial / 100
		}

		dial = ((newDial % 100) + 100) % 100
		if dial == 0 {
			ansA++
		}

		symbol := ""
		switch dir {
		case 'L':
			symbol = "L -"
		case 'R':
			symbol = "R +"
		}
		fmt.Printf("%v %3v => %3v | %4v    || %4v, %4v\n", symbol, turn, dial, newDial, ansA, ansB)
	}

	log.Println(ansA, ansB)
}
