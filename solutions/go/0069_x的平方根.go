package main

import "fmt"

func mySqrt(x int) int {
	if x < 2 {
		return x
	}
	left, right := 1, x/2
	for left <= right {
		mid := (left + right) / 2
		sq := mid * mid
		if sq == x {
			return mid
		} else if sq < x {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return right
}

func main() {
	cases := [][2]int{{4, 2}, {8, 2}, {0, 0}, {1, 1}, {9, 3}, {2147395600, 46340}}
	for _, tc := range cases {
		result := mySqrt(tc[0])
		ok := "PASS"
		if result != tc[1] {
			ok = "FAIL"
		}
		fmt.Printf("mySqrt(%d) = %d, expected %d: %s\n", tc[0], result, tc[1], ok)
	}
}
