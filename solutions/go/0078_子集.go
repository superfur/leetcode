package main

// 78. 子集
// 回溯枚举所有子集（幂集），数组元素互不相同
func subsets(nums []int) [][]int {
	result := make([][]int, 0)
	path := make([]int, 0)

	var dfs func(start int)
	dfs = func(start int) {
		cp := make([]int, len(path))
		copy(cp, path)
		result = append(result, cp)
		for i := start; i < len(nums); i++ {
			path = append(path, nums[i])
			dfs(i + 1)
			path = path[:len(path)-1]
		}
	}

	dfs(0)
	return result
}