package main

import (
	"fmt"
	"strconv"
	"strings"
)

const (
	DAY3_INPUT = "/home/jshiver/learning_is_good/advent_of_code/2019/inputs/day3.txt"
	GRID_W     = 40000
	GRID_H     = 40000
	//GRID_W = 4000
	//GRID_H = 4000
	IX = 99999
	CP = 100000
)

type direction int

const (
	Right direction = iota + 1
	Left
	Down
	Up
)

type intersection struct {
	x int
	y int
}

type gridMove struct {
	dir      direction
	distance int
}

func day3() {
	fmt.Printf("day3 pt1: %d\n", day3pt1())
	fmt.Printf("day3 pt2: %d\n", day3pt2())
}

func day3pt1() int {
	wires, err := readFileOfStrings(DAY3_INPUT)
	if err != nil {
		panic(err)
	}
	return findCrossedWires(wires)
}

func day3pt2() int {
	wires, err := readFileOfStrings(DAY3_INPUT)
	if err != nil {
		panic(err)
	}
	return findMinSignalDelay(wires)
}

func xFormRaw(rawMove string) gridMove {
	var move gridMove
	switch rawMove[0] {
	case 'R':
		rawDistance := strings.TrimPrefix(rawMove, "R")
		d, err := strconv.Atoi(rawDistance)
		if err != nil {
			panic(err)
		}
		move = gridMove{
			dir:      Right,
			distance: d,
		}
	case 'L':
		rawDistance := strings.TrimPrefix(rawMove, "L")
		d, err := strconv.Atoi(rawDistance)
		if err != nil {
			panic(err)
		}
		move = gridMove{
			dir:      Left,
			distance: d,
		}
	case 'U':
		rawDistance := strings.TrimPrefix(rawMove, "U")
		d, err := strconv.Atoi(rawDistance)
		if err != nil {
			panic(err)
		}
		move = gridMove{
			dir:      Up,
			distance: d,
		}
	case 'D':
		rawDistance := strings.TrimPrefix(rawMove, "D")
		d, err := strconv.Atoi(rawDistance)
		if err != nil {
			panic(err)
		}
		move = gridMove{
			dir:      Down,
			distance: d,
		}
	}
	return move
}

func findCrossedWires(wires []string) int {
	var wireGrid [][]int
	for y := 0; y < GRID_H; y++ {
		wireGrid = append(wireGrid, make([]int, GRID_W))
	}

	centralPort := intersection{
		x: GRID_W / 2,
		y: GRID_H / 2,
	}
	wireGrid[centralPort.y][centralPort.x] = CP

	var visited []intersection
	var v []intersection
	for i, w := range wires {
		rawWireMoves := strings.Split(w, ",")
		var wireMoves []gridMove
		for _, m := range rawWireMoves {
			wireMoves = append(wireMoves, xFormRaw(m))
		}
		wireGrid, v = moveWireOnGrid(wireGrid, wireMoves, centralPort, i+1)
		visited = append(visited, v...)
	}

	var intersections []intersection
	for _, c := range visited {
		if wireGrid[c.y][c.x] == IX {
			intersections = append(intersections, c)
		}
	}

	var minDistance int
	for _, i := range intersections {
		iDistance := findManDistance(centralPort, i)
		if minDistance == 0 || iDistance < minDistance {
			minDistance = iDistance
		}
	}
	return minDistance

}

func findManDistance(i1, i2 intersection) int {
	return abs(i1.x-i2.x) + abs(i1.y-i2.y)

}

