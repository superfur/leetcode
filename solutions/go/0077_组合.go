package main

// 77. 组合
// 回溯 + 剪枝，返回 [1, n] 中所有 k 个数的组合
func combine(n int, k int) [][]int {
	result := make([][]int, 0)
	path := make([]int, 0, k)

	var dfs func(start int)
	dfs = func(start int) {
		if len(path) == k {
			cp := make([]int, k)
			copy(cp, path)
			result = append(result, cp)
			return
		}
		// 剪枝: i 最大值 = n - (k - len(path)) + 1
		upper := n - (k - len(path)) + 1
		for i := start; i <= upper; i++ {
			path = append(path, i)
			dfs(i + 1)
			path = path[:len(path)-1]
		}
	}

	dfs(1)
	return result
}
