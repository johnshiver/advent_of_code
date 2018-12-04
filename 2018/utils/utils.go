package utils

import (
	"bufio"
	"os"
	"strconv"
)

// ReadFileofInts ...
//
func ReadFileofInts(fileName string) ([]int, error) {

	file, err := os.Open("input.txt")
	if err != nil {
		return nil, err
	}
	defer file.Close()

	allVals := []int{}
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

// ReadFileofStrings ...
//
func ReadFileofStrings(fileName string) ([]string, error) {

	file, err := os.Open("input.txt")
	if err != nil {
		return nil, err
	}
	defer file.Close()

	allVals := []string{}
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
