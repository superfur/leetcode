package main

// 79. 单词搜索
// 回溯 DFS：枚举起点，四个方向递归搜索 word[k+1..]，
// 走过一格后用 0 标记，回溯时还原，避免重复使用。
func exist(board [][]byte, word string) bool {
	m, n := len(board), len(board[0])
	if m == 0 || n == 0 || word == "" {
		return false
	}

	var dfs func(i, j, k int) bool
	dfs = func(i, j, k int) bool {
		if k == len(word) {
			return true
		}
		if i < 0 || i >= m || j < 0 || j >= n || board[i][j] != word[k] {
			return false
		}
		saved := board[i][j]
		board[i][j] = 0
		found := dfs(i+1, j, k+1) ||
			dfs(i-1, j, k+1) ||
			dfs(i, j+1, k+1) ||
			dfs(i, j-1, k+1)
		board[i][j] = saved
		return found
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if dfs(i, j, 0) {
				return true
			}
		}
	}
	return false
}