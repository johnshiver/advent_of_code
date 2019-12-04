package main

func main() {
	//prog := os.Args[1]
	prog := "3"
	switch prog {
	case "1":
		day1()
	case "2":
		day2()
	case "3":
		day3()
	default:
		panic("no program to run")
	}
}
