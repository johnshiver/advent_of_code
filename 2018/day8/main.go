package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Node struct {
	children      []*Node
	label         int
	start         int
	metaDataCount int
}

func (n *Node) lastChildPos() int {
	// might be good to cache this
	var pos int
	for _, child := range n.children {
		if child.end() > pos {
			pos = child.end()
		}
	}
	return pos
}

func (n *Node) end() int {
	if len(n.children) > 0 {
		return n.lastChildPos() + n.metaDataCount
	}
	return n.start + n.metaDataCount + 1
}

// returns positions metadata vals will occur in the tree array
func (n *Node) getMetaDataValPos() []int {
	if len(n.children) > 0 {
		return []int{n.lastChildPos() + 1, n.end() + 1}
	}
	return []int{n.start + 2, n.end() + 1}
}

func createArrayFromInput(filename string) []int {
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	allVals := []int{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		newLine := scanner.Text()
		if err != nil {
			log.Fatal(err)
		}
		for _, i := range strings.Split(newLine, " ") {
			val, err := strconv.Atoi(i)
			if err != nil {
				log.Fatal(err)
			}
			allVals = append(allVals, val)
		}
	}
	return allVals
}

func createTreeFromArray(treeVals []int) []*Node {
	startPos := 0
	label := 0
	allRoots := []*Node{}
	for startPos < len(treeVals) {
		newNode := createNode(treeVals, startPos, label)
		allRoots = append(allRoots, newNode)
		startPos = newNode.end() + 1
	}
	return allRoots
}

func createNode(treeVals []int, startPos, nodeLabel int) *Node {
	// check min size of a tree node
	// metadata includes number of children, min is 0, and metadata, which must at least be 1
	// so min is 3
	if startPos+2 > len(treeVals) {
		fmt.Printf("nil start %d label %d", startPos, nodeLabel)
		return nil
	}
	newNode := Node{label: nodeLabel, start: startPos, metaDataCount: treeVals[startPos+1], children: []*Node{}}
	noChild := treeVals[startPos]
	startPos = startPos + 2
	childLabel := nodeLabel + 1
	for i := 0; i < noChild; i++ {
		child := createNode(treeVals, startPos, childLabel)
		if child != nil {
			newNode.children = append(newNode.children, child)
		}
		startPos = child.end() + 1
		childLabel++
	}
	return &newNode
}

func main() {
	var input string
	input = "input.txt"
	tree := createArrayFromInput(input)
	roots := createTreeFromArray(tree)
	metaData := []int{}
	for _, n := range roots {
		allNodes := []*Node{}
		allNodes = append(allNodes, n)
		for len(allNodes) > 0 {
			curr := allNodes[0]
			allNodes = allNodes[1:]
			metaPos := curr.getMetaDataValPos()
			metadats := tree[metaPos[0]:metaPos[1]]
			metaData = append(metaData, metadats...)
			for _, child := range curr.children {
				allNodes = append(allNodes, child)
			}
		}

	}
	sum := 0
	for _, i := range metaData {
		sum += i
	}
	fmt.Println(sum)
}
