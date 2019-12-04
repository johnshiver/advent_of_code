package main

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestGetWireCrossDistance(t *testing.T) {
	type test struct {
		wires    []string
		expected int
	}
	tests := []test{
		{
			wires:    []string{"R8,U5,L5,D3", "U7,R6,D4,L4"},
			expected: 6,
		},
		{
			wires:    []string{"R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"},
			expected: 159,
		},
		{
			wires:    []string{"R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"},
			expected: 135,
		},
	}

	for _, tt := range tests {
		require.Equal(t, tt.expected, findCrossedWires(tt.wires))
	}
}

func TestGetWireMinSignalDelay(t *testing.T) {
	type test struct {
		wires    []string
		expected int
	}
	tests := []test{
		{
			wires:    []string{"R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"},
			expected: 610,
		},
		{
			wires:    []string{"R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"},
			expected: 410,
		},
	}

	for _, tt := range tests {
		require.Equal(t, tt.expected, findMinSignalDelay(tt.wires))
	}
}
