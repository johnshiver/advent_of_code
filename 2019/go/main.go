package main

import "os"

func main() {
	prog := os.Args[1]
	switch prog {
	case "1":
		day1()
	case "2":
		day2()
	case "3":
		day3()
	case "4":
		day4()
	default:
		panic("no program to run")
	}
}
