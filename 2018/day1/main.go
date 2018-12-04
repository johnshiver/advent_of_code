package main

import (
	"fmt"
	"log"

	"github.com/johnshiver/advent_of_code/2018/utils"
)

func part1() {
	allVals, err := utils.ReadFileofInts("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	runningCount := 0
	for _, val := range allVals {
		runningCount += val
	}
	fmt.Println(runningCount)
}

func part2() {
	allVals, err := utils.ReadFileofInts("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	foundSeen := false
	seenCounts := make(map[int]bool)
	runningCount := 0
	for !foundSeen {
		for _, val := range allVals {
			runningCount += val
			if _, ok := seenCounts[runningCount]; ok {
				fmt.Println(runningCount)
				foundSeen = true
				break
			}
			seenCounts[runningCount] = true
		}
	}
}

func main() {
	part1()
	part2()
}
