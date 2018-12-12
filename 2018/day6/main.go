package main

import (
	"fmt"
	"log"
	"strconv"
	"strings"

	"github.com/johnshiver/advent_of_code/2018/utils"
)

type coordinate struct {
	x     int
	y     int
	label int
}

func createGrid(coordinates []coordinate) [][]int {
	var maxX, maxY int
	grid := [][]int{}

	for _, c := range coordinates {
		if c.x > maxX {
			maxX = c.x
		}
		if c.y > maxY {
			maxY = c.y
		}
	}

	for i := 0; i < maxY+1; i++ {
		newLine := make([]int, maxX+1)
		grid = append(grid, newLine)
	}

	for _, c := range coordinates {
		grid[c.y][c.x] = c.label

	}

	return grid
}

func printGrid(grid [][]int) {
	for _, l := range grid {
		stringLine := []string{}

		for _, c := range l {
			lC := strconv.Itoa(c)
			stringLine = append(stringLine, lC)
		}
		fmt.Println(strings.Join(stringLine, " "))
	}
}

func calculateManhattanDistances(grid [][]int, coords []coordinate) {

	for y := 0; y < len(grid); y++ {
		for x := 0; x < len(grid[0]); x++ {
			mindistances := make(map[int][]int)
			for _, c := range coords {
				manDistance := utils.Abs(x-c.x) + utils.Abs(y-c.y)
				mindistances[manDistance] = append(mindistances[manDistance], c.label)
			}

			closestDist := 320000
			var closestCoord int
			for mDistance, cs := range mindistances {
				if mDistance < closestDist {
					closestDist = mDistance
					if len(cs) > 1 {
						closestCoord = 0
					} else {
						closestCoord = cs[0]
					}
				}
			}

			if grid[y][x] > 0 {
				// this is a coord tile
				continue
			} else {
				grid[y][x] = closestCoord
			}
		}
	}
}

func isOnEdge(x, y int, grid [][]int) bool {
	if x == 0 || y == 0 || x == len(grid[0])-1 || y == len(grid)-1 {
		return true
	}
	return false
}

func countArea(grid [][]int) int {

	counts := make(map[int]int)
	for y := 0; y < len(grid); y++ {
		for x := 0; x < len(grid[0]); x++ {
			if isOnEdge(x, y, grid) {
				counts[grid[y][x]] -= 10000000000
			}
			counts[grid[y][x]]++
		}
	}

	highestCount := 0

	for label, count := range counts {
		fmt.Println(label, count)
		if count > highestCount {
			highestCount = count
		}
	}

	return highestCount

}

func main() {
	coordinates, err := utils.ReadFileofStrings("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	allCoords := []coordinate{}
	for i, c := range coordinates {
		coords := strings.Split(c, ", ")
		x, err := strconv.Atoi(coords[0])
		if err != nil {
			log.Fatal(err)
		}
		y, err := strconv.Atoi(coords[1])
		if err != nil {
			log.Fatal(err)
		}
		allCoords = append(allCoords, coordinate{x: x, y: y, label: i + 1})
	}
	grid := createGrid(allCoords)
	calculateManhattanDistances(grid, allCoords)
	printGrid(grid)
	fmt.Println(countArea(grid))
}
