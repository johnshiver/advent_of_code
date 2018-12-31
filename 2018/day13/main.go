package main

import (
	"fmt"
	"log"

	"github.com/johnshiver/advent_of_code/2018/utils"
)

type trackCar struct {
	x         int
	y         int
	direction string
	nextTurn  int
}

func (tc *trackCar) makeTurn() (string, error) {
	switch tc.nextTurn {
	case 0:
		tc.nextTurn++
		return "left", nil
	case 1:
		tc.nextTurn++
		return "straight", nil
	case 2:
		tc.nextTurn = 0
		return "right", nil
	default:
		return "", fmt.Errorf("trackCard nextTurn has invalid value %d", tc.nextTurn)
	}
}

func createTrackCarsFromGrid(grid []string) []*trackCar {
	trackCars := []*trackCar{}
	for y, l := range grid {
		for x := 0; x < len(l); x++ {
			curBlock := string(l[x])
			if curBlock == ">" || curBlock == "<" || curBlock == "^" || curBlock == "v" {
				trackCars = append(trackCars, &trackCar{x: x, y: y, direction: curBlock})
			}
		}
	}
	return trackCars
}

func part1() {
	// read input into memory
	gridLines, err := utils.ReadFileofStrings("test_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	for _, l := range gridLines {
		fmt.Println(l)
	}

	// find track cars
	trackCars := createTrackCarsFromGrid(gridLines)
	for _, tc := range trackCars {
		fmt.Println(tc)
	}

}

func main() {
	part1()
}
