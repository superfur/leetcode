// totalNQueens 返回 N 皇后问题不同解决方案的数量
//
// 时间复杂度: O(n!)
//   - 最坏情况下需要尝试所有可能的排列组合
//   - 但由于剪枝优化，实际运行时间远小于 O(n!)
// 空间复杂度: O(n)
//   - 递归调用栈深度为 O(n)
//
// 思路:
// 1. 使用回溯算法，逐行放置皇后
// 2. 使用位运算优化冲突检查：
//    - cols: 列占用情况（第 j 列被占用，则第 j 位为 1）
//    - diag1: 主对角线占用情况（row - col + n - 1 映射到位号）
//    - diag2: 副对角线占用情况（row + col 映射到位号）
// 3. 当所有行都放置了皇后，计数加一
//
// 优化:
// - 使用位运算代替数组遍历，大幅提升性能
// - 位运算检查冲突的时间复杂度为 O(1)
//
// 示例:
// n = 4 时，返回 2
func totalNQueens(n int) int {
	count := 0
	
	// backtrack 回溯函数
	// row: 当前要放置皇后的行号
	// cols: 已被占用的列集合（第 j 列占用，则第 j 位为 1）
	// diag1: 主对角线集合（row - col 固定，用 (row - col + n - 1) 映射到 [0, 2n-2]）
	// diag2: 副对角线集合（row + col 固定，直接用 row + col 映射到 [0, 2n-2]）
	var backtrack func(row int, cols int, diag1 int, diag2 int)
	backtrack = func(row int, cols int, diag1 int, diag2 int) {
		// 所有行都已放置皇后，找到一个有效解
		if row == n {
			count++
			return
		}
		
		// 尝试在当前行的每一列放置皇后
		for col := 0; col < n; col++ {
			d1 := row - col + n - 1
			d2 := row + col
			
			colBit := 1 << col
			d1Bit := 1 << d1
			d2Bit := 1 << d2
			
			// 检查是否有冲突
			if (cols & colBit) != 0 {
				continue
			}
			if (diag1 & d1Bit) != 0 {
				continue
			}
			if (diag2 & d2Bit) != 0 {
				continue
			}
			
			// 递归处理下一行
			backtrack(row+1, cols|colBit, diag1|d1Bit, diag2|d2Bit)
		}
	}
	
	backtrack(0, 0, 0, 0)
	return count
}