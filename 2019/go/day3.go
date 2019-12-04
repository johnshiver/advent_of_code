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
	IX         = 99999
	CP         = 100000
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
}

func day3pt1() int {
	wires, err := ReadFileOfStrings(DAY3_INPUT)
	if err != nil {
		panic(err)
	}
	return findCrossedWires(wires)
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
	return Abs(i1.x-i2.x) + Abs(i1.y-i2.y)

}

func moveWireOnGrid(grid [][]int, wireMoves []gridMove, centralPort intersection, wireNum int) ([][]int, []intersection) {

	curX := centralPort.x
	curY := centralPort.y
	var visited []intersection

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
			}
			curY -= m.distance
		}

	}

	return grid, visited
}
