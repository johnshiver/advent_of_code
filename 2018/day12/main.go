package main

import (
	"fmt"
	"log"
	"strings"

	"github.com/johnshiver/advent_of_code/2018/utils"
)

type simulation struct {
	generations map[int]*generation
	rules       map[string]string
}

func (s *simulation) getPlantCount(startingPot, numGeneration int) int {
	count := 0
	lastGen := s.generations[numGeneration]
	for i, v := range lastGen.plants {
		if v == "#" {
			count += i - startingPot
		}
	}
	return count
}

type generation struct {
	num    int
	plants []string
}

func createGenerationFromInitialState(num int, init []string) *generation {
	return &generation{num: num, plants: init}
}

func (g *generation) applyRules(rules map[string]string) {
	newState := []string{}
	for _, v := range g.plants {
		newState = append(newState, v)
	}
	for i := 0; i+5 < len(g.plants); i++ {
		writeIndex := i + 2
		c := g.plants[i : i+5]
		curr := strings.Join(c, "")
		if _, ok := rules[curr]; !ok {
			newState[writeIndex] = "."
			continue
		}
		newState[writeIndex] = rules[curr]
	}
	g.plants = newState
}

func parseInitStateAndRulesFromInput(inputFile string) (string, map[string]string) {
	lines, err := utils.ReadFileofStrings(inputFile)
	if err != nil {
		log.Fatal(err)
	}
	initialState := lines[0]
	initialState = initialState[15:]
	rules := make(map[string]string)
	for _, line := range lines[2:] {
		rule := line[:5]
		outcome := line[9]
		rules[rule] = string(outcome)
	}
	return initialState, rules

}

func part1() {

	// const numGeneration = 20
	const numGeneration = 500

	init, rules := parseInitStateAndRulesFromInput("input.txt")
	p1Simulation := &simulation{rules: rules, generations: make(map[int]*generation)}
	bufferSize := 10000
	buffer := []string{}
	for i := 0; i < bufferSize; i++ {
		buffer = append(buffer, ".")
	}
	initialState := strings.Split(init, "")
	buffer = append(buffer, initialState...)
	for i := 0; i < bufferSize; i++ {
		buffer = append(buffer, ".")
	}

	prevGeneration := createGenerationFromInitialState(0, buffer)
	//	p1Simulation.generations[0] = prevGeneration
	for n := 1; n <= numGeneration; n++ {
		newGeneration := createGenerationFromInitialState(n, prevGeneration.plants)
		//	p1Simulation.generations[n] = newGeneration
		newGeneration.applyRules(p1Simulation.rules)
		prevGeneration = newGeneration
		if n == numGeneration {
			p1Simulation.generations[n] = newGeneration
		}
	}
	// for n := 0; n < numGeneration; n++ {
	// 	fmt.Println(n, strings.Join(p1Simulation.generations[n].plants, ""))
	// }
	fmt.Println(p1Simulation.getPlantCount(bufferSize, numGeneration))
}

func main() {
	part1()
}
