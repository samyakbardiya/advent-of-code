package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func a() {
	file, err := os.Open("input")
	if err != nil {
		log.Fatalln(err)
	}
	defer file.Close()

	dial := 50
	password := 0

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		rotate := strings.TrimSpace(line)

		direction := rotate[0]
		count, err := strconv.Atoi(rotate[1:])
		if err != nil {
			log.Fatalln(err)
		}
		var symbol string

		switch direction {
		case 'L':
			symbol = "-"
			dial = dial - count
		case 'R':
			symbol = "+"
			dial = dial + count
		default:
			log.Fatalf("OPS read something weird: %v", rotate[0])
		}

		if dial < 0 {
			fmt.Printf("Crossed @ '%v %3v' => %v\n", symbol, count, dial)
			dial = 100 + (dial % 100)
		} else if dial > 99 {
			dial = (dial % 100)
		}

		fmt.Printf("After '%v %3v' => %3v\n", symbol, count, dial)

		if dial == 0 {
			password += 1
		}
	}

	fmt.Printf("Ans: %v\n", password)

	if err := scanner.Err(); err != nil {
		fmt.Println("Error:", err)
	}
}
