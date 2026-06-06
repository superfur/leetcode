package main

import "fmt"

func climbStairs(n int) int {
	if n <= 2 {
		return n
	}
	a, b := 1, 2
	for i := 3; i <= n; i++ {
		a, b = b, a+b
	}
	return b
}

func main() {
	cases := [][2]int{{1, 1}, {2, 2}, {3, 3}, {5, 8}, {10, 89}, {45, 1836311903}}
	for _, tc := range cases {
		result := climbStairs(tc[0])
		ok := "PASS"
		if result != tc[1] {
			ok = "FAIL"
		}
		fmt.Printf("climbStairs(%d) = %d, expected %d: %s\n", tc[0], result, tc[1], ok)
	}
}
