package main

import (
	"bufio"
	"os"
	"strconv"
)

func ReadFileOfInts(fileName string) ([]int, error) {

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
