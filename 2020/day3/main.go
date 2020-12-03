package main

import (
	"bufio"
	"fmt"
	"os"
)



func readFileofStrings(fileName string) ([]string, error) {

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


// read input and expand to fit specified dimensions
// true indicates tree, false indicates no tree
func readInput(fileName string, x, y int) ([][]bool, error) {

	rawInput, err := readFileofStrings(fileName)
	if err != nil {
		return nil, err
	}

	return nil, nil
}

// x and y denote how
func countTrees(terrain [][]bool, x, y int) int {
	return 0
}


func main() {
	testTerrain := readInput("test_input", 3, 1)
	testTreeCount := countTrees(testTerrain, 3, 1)
	expectedTrees := 7
	if testTreeCount != expectedTrees {
		fmt.Printf("test input found %d trees, expected %d", testTreeCount, expectedTrees)
		return
	}


}