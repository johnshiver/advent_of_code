package main

import (
	"fmt"
	"strconv"
)

func day4() {
	fmt.Printf("day4 pt1 output is: %d\n", day4pt1())
	fmt.Printf("day4 pt2 output is: %d\n", day4pt2())
}

func day4pt1() int {
	return validPwsInRange(183564, 657474)
}
func day4pt2() int {
	return validPwsInRange2(183564, 657474)
}

func validPwsInRange(x, y int) int {
	var validPwds int
	for x := x; x <= y; x++ {
		if validPwd(x) {
			validPwds++
		}
	}
	return validPwds
}

func validPwsInRange2(x, y int) int {
	var validPwds int
	for x := x; x <= y; x++ {
		if validPwd2(x) {
			validPwds++
		}
	}
	return validPwds
}

func validPwd(x int) bool {
	txInput := strconv.Itoa(x)
	// 6 digit num
	if len(txInput) != 6 {
		return false
	}

	var adjs bool
	alwaysInc := true
	for j := 1; j < 6; j++ {
		if txInput[j-1] == txInput[j] {
			adjs = true
		} else if txInput[j-1] > txInput[j] {
			alwaysInc = false
		}
	}
	return adjs && alwaysInc
}

func validPwd2(x int) bool {
	txInput := strconv.Itoa(x)
	// 6 digit num
	if len(txInput) != 6 {
		return false
	}

	var adjs bool
	alwaysInc := true
	for j := 1; j < 6; j++ {
		if txInput[j-1] == txInput[j] {
			if j-2 >= 0 && txInput[j-2] == txInput[j] {
				continue
			}
			if j+1 < 6 && txInput[j+1] == txInput[j] {
				continue
			}
			adjs = true
		} else if txInput[j-1] > txInput[j] {
			alwaysInc = false
		}
	}
	return adjs && alwaysInc
}
