package main

import (
	"fmt"
)

const DAY1_INPUT = "/home/jshiver/learning_is_good/advent_of_code/2019/inputs/day1.txt"

func day1() {
	fmt.Printf("day1 pt1 output is: %d\n", _day1pt1())
	fmt.Printf("day1 pt2 output is: %d", _day1pt2())
}

func _day1pt1() int {
	ints, err := ReadFileOfInts(DAY1_INPUT)
	if err != nil {
		panic(err)
	}
	final := 0
	for _, i := range ints {
		final += calculateReqMass(i)
	}
	return final
}

func calculateReqMass(mass int) int {
	return (mass / 3) - 2
}

func _day1pt2() int {
	ints, err := ReadFileOfInts(DAY1_INPUT)
	if err != nil {
		panic(err)
	}
	final := 0
	for _, i := range ints {
		final += calcReqMassAndFuel(i)
	}
	return final
}

func calcReqMassAndFuel(mass int) int {
	final := 0
	rMass := calculateReqMass(mass)
	for rMass > 0 {
		final += rMass
		rMass = calculateReqMass(rMass)
	}
	return final
}
