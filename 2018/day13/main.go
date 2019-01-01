package main

import (
	"fmt"
	"log"
	"sort"

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

func (tc *trackCar) makeMove(grid []string) {
	switch tc.direction {
	case ">":
		tc.x++
	case "<":
		tc.x--
	case "^":
		tc.y--
	case "v":
		tc.y++
	}
	// if currBlock is a turn, change direction
	// if it is an intersection, change direction according to nextTurn
	/*

				/---\
				|   |  /----\
				| /-+--+-\  |
				| | |  X |  |
				\-+-/  \-+--/
		  	      \------/

	*/
	currBlock := string(grid[tc.y][tc.x])
	switch currBlock {
	case "\\":
		switch tc.direction {
		case ">":
			tc.direction = "v"
		case "<":
			tc.direction = "^"
		case "^":
			tc.direction = "<"
		case "v":
			tc.direction = ">"
		}
	case "/":
		switch tc.direction {
		case ">":
			tc.direction = "^"
		case "<":
			tc.direction = "v"
		case "^":
			tc.direction = ">"
		case "v":
			tc.direction = "<"
		}
	case "+":
		newDirection, err := tc.makeTurn()
		if err != nil {
			log.Fatal(err)
		}
		switch newDirection {
		case "left":
			switch tc.direction {
			case ">":
				tc.direction = "^"
			case "<":
				tc.direction = "v"
			case "^":
				tc.direction = "<"
			case "v":
				tc.direction = ">"
			}
		case "right":
		case ">":
			tc.direction = "v"
		case "<":
			tc.direction = "^"
		case "^":
			tc.direction = ">"
		case "v":
			tc.direction = "<"
		case "straight":
		}
	default:
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

func sortTrackCars(trackCars []*trackCar) {
	// TODO: sort by x too
	sort.Slice(trackCars, func(i, j int) bool {
		if trackCars[i].y < trackCars[j].y {
			return true
		}
		if trackCars[i].y > trackCars[j].y {
			return false
		}
		return trackCars[i].x < trackCars[j].x
	})
}

func part1() {
	// read input into memory
	grid, err := utils.ReadFileofStrings("test_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	for _, l := range grid {
		fmt.Println(l)
	}

	// find track cars
	trackCars := createTrackCarsFromGrid(grid)
	sortTrackCars(trackCars)
	for _, tc := range trackCars {
		fmt.Println(tc)
	}

	crashDetected := false
	var crashX, crashY int
	for !crashDetected {
		for _, car := range trackCars {
			car.makeMove(grid)
		}
		// need to resort each time
		sortTrackCars(trackCars)
		// cars should be next to each other if there is a crash
		prevCar := trackCars[0]
		fmt.Printf("Checking car: \n\tx: %d y: %d\n", prevCar.x, prevCar.y)
		for i := 1; i < len(trackCars); i++ {
			curr := trackCars[i]
			fmt.Printf("Checking car: \n\tx: %d y: %d\n", curr.x, curr.y)
			if curr.x == prevCar.x && curr.y == prevCar.y {
				crashDetected = true
				crashX = curr.x
				crashY = curr.y
				break
			}
			prevCar = curr
		}
	}
	fmt.Printf("x: %d y: %d\n", crashX, crashY)
}

func main() {
	part1()
}
