package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const DAY2_INPUT = "/home/jshiver/learning_is_good/advent_of_code/2019/inputs/day2.txt"

func day2() {
	fmt.Printf("day2 pt1 output is: %d\n", _day2pt1())
	fmt.Println("day2 pt2 output is:")
	_day2pt2()
}


func _day2pt1() int {
	nums, err := readDay2Input()
	if err != nil {
		panic(err)
	}
	nums[1] = 12
	nums[2] = 2
	return intCodeProgram(nums)[0]
}

func _day2pt2() {
	expectedOutput := 19690720
	for noun :=0; noun < 100; noun ++ {
		for verb :=0; verb < 100; verb++ {
			nums, err := readDay2Input()
			if err != nil {
				panic(err)
			}
			nums[1] = noun
			nums[2] = verb
			ret := intCodeProgram(nums)[0]
			if ret == expectedOutput {
				fmt.Printf("noun %d verb %d produced output", noun, verb)
				return
			}
		}
	}
	fmt.Println("no output could be found")
}

func nxPos(pos, totalLen int) int {
	if pos >= totalLen {
		return pos - totalLen
	}
	return pos
}

func intCodeProgram(program []int) []int {
	keepGoing := true
	opc := 0
	tl := len(program)
	for keepGoing {
		opCode := program[opc]
		r1 := program[nxPos(opc+1, tl)]
		r2 := program[nxPos(opc+2, tl)]
		w := program[nxPos(opc+3, tl)]
		switch opCode {
		case 1:
			program = addIntCode(program, r1, r2, w)
		case 2:
			program = multiIntCode(program, r1, r2, w)
		case 99:
			keepGoing = false
		default:
			panic(fmt.Errorf("opcode was %d", opCode))
		}
		opc += 4
		opc = nxPos(opc, tl)
	}
	return program
}

func addIntCode(prog []int, r1, r2, w int) []int {
	prog[w] = prog[r1] + prog[r2]
	return prog
}

func multiIntCode(prog []int, r1, r2, w int) []int {
	prog[w] = prog[r1] * prog[r2]
	return prog
}

func readDay2Input() ([]int, error) {
	file, err := os.Open(DAY2_INPUT)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var allVals []int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		newLine := scanner.Text()
		splits := strings.Split(newLine, ",")
		for _, s := range splits {
			newInt, err := strconv.Atoi(s)
			if err != nil {
				return nil, err
			}
			allVals = append(allVals, newInt)
		}
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}
	return allVals, nil
}
