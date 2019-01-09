package main

import (
	"fmt"
	"log"
	"strconv"
	"strings"
)

type recipeList struct {
	firstRecipe *recipe
	lastRecipe  *recipe
}

func (rl *recipeList) len() int {
	total := 0
	cur := rl.firstRecipe
	for cur != rl.lastRecipe {
		total++
		cur = cur.nextRecipe
	}
	return total
}

func (rl *recipeList) printNextTen(targetRecipe int) {
	cur := rl.firstRecipe
	for i := 0; i < targetRecipe; i++ {
		cur = cur.nextRecipe
	}
	answer := []string{}
	for i := 0; i < 10; i++ {
		score := strconv.Itoa(cur.score)
		answer = append(answer, score)
		cur = cur.nextRecipe
	}
	fmt.Println(strings.Join(answer, " "))

}

func (rl *recipeList) print(elf1, elf2 *recipe) {
	scores := []string{}
	cur := rl.firstRecipe
	for cur != rl.lastRecipe {
		score := strconv.Itoa(cur.score)
		if cur == elf1 {
			scores = append(scores, fmt.Sprintf("(%s)", score))

		}
		if cur == elf2 {
			scores = append(scores, fmt.Sprintf("[%s]", score))

		}
		if cur != elf1 && cur != elf2 {
			scores = append(scores, score)
		}
		cur = cur.nextRecipe
	}

	score := strconv.Itoa(cur.score)
	if cur == elf1 {
		scores = append(scores, fmt.Sprintf("(%s)", score))

	}
	if cur == elf2 {
		scores = append(scores, fmt.Sprintf("[%s]", score))

	}
	if cur != elf1 && cur != elf2 {
		scores = append(scores, score)
	}

	fmt.Println(strings.Join(scores, " "))
}

func (rl *recipeList) addRecipe(score int) {
	if score > 9 {
		err := fmt.Errorf("can only add recipe score of 0-9")
		log.Fatal(err)
	}
	newRecipe := &recipe{score: score}
	if rl.firstRecipe == nil {
		rl.firstRecipe = newRecipe
		rl.lastRecipe = newRecipe
	} else {
		prevLastRecipe := rl.lastRecipe
		prevLastRecipe.nextRecipe = newRecipe
		rl.lastRecipe = newRecipe
	}
	newRecipe.nextRecipe = rl.firstRecipe

}

type recipe struct {
	score      int
	nextRecipe *recipe
}

func getDigitsFromInt(score int) []int {
	digits := []int{}

	strScore := strconv.Itoa(score)
	for _, s := range strScore {
		d, err := strconv.Atoi(string(s))
		if err != nil {
			log.Fatal(err)
		}
		digits = append(digits, d)
	}
	return digits

}

func part1() {
	targetRecipe := 637061

	recipeList := recipeList{}
	recipeList.addRecipe(3)
	recipeList.addRecipe(7)
	elf1 := recipeList.firstRecipe
	elf2 := recipeList.firstRecipe.nextRecipe
	recipeList.print(elf1, elf2)

	for recipeList.len() < targetRecipe+10 {
		nextRecipeVal := elf1.score + elf2.score

		digits := getDigitsFromInt(nextRecipeVal)
		for _, d := range digits {
			recipeList.addRecipe(d)
		}

		elf1score := elf1.score
		for i := 0; i < 1+elf1score; i++ {
			elf1 = elf1.nextRecipe
		}
		elf2score := elf2.score
		for i := 0; i < 1+elf2score; i++ {
			elf2 = elf2.nextRecipe
		}
		// recipeList.print(elf1, elf2)
	}
	recipeList.printNextTen(targetRecipe)
}

func main() {
	part1()

}
