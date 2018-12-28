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

func calcPowerLevelStartingAtPosition(x, y, degree int, grid [][]int) int {
	power := 0
	for i := x; i < len(grid[0]) && i < x+degree; i++ {
		for j := y; j < len(grid) && j < y+degree; j++ {
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
			powerLevels[y][x] = calcPowerLevelStartingAtPosition(x, y, 3, grid)
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

type Result struct {
	x      int
	y      int
	power  int
	degree int
}

type Work struct {
	x      int
	y      int
	degree int
}

func part2() {
	const WORKER_COUNT = 8
	resultChan := make(chan *Result, 1000)
	workChan := make(chan *Work, 10000)
	serialNumber := 2866
	grid := createGrid()
	fillInPowerLevels(serialNumber, grid)

	for i := 0; i < WORKER_COUNT; i++ {
		go func() {
			for work := range workChan {
				power := calcPowerLevelStartingAtPosition(work.x, work.y, work.degree, grid)
				resultChan <- &Result{x: work.x, y: work.y, power: power, degree: work.degree}
			}
		}()
	}

	go func() {
		for y := 0; y < len(grid); y++ {
			for x := 0; x < len(grid[0]); x++ {
				for d := 0; d < 300; d++ {
					workChan <- &Work{y: y, x: x, degree: d}
				}
			}
		}
		close(workChan)
	}()

	largestResult := &Result{}
	resultsSeen := 0
	for i := 0; i < 27000000; i++ {
		r := <-resultChan
		resultsSeen++
		if r.power > largestResult.power {
			largestResult = r
		}
		if resultsSeen%100000 == 0 {
			fmt.Printf("Have seen %d results\n", resultsSeen)
			fmt.Printf("Largest sofar: %v", largestResult)
			fmt.Println()
		}
	}
	fmt.Printf("\nLargest found: \n\tX: %d Y: %d Degree %d Power %d\n", largestResult.x+1, largestResult.y+1, largestResult.degree, largestResult.power)
}

func main() {
	part1()
	part2()
}
