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

func (s *simulation) getPlantCount() int {
	plantCount := 0
	for _, g := range s.generations {
		plantCount += strings.Count(g.plants, "#")
	}
	return plantCount
}

type generation struct {
	num          int
	plants       []string
	zeroPotIndex int
}

/*

 */

func createGenerationFromInitialState(num, start int, init string) *generation {
	// must have 5 plants buffered on either side
	initState := strings.TrimLeft(init, ".")
	initState = strings.TrimRight(init, ".")
	initState = strings.Repeat(".", 5) + init + strings.Repeat(".", 5)
	return &generation{num: num, plants: initState, zeroPotIndex: start}

}

func (g *generation) applyRules(rules map[string]string) {
	newState := []string{}
	for i := 0; i+5 < len(g.plants); i++ {
		curr := g.plants[i : i+5]
		if _, ok := rules[curr]; !ok {
			newState = append(newState, ".")
			fmt.Printf("Didnt find %s\n", curr)
		}
		newState = append(newState, rules[curr])
	}
	g.plants = strings.Join(newState, "")
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
	const numGeneration = 20
	initialState, rules := parseInitStateAndRulesFromInput("test_input.txt")
	testSimulation := &simulation{rules: rules, generations: make(map[int]*generation)}
	prevGeneration := createGenerationFromInitialState(0, 0, initialState)
	for n := 0; n < numGeneration; n++ {
		newGeneration := createGenerationFromInitialState(n, prevGeneration.zeroPotIndex, prevGeneration.plants)
		testSimulation.generations[n] = newGeneration
		newGeneration.applyRules(testSimulation.rules)
		prevGeneration = newGeneration
	}
	fmt.Println(testSimulation.getPlantCount())
	for n := 0; n < numGeneration; n++ {
		fmt.Println(n, testSimulation.generations[n].plants)
	}
}

func main() {
	part1()

}
