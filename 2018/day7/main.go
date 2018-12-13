package main

import (
	"fmt"
	"log"
	"sort"
	"strings"

	"github.com/johnshiver/advent_of_code/2018/utils"
)

type Node struct {
	label     string
	deps      []*Node
	parents   []*Node
	priority  int
	scheduled bool
	finished  bool
}

func (n *Node) ready() bool {
	for _, d := range n.parents {
		if d.finished != true {
			return false
		}
	}
	return true
}

func parseNodesFromLine(l string) (string, string) {
	// assumes they'll be in the same position for each input
	// first val is dependency node of the second val
	return string(l[5]), string(l[36])
}

func buildGraph(nodeDeps []string) (map[string]*Node, string) {
	// returns graph and root node

	var root string
	graph := make(map[string]*Node)
	allNods := make(map[string]bool)
	for _, nd := range nodeDeps {
		dep, nod := parseNodesFromLine(nd)
		allNods[nod] = true
		if _, ok := graph[dep]; !ok {
			newNode := Node{label: dep}
			graph[dep] = &newNode
		}
		if _, ok := graph[nod]; !ok {
			newNode := Node{label: nod}
			graph[nod] = &newNode
		}
		graph[dep].deps = append(graph[dep].deps, graph[nod])
		graph[nod].parents = append(graph[nod].parents, graph[dep])
	}

	for label := range graph {
		if _, ok := allNods[label]; !ok {
			root = label
			break
		}
	}

	return graph, root
}

func printGraphByOrder(graph map[string]*Node) {
	nodeVals := []string{}
	sortedNodes := []*Node{}
	for _, n := range graph {
		sortedNodes = append(sortedNodes, n)
	}

	sort.Slice(sortedNodes, func(i, j int) bool {
		return sortedNodes[i].priority < sortedNodes[j].priority
	})

	for _, n := range sortedNodes {
		nodeVals = append(nodeVals, n.label)
	}
	fmt.Println(strings.Join(nodeVals, ""))

}

func printGraph(nodes map[string]*Node, root string) {

}

func calculateOrder(nodes map[string]*Node) map[string]*Node {
	priority := 0
	scheduledNodes := []*Node{}
	for _, n := range nodes {
		if n.ready() {
			fmt.Println("First scheduled node is ", n.label)
			n.scheduled = true
		}
		scheduledNodes = append(scheduledNodes, n)
	}
	for priority < len(scheduledNodes) {
		sort.Slice(scheduledNodes, func(i, j int) bool {
			switch strings.Compare(scheduledNodes[i].label, scheduledNodes[j].label) {
			case -1:
				return true
			case 1:
				return false
			}
			if scheduledNodes[i].ready() && !scheduledNodes[j].ready() {
				return false
			}
			return true
		})

		var current *Node
		for _, n := range scheduledNodes {
			if n.scheduled == true && n.ready() && !n.finished {
				current = n
				break
			}
		}
		current.finished = true
		current.priority = priority
		priority++
		fmt.Println("Setting priority ", current.label, current.priority)
		for _, dep := range current.deps {
			fmt.Println("Adding ", dep.label)
			dep.scheduled = true
		}
	}
	return nodes
}

func main() {
	inputs, err := utils.ReadFileofStrings("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	nodeGraph, root := buildGraph(inputs)
	fmt.Println(root)
	calculateOrder(nodeGraph)
	printGraphByOrder(nodeGraph)
}
