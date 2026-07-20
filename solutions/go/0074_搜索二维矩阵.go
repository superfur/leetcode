package main

func searchMatrix(matrix [][]int, target int) bool {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return false
	}

	m, n := len(matrix), len(matrix[0])
	left, right := 0, m*n-1

	for left <= right {
		mid := (left + right) / 2
		row, col := mid/n, mid%n
		val := matrix[row][col]

		switch {
		case val == target:
			return true
		case val < target:
			left = mid + 1
		default:
			right = mid - 1
		}
	}

	return false
}
