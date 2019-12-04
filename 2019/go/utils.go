package main

import (
	"bufio"
	"os"
	"strconv"
)

func readFileOfInts(fileName string) ([]int, error) {
	file, err := os.Open(fileName)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var allVals []int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		newVal := scanner.Text()
		newInt, err := strconv.Atoi(newVal)
		if err != nil {
			return nil, err
		}
		allVals = append(allVals, newInt)
	}
	if err := scanner.Err(); err != nil {
		return nil, err
	}
	return allVals, nil
}

func readFileOfStrings(fileName string) ([]string, error) {
	file, err := os.Open(fileName)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var allVals []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		newVal := scanner.Text()
		allVals = append(allVals, newVal)
	}
	if err := scanner.Err(); err != nil {
		return nil, err
	}
	return allVals, nil
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