func moveWireOnGrid(grid [][]int, wireMoves []gridMove, centralPort intersection, wireNum int) ([][]int, []intersection) {

	curX := centralPort.x
	curY := centralPort.y
	var visited []intersection
	totalSteps := 0

	for _, m := range wireMoves {

		switch m.dir {
		case Right:
			for x := curX; x < curX+m.distance; x++ {
				if grid[curY][x] != 0 && grid[curY][x] != wireNum {
					grid[curY][x] = IX
				} else {
					grid[curY][x] = wireNum
				}
				visited = append(visited, intersection{x, curY})
				totalSteps++
			}
			curX += m.distance
		case Left:
			for x := curX; x > curX-m.distance; x-- {
				if grid[curY][x] != 0 && grid[curY][x] != wireNum {
					grid[curY][x] = IX
				} else {
					grid[curY][x] = wireNum
				}
				visited = append(visited, intersection{x, curY})
				totalSteps++
			}
			curX -= m.distance
		case Up:
			for y := curY; y < curY+m.distance; y++ {
				if grid[y][curX] != 0 && grid[y][curX] != wireNum {
					grid[y][curX] = IX
				} else {
					grid[y][curX] = wireNum
				}
				visited = append(visited, intersection{curX, y})
				totalSteps++
			}
			curY += m.distance
		case Down:
			for y := curY; y > curY-m.distance; y-- {
				if grid[y][curX] != 0 && grid[y][curX] != wireNum {
					grid[y][curX] = IX
				} else {
					grid[y][curX] = wireNum
				}
				visited = append(visited, intersection{curX, y})
				totalSteps++
			}
			curY -= m.distance
		}

	}

	return grid, visited
}

func findMinSignalDelay(wires []string) int {
	var wireGrid [][]int
	for y := 0; y < GRID_H; y++ {
		wireGrid = append(wireGrid, make([]int, GRID_W))
	}

	centralPort := intersection{
		x: GRID_W / 2,
		y: GRID_H / 2,
	}
	wireGrid[centralPort.y][centralPort.x] = CP

	visited := make(map[intersection]int)
	for i, w := range wires {
		rawWireMoves := strings.Split(w, ",")
		var wireMoves []gridMove
		for _, m := range rawWireMoves {
			wireMoves = append(wireMoves, xFormRaw(m))
		}
		wireGrid = moveWireOnGrid2(wireGrid, wireMoves, centralPort, i+1, visited)
	}

	for c := range visited {
		if wireGrid[c.y][c.x] != IX {
			delete(visited, c)
		}
	}

	var minDelay int
	for _, steps := range visited {
		if minDelay == 0 || steps < minDelay {
			minDelay = steps
		}
	}
	return minDelay

}

func moveWireOnGrid2(grid [][]int, wireMoves []gridMove, centralPort intersection, wireNum int, visited map[intersection]int) [][]int {

	curX := centralPort.x
	curY := centralPort.y
	var totalSteps int

	for _, m := range wireMoves {

		switch m.dir {
		case Right:
			for x := curX; x < curX+m.distance; x++ {
				i := intersection{x, curY}
				if grid[curY][x] != 0 && grid[curY][x] != wireNum {
					visited[i] += totalSteps
					grid[curY][x] = IX
				} else if grid[curY][x] == 0 {
					visited[i] = totalSteps
					grid[curY][x] = wireNum
				} else {
					grid[curY][x] = wireNum
				}
				totalSteps++
			}
			curX += m.distance
		case Left:
			for x := curX; x > curX-m.distance; x-- {
				i := intersection{x, curY}
				if grid[curY][x] != 0 && grid[curY][x] != wireNum {
					visited[i] += totalSteps
					grid[curY][x] = IX
				} else if grid[curY][x] == 0 {
					visited[i] = totalSteps
					grid[curY][x] = wireNum
				} else {
					grid[curY][x] = wireNum
				}
				totalSteps++
			}
			curX -= m.distance
		case Up:
			for y := curY; y < curY+m.distance; y++ {
				i := intersection{curX, y}
				if grid[y][curX] != 0 && grid[y][curX] != wireNum {
					visited[i] += totalSteps
					grid[y][curX] = IX
				} else if grid[y][curX] == 0 {
					visited[i] = totalSteps
					grid[y][curX] = wireNum
				} else {
					grid[y][curX] = wireNum
				}
				totalSteps++
			}
			curY += m.distance
		case Down:
			for y := curY; y > curY-m.distance; y-- {
				i := intersection{curX, y}
				if grid[y][curX] != 0 && grid[y][curX] != wireNum {
					visited[i] += totalSteps
					grid[y][curX] = IX
				} else if grid[y][curX] == 0 {
					visited[i] = totalSteps
					grid[y][curX] = wireNum
				} else {
					grid[y][curX] = wireNum
				}

				totalSteps++
			}
			curY -= m.distance
		}

	}

	return grid
}
