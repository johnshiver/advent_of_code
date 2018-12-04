package main

import (
	"fmt"
	"log"

	"github.com/johnshiver/advent_of_code/2018/utils"
)

const WORKER_COUNT = 1

type result struct {
	twos   int
	threes int
}

func parseID(valChan chan string, resultChan chan result) {
	for val := range valChan {
		valCount := make(map[rune]int)
		for _, char := range val {
			valCount[char]++
		}
		twos := 0
		threes := 0
		for _, count := range valCount {
			if count == 2 {
				twos++
			}
			if count == 3 {
				threes++
			}
		}
		resultChan <- result{twos: twos, threes: threes}
	}
}

func part1() {
	vals, err := utils.ReadFileofStrings("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	valChan := make(chan string, len(vals))
	resultChan := make(chan result, len(vals))
	for i := 0; i < WORKER_COUNT; i++ {
		go parseID(valChan, resultChan)
	}

	for _, val := range vals {
		valChan <- val
	}
	close(valChan)

	twos := 0
	threes := 0
	for i := 0; i < len(vals); i++ {
		r := <-resultChan
		if r.twos > 0 {
			twos++
		}
		if r.threes > 0 {
			threes++
		}
	}

	fmt.Println(twos * threes)
}

func compareIDs(vals []string, posChan chan int, resultChan chan string) {
	for pos := range posChan {
		valToCheck := vals[pos]
		otherVals := vals[:pos]
		otherVals = append(otherVals, vals[pos:]...)
		for _, v := range otherVals {
			mismatches := 0
			for i := 0; i < len(valToCheck); i++ {
				if valToCheck[i] != v[i] {
					mismatches++
				}
			}
			if mismatches == 1 {
				commonChars := []byte{}
				for i := 0; i < len(valToCheck); i++ {
					if valToCheck[i] == v[i] {
						commonChars = append(commonChars, valToCheck[i])
					}
				}
				resultChan <- string(commonChars)
			}
		}
	}
}

func part2() {
	vals, err := utils.ReadFileofStrings("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	posChan := make(chan int, len(vals))
	resultChan := make(chan string, 1)
	for i := range vals {
		posChan <- i
	}
	close(posChan)
	for i := 0; i < 1; i++ {
		go compareIDs(vals, posChan, resultChan)
	}

	for w := 0; w < 1; w++ {
		r := <-resultChan
		fmt.Println(r)
	}

}

func main() {
	part1()
	part2()
}
