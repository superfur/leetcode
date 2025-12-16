func solveNQueens(n int) [][]string {
	var result [][]string
	// queens[i] 表示第 i 行皇后所在的列位置
	queens := make([]int, n)
	
	var backtrack func(row int)
	backtrack = func(row int) {
		// 所有行都放置了皇后，找到一个解
		if row == n {
			solution := make([]string, n)
			for i := 0; i < n; i++ {
				rowStr := make([]byte, n)
				for j := 0; j < n; j++ {
					if queens[i] == j {
						rowStr[j] = 'Q'
					} else {
						rowStr[j] = '.'
					}
				}
				solution[i] = string(rowStr)
			}
			result = append(result, solution)
			return
		}
		
		// 尝试在当前行的每一列放置皇后
		for col := 0; col < n; col++ {
			// 检查当前位置是否安全
			if isValid(queens, row, col) {
				queens[row] = col
				backtrack(row + 1)
				// 回溯：不需要显式恢复，因为会被覆盖
			}
		}
	}
	
	backtrack(0)
	return result
}

// isValid 检查在 (row, col) 位置放置皇后是否安全
func isValid(queens []int, row, col int) bool {
	for i := 0; i < row; i++ {
		// 检查是否在同一列
		if queens[i] == col {
			return false
		}
		// 检查是否在同一主对角线（左上到右下）：row - col 相同
		if i-queens[i] == row-col {
			return false
		}
		// 检查是否在同一副对角线（右上到左下）：row + col 相同
		if i+queens[i] == row+col {
			return false
		}
	}
	return true
}