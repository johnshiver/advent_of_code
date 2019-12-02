package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestReqMass(t *testing.T) {
	type test struct {
		input    int
		expected int
	}
	tests := []test{
		{input: 12, expected: 2},
		{input: 14, expected: 2},
		{input: 1969, expected: 654},
		{input: 100756, expected: 33583},
	}

	for _, tt := range tests {
		assert.Equal(t, tt.expected, calculateReqMass(tt.input))
	}
}

func TestReqMassAndFuel(t *testing.T) {
	type test struct {
		input    int
		expected int
	}
	tests := []test{
		{input: 12, expected: 2},
		{input: 1969, expected: 966},
		{input: 100756, expected: 50346},
	}

	for _, tt := range tests {
		assert.Equal(t, tt.expected, calcReqMassAndFuel(tt.input))
	}
}
