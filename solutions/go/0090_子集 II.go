package main

import "sort"

// 90. 子集 II
// 排序 + 回溯：同一层若 nums[i] == nums[i-1] 则跳过，避免重复子集。
func subsetsWithDup(nums []int) [][]int {
	sort.Ints(nums)
	result := [][]int{}
	path := []int{}

	var backtrack func(start int)
	backtrack = func(start int) {
		// 必须拷贝 path
		cur := make([]int, len(path))
		copy(cur, path)
		result = append(result, cur)
		for i := start; i < len(nums); i++ {
			if i > start && nums[i] == nums[i-1] {
				continue
			}
			path = append(path, nums[i])
			backtrack(i + 1)
			path = path[:len(path)-1]
		}
	}
	backtrack(0)
	return result
}