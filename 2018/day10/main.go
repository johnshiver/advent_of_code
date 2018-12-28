package main

import (
	"fmt"
	"log"
	"regexp"
	"strconv"
	"strings"

	"github.com/johnshiver/advent_of_code/2018/utils"
)

var minX, minY, maxX, maxY int

type Position struct {
	x int
	y int
}

type Point struct {
	start Position
	end   Position
	xVel  int
	yVel  int
}

func createGrid(points []*Point) [][]string {
	// set min and max x + y
	for _, p := range points {
		if p.start.x < minX {
			minX = p.start.x
		}
		if p.start.x > maxX {
			maxX = p.start.x
		}
		if p.start.y < minY {
			minY = p.start.y
		}
		if p.start.y > maxY {
			maxY = p.start.y
		}
	}

	grid := [][]string{}
	minX = utils.Abs(minX)
	minY = utils.Abs(minY)

	log.Printf("minX %d maxX %d minY %d maxY %d\n", minX, maxX, minY, maxY)

	for i := 0; i < minY+maxY+1; i++ {
		grid = append(grid, make([]string, minX+maxX+1))
	}

	for y := 0; y < len(grid); y++ {
		for x := 0; x < len(grid[0]); x++ {
			grid[y][x] = "."
		}
	}

	return grid
}

// putPointsOnGrid ...
//
// example
// -9
// if len is 18
// then -9 should be in the 0 position
// ==
// what if we have an odd number of columns?
// [-3, -2, -1, 0, 1, 2, 3, 4]
func putPointsOnGrid(points []*Point, grid [][]string) error {
	xPositions := []int{}
	for i := -minX; i <= maxX; i++ {
		xPositions = append(xPositions, i)
	}
	fmt.Printf("xPositions %v\n", xPositions)

	yPositions := []int{}
	for i := -minY; i <= maxY; i++ {
		yPositions = append(yPositions, i)
	}
	fmt.Printf("yPositions %v\n", yPositions)

	for _, p := range points {
		xgridPos := utils.IndexOf(p.start.x, xPositions)
		ygridPos := utils.IndexOf(p.start.y, yPositions)
		if xgridPos == -1 || ygridPos == -1 {
			return fmt.Errorf("position not found in positons: x = %d y = %d maxX xPositions %v yPositions %v", p.start.x, p.start.y, xPositions, yPositions)
		}
		fmt.Printf("p.start.x %d p.start.y %d\n", p.start.x, p.start.y)
		fmt.Printf("xgridPos %d ygridPos %d\n", xgridPos, ygridPos)
		if ygridPos >= len(grid) || xgridPos >= len(grid[0]) {
			return fmt.Errorf("positiion outside of grid ygridPos %d xgridPos %d", ygridPos, xgridPos)
		}
		grid[ygridPos][xgridPos] = "#"
	}

	return nil

}

func test1() {
	points := []*Point{}
	numberRegex := regexp.MustCompile(`[-]?[0-9]+`)
	testInputs, err := utils.ReadFileofStrings("test_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	var x, y, xVel, yVel int
	var sPos Position
	for _, t := range testInputs {
		testNums := numberRegex.FindAllString(t, -1)
		x, err = strconv.Atoi(testNums[0])
		if err != nil {
			log.Fatal(err)
		}
		y, err = strconv.Atoi(testNums[1])
		if err != nil {
			log.Fatal(err)
		}
		sPos = Position{x: x, y: y}
		xVel, err = strconv.Atoi(testNums[2])
		if err != nil {
			log.Fatal(err)
		}
		yVel, err = strconv.Atoi(testNums[3])
		if err != nil {
			log.Fatal(err)
		}
		points = append(points, &Point{start: sPos, xVel: xVel, yVel: yVel})
	}

	grid := createGrid(points)
	for _, line := range grid {
		fmt.Println(strings.Join(line, ""))
	}
	err = putPointsOnGrid(points, grid)
	if err != nil {
		log.Println(err)
	}
	for _, line := range grid {
		fmt.Println(strings.Join(line, ""))
	}

}
func main() {
	test1()
}
