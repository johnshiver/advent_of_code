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

func main() {
	theString, err := utils.ReadFileofStrings("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	polymerString := theString[0]
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
	fmt.Println(polymerString)
	fmt.Println(len(polymerString))
}
