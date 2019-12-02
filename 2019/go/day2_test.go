package main

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func TestIntCodeProgram(t *testing.T) {
	type test struct {
		input    []int
		pos int
		expected int
	}
	tests := []test{
		{input: []int{1, 0, 0, 0, 99}, pos: 0, expected: 2},
		// {input: []int{2, 3, 0, 6, 99}, pos: 3, expected: 6}, // this test case's input is wrong
		{input: []int{2, 4, 4, 5, 99, 0}, pos: 5, expected: 9801},
		{input: []int{1, 1, 1, 4, 99, 5, 6, 0, 99}, pos: 0, expected: 30},
	}
	for _, tt := range tests {
		require.Equal(t, tt.expected, intCodeProgram(tt.input)[tt.pos])
	}
}
