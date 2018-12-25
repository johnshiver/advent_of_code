package main

import (
	"fmt"
	"log"
	"regexp"
	"strconv"

	"github.com/johnshiver/advent_of_code/2018/utils"
)

const SPECIAL_MARBLE = 23

type Marble struct {
	num              int
	clockwise        *Marble
	counterClockwise *Marble
}

type Game struct {
	players       int
	playerScores  map[int]int
	lastMarble    int
	highScore     int
	testHighScore int
	marbles       []*Marble
	currentMarble *Marble
	currentElf    int
}

func (g *Game) playGame() {
	currMarbleVal := 0
	firstMarble := &Marble{num: currMarbleVal}
	firstMarble.clockwise = firstMarble
	firstMarble.counterClockwise = firstMarble
	g.currentMarble = firstMarble
	currMarbleVal++
	g.currentElf = 1
	for currMarbleVal < g.lastMarble {
		g.addMarble(currMarbleVal)
		currMarbleVal++
	}
	highScore := -1
	for _, score := range g.playerScores {
		if score > highScore {
			highScore = score
		}
	}
	g.highScore = highScore
}

func (g *Game) removeMarble(m *Marble) *Marble {
	g.playerScores[g.currentElf] += m.num
	m.counterClockwise.clockwise = m.clockwise
	m.clockwise.counterClockwise = m.counterClockwise
	return m.clockwise
}

func (g *Game) addMarble(val int) {
	if val%SPECIAL_MARBLE == 0 {
		// current elf keeps marble, adding it to their score
		g.playerScores[g.currentElf] += val
		// marble 7 marbles counter clockwise is removed and added to score
		marbleToRemove := g.currentMarble
		for i := 0; i < 7; i++ {
			marbleToRemove = marbleToRemove.counterClockwise
		}
		g.currentMarble = g.removeMarble(marbleToRemove)
	} else {
		newMarble := &Marble{num: val}
		left := g.currentMarble.clockwise
		right := g.currentMarble.clockwise.clockwise
		left.clockwise = newMarble
		right.counterClockwise = newMarble
		newMarble.counterClockwise = left
		newMarble.clockwise = right
		g.currentMarble = newMarble
	}
	g.currentElf++
	if g.currentElf > g.players {
		g.currentElf = 1
	}
}

func part1() {
	numberRegex := regexp.MustCompile(`[0-9]+`)
	testInputs, err := utils.ReadFileofStrings("test_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	testGames := []*Game{}
	for _, t := range testInputs {
		testNums := numberRegex.FindAllString(t, -1)

		numPlayers, err := strconv.Atoi(testNums[0])
		if err != nil {
			log.Fatal(err)
		}
		lastMarble, err := strconv.Atoi(testNums[1])
		if err != nil {
			log.Fatal(err)
		}
		testHighScore, err := strconv.Atoi(testNums[2])
		if err != nil {
			log.Fatal(err)
		}

		testGames = append(testGames, &Game{players: numPlayers,
			lastMarble:    lastMarble,
			testHighScore: testHighScore,
			playerScores:  make(map[int]int),
		})
	}
	for _, game := range testGames {
		game.playGame()
		fmt.Printf("Hi Score %d, expected score %d\n", game.highScore, game.testHighScore)
	}

	inputs, err := utils.ReadFileofStrings("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	var game Game
	for _, i := range inputs {
		inputNums := numberRegex.FindAllString(i, -1)
		fmt.Println(inputNums)
		numPlayers, err := strconv.Atoi(inputNums[0])
		if err != nil {
			log.Fatal(err)
		}
		lastMarble, err := strconv.Atoi(inputNums[1])
		if err != nil {
			log.Fatal(err)
		}
		game = Game{players: numPlayers, lastMarble: lastMarble, playerScores: make(map[int]int)}
	}
	game.playGame()
	fmt.Println(game.highScore)

}

func main() {
	part1()
}
