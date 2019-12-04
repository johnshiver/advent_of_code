package main

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestValidPw(t *testing.T) {
	type test struct {
		input    int
		expected bool
	}
	tests := []test{
		{input: 111111, expected: true},
		{input: 223450, expected: false},
		{input: 123789, expected: false},
	}

	for _, tt := range tests {
		require.Equal(t, tt.expected, validPwd(tt.input))
	}
}

func TestValidPw2(t *testing.T) {
	type test struct {
		input    int
		expected bool
	}
	tests := []test{
		{input: 112233, expected: true},
		{input: 123444, expected: false},
		{input: 111122, expected: true},
	}

	for _, tt := range tests {
		require.Equal(t, tt.expected, validPwd2(tt.input))
	}
}
