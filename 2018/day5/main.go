package main

import (
	"fmt"
	"log"
	"strings"

	"github.com/johnshiver/advent_of_code/2018/utils"
)

func checkReactions(polymerString string) []int {
	i := 0
	j := 1
	ps := string(polymerString)
	deadLinks := make([]int, len(ps))
	for j < len(ps) {
		ch1 := ps[i]
		ch2 := ps[j]

		if strings.ToLower(string(ch1)) == strings.ToLower(string(ch2)) && ch1 != ch2 {
			deadLinks[i] = 1
			deadLinks[j] = 1
			i += 2
			j += 2
		} else {
			i++
			j++
		}
	}
	return deadLinks
}

func removeDeadLinks(polymerString string, deadLinks []int) string {
	ps := string(polymerString)
	finalBytes := []byte{}
	for i := 0; i < len(ps); i++ {
		if deadLinks[i] == 1 {
			continue
		}
		finalBytes = append(finalBytes, ps[i])
	}
	return string(finalBytes)
}

func reducePolymer(polymerString string) string {
	inProgress := true
	for inProgress {
		deadLinks := checkReactions(polymerString)
		if len(deadLinks) < 1 {
			inProgress = false
		}
		numLinks := 0
		for i := 0; i < len(deadLinks); i++ {
			if deadLinks[i] == 1 {
				numLinks++
			}
		}
		if numLinks == 0 {
			inProgress = false
		}
		polymerString = removeDeadLinks(polymerString, deadLinks)
	}
	return polymerString
}

func removeElement(e1, e2 byte, polymerString string) []int {
	i := 0
	ps := string(polymerString)
	deadLinks := make([]int, len(ps))
	for i < len(ps) {
		ch1 := ps[i]
		if ch1 == e1 || ch1 == e2 {
			deadLinks[i] = 1
		}
		i++
	}
	return deadLinks
}

func part2(polymerString string, elemChan chan []int, results chan int) {
	for deadElements := range elemChan {
		newPolymer := removeDeadLinks(polymerString, deadElements)
		reducedPolymer := reducePolymer(newPolymer)
		results <- len(reducedPolymer)
	}
}

func main() {
	theString, err := utils.ReadFileofStrings("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	polymerString := theString[0]
	smallestChange := 320000000
	alphabet := "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
	i := 0
	j := 1
	elemnChan := make(chan []int, 26)
	results := make(chan int, 26)
	for w := 0; w < 8; w++ {
		go part2(polymerString, elemnChan, results)
	}
	for j < len(alphabet) {
		deadElements := removeElement(alphabet[i], alphabet[j], polymerString)
		elemnChan <- deadElements
		i += 2
		j += 2
	}

	for c := 0; c < 26; c++ {
		polymerSize := <-results
		fmt.Println(polymerSize)
		if polymerSize < smallestChange {
			smallestChange = polymerSize
		}
	}
	fmt.Println(smallestChange)
}
