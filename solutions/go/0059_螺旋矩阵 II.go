package main

/*
 * 螺旋矩阵 II - 边界模拟法
 *
 * 时间复杂度: O(n²)，填充 n² 个元素
 * 空间复杂度: O(1)，除了结果矩阵外只使用常数个变量
 *
 * 思路:
 * 1. 创建 n×n 矩阵，定义四个边界：top, bottom, left, right
 * 2. 按照 右->下->左->上 的顺序填充数字 1 到 n²
 * 3. 每完成一个方向，更新对应的边界
 * 4. 当 num > n² 时停止
 *
 * 示例: n = 3
 * 输出: [[1,2,3],[8,9,4],[7,6,5]]
 */
func generateMatrix(n int) [][]int {
	matrix := make([][]int, n)
	for i := range matrix {
		matrix[i] = make([]int, n)
	}

	top, bottom := 0, n-1
	left, right := 0, n-1
	num := 1

	for num <= n*n {
		// 向右：填充 top 行
		for j := left; j <= right; j++ {
			matrix[top][j] = num
			num++
		}
		top++

		// 向下：填充 right 列
		for i := top; i <= bottom; i++ {
			matrix[i][right] = num
			num++
		}
		right--

		// 向左：填充 bottom 行（若有剩余行）
		if top <= bottom {
			for j := right; j >= left; j-- {
				matrix[bottom][j] = num
				num++
			}
			bottom--
		}

		// 向上：填充 left 列（若有剩余列）
		if left <= right {
			for i := bottom; i >= top; i-- {
				matrix[i][left] = num
				num++
			}
			left++
		}
	}

	return matrix
}
