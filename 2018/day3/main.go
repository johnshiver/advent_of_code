package main

import (
	"fmt"
	"log"
	"strconv"
	"strings"

	"github.com/johnshiver/advent_of_code/2018/utils"
)

func createBoard(width, height int) [][]int {
	board := [][]int{}
	for i := 0; i < height; i++ {
		board = append(board, make([]int, width))
	}
	return board
}

type square struct {
	id     int
	x      int
	y      int
	width  int
	height int
}

func createSquare(inputLine string) (square, error) {
	// raw form [#1 @ 108,350: 22x29]

	// get id
	splits := strings.Split(inputLine, " ")
	idRaw := splits[0][1:]
	id, err := strconv.Atoi(idRaw)
	if err != nil {
		return square{}, err
	}

	// get coordinates
	coordinates := splits[2]
	coordinateSplits := strings.Split(coordinates, ",")
	xRaw := coordinateSplits[0]
	yRaw := coordinateSplits[1][:len(coordinateSplits[1])-1]
	x, err := strconv.Atoi(xRaw)
	if err != nil {
		return square{}, err
	}
	y, err := strconv.Atoi(yRaw)
	if err != nil {
		return square{}, err
	}

	// get dimensions
	dimensions := splits[3]
	dimensionSplits := strings.Split(dimensions, "x")
	widthRaw := dimensionSplits[0]
	width, err := strconv.Atoi(widthRaw)
	if err != nil {
		return square{}, err
	}
	heightRaw := dimensionSplits[1]
	height, err := strconv.Atoi(heightRaw)
	if err != nil {
		return square{}, err
	}
	return square{id: id, x: x, y: y, width: width, height: height}, nil
}

func putSquareOnBoard(board [][]int, s square) [][]int {
	// [row][col]
	// 3x3 == [3][3]
	fmt.Println(s)
	for row := s.y; row < s.y+s.height; row++ {
		for col := s.x; col < s.x+s.width; col++ {
			if board[row][col] == 0 {
				board[row][col] = s.id
			} else if board[row][col] > 0 {
				board[row][col] = -1
			}
		}
	}
	return board
}

func countOverlaps(board [][]int) int {
	var total int
	for row := 0; row < len(board[0]); row++ {
		for col := 0; col < len(board); col++ {
			if board[row][col] == -1 {
				total++
			}
		}
	}
	return total
}

func checkSquareOnBoard(board [][]int, s square) bool {
	for row := s.y; row < s.y+s.height; row++ {
		for col := s.x; col < s.x+s.width; col++ {
			if board[row][col] != s.id {
				return false
			}
		}
	}
	return true
}

func main() {
	const width = 1000
	const height = 1000
	board := createBoard(width, height)
	squares, err := utils.ReadFileofStrings("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	allSquares := []square{}
	for _, s := range squares {
		newSquare, err := createSquare(s)
		allSquares = append(allSquares, newSquare)
		if err != nil {
			log.Fatal(err)
		}
		board = putSquareOnBoard(board, newSquare)
	}
	fmt.Println(countOverlaps(board))
	for _, s := range allSquares {
		match := checkSquareOnBoard(board, s)
		if match {
			fmt.Println(s.id)
			return
		}
	}
}
