package main

import (
	"fmt"
	"log"
	"sort"
	"strings"

	"github.com/johnshiver/advent_of_code/2018/utils"
)

type trackCar struct {
	x         int
	y         int
	direction string
	nextTurn  int
	active    bool
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

func (tc *trackCar) makeMove(grid [][]string) {
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
			switch tc.direction {
			case ">":
				tc.direction = "v"
			case "<":
				tc.direction = "^"
			case "^":
				tc.direction = ">"
			case "v":
				tc.direction = "<"
			}
		case "straight":
		}
	default:
	}
}

func createTrackCarsFromGrid(grid [][]string) []*trackCar {
	trackCars := []*trackCar{}
	for y := 0; y < len(grid); y++ {
		for x := 0; x < len(grid[y]); x++ {
			curBlock := string(grid[y][x])
			if curBlock == ">" || curBlock == "<" || curBlock == "^" || curBlock == "v" {
				trackCars = append(trackCars, &trackCar{x: x, y: y, direction: curBlock, active: true})
				grid[y][x] = "-"
			}
		}
	}
	return trackCars
}

func sortTrackCars(trackCars []*trackCar) {
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

func printGridWithCars(gridCopy, grid [][]string, trackCars []*trackCar) {
	for _, tc := range trackCars {
		gridCopy[tc.y][tc.x] = tc.direction
	}
	for y := 0; y < len(gridCopy); y++ {
		fmt.Println(strings.Join(gridCopy[y], ""))
	}
	for _, tc := range trackCars {
		gridCopy[tc.y][tc.x] = grid[tc.y][tc.x]
	}

}

type location struct {
	x int
	y int
}

func part1() {
	// read input into memory
	gridLines, err := utils.ReadFileofStrings("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	grid := [][]string{}
	gridCopy := [][]string{}

	for _, l := range gridLines {
		line := strings.Split(l, "")
		grid = append(grid, line)
		line2 := strings.Split(l, "")
		gridCopy = append(gridCopy, line2)
	}

	// find track cars
	trackCars := createTrackCarsFromGrid(grid)
	sortTrackCars(trackCars)

	crashDetected := false
	var crashX, crashY int
	ticks := 0
	locations := make(map[location]bool)
	for !crashDetected {
		// printGridWithCars(gridCopy, grid, trackCars)
		for _, car := range trackCars {
			// need to check if cars collide after each crash
			prevCarLoc := location{x: car.x, y: car.y}
			locations[prevCarLoc] = false
			car.makeMove(grid)
			carLoc := location{x: car.x, y: car.y}
			if collided := locations[carLoc]; collided == true {
				crashDetected = true
				fmt.Println(carLoc)
				fmt.Println(ticks)
				return
			}
			locations[carLoc] = true
		}
		ticks++
		// need to resort each time
		sortTrackCars(trackCars)
		// fmt.Println(strings.Repeat("-", 45))
		// for _, tc := range trackCars {
		// 	fmt.Println(tc)
		// }
	}
	fmt.Printf("x: %d y: %d\n", crashX, crashY)
}

func part2() {
	// read input into memory
	gridLines, err := utils.ReadFileofStrings("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	grid := [][]string{}
	gridCopy := [][]string{}
	for _, l := range gridLines {
		line := strings.Split(l, "")
		grid = append(grid, line)
		line2 := strings.Split(l, "")
		gridCopy = append(gridCopy, line2)
	}

	// find track cars
	trackCars := createTrackCarsFromGrid(grid)
	fmt.Println(len(trackCars))
	sortTrackCars(trackCars)

	ticks := 0
	locations := make(map[location]bool)
	activeCars := len(trackCars)
	for activeCars > 1 {
		// printGridWithCars(gridCopy, grid, trackCars)
		for _, car := range trackCars {
			if car.active == false {
				continue
			}
			// need to check if cars collide after each crash
			prevCarLoc := location{x: car.x, y: car.y}
			delete(locations, prevCarLoc)
			car.makeMove(grid)
			carLoc := location{x: car.x, y: car.y}
			if collided := locations[carLoc]; collided == true {
				for _, tc := range trackCars {
					if tc.x == carLoc.x && tc.y == carLoc.y {
						tc.active = false
						continue
					}
				}
				curActiveCars := 0
				for _, tc := range trackCars {
					if tc.active == true {
						curActiveCars++
					}
				}
				activeCars = curActiveCars
				delete(locations, carLoc)
			} else {
				locations[carLoc] = true
			}
		}
		ticks++
		sortTrackCars(trackCars)
	}
	for _, tc := range trackCars {
		if tc.active == true {
			fmt.Printf("x: %d y: %d\n", tc.x, tc.y)
		}
	}

}

func main() {
	// part1()
	part2()
}
