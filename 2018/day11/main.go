package main

import "fmt"

func createGrid() [][]int {
	grid := [][]int{}
	for i := 0; i < 300; i++ {
		grid = append(grid, make([]int, 300))
	}
	return grid
}

func calculatePower(x, y, serialNumber int) int {
	// find fuel cell's rack id: x coordinate + 10
	rackID := x + 10
	// begin with power level of rack ID * y coordinate
	powerLevel := rackID * y
	// increase power level by value of grid serial number (puzzle input)
	powerLevel += serialNumber
	// set power level to itself multipled by rack id
	powerLevel *= rackID
	// keep only the hundreds digit of the power level: 12345 should becoe 3.  numbers below 100 are 0
	if powerLevel < 100 {
		powerLevel = 0
	} else {
		powerLevel = (powerLevel % 1000) / 100
	}
	// subtract 5
	return powerLevel - 5

}

func calcPowerLevelStartingAtPosition(x, y int, grid [][]int) int {
	power := 0
	for i := x; i < len(grid[0]) && i < x+3; i++ {
		for j := y; j < len(grid) && j < y+3; j++ {
			power += grid[j][i]
		}
	}
	return power
}

func fillInPowerLevels(serialNumber int, grid [][]int) {
	for y := 0; y < len(grid); y++ {
		for x := 0; x < len(grid[0]); x++ {
			grid[y][x] = calculatePower(x+1, y+1, serialNumber)
		}
	}
}

func part1() {
	serialNumber := 2866
	grid := createGrid()
	fillInPowerLevels(serialNumber, grid)
	powerLevels := createGrid()
	for y := 0; y < len(grid); y++ {
		for x := 0; x < len(grid[0]); x++ {
			powerLevels[y][x] = calcPowerLevelStartingAtPosition(x, y, grid)
		}
	}

	largestPower := -10000
	var finalX, finalY int
	for y := 0; y < len(grid); y++ {
		for x := 0; x < len(grid[0]); x++ {
			power := powerLevels[y][x]
			if power > largestPower {
				largestPower = power
				finalX = x + 1
				finalY = y + 1
			}
		}
	}
	fmt.Println(finalX, finalY)
}

func main() {
	part1()
}
