package main

// 118. 杨辉三角
// 逐行生成：每行首尾都是 1，中间第 j 个数等于上一行第 j-1 和第 j 个数之和。
func generate(numRows int) [][]int {
	result := make([][]int, numRows)
	for i := 0; i < numRows; i++ {
		row := make([]int, i+1)
		row[0] = 1
		row[i] = 1
		for j := 1; j < i; j++ {
			row[j] = result[i-1][j-1] + result[i-1][j]
		}
		result[i] = row
	}
	return result
}
