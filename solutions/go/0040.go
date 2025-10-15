import "sort"

// combinationSum2 组合总和 II - 回溯算法
// 找出所有可以使数字和为目标数 target 的不同组合
// 每个数字在每个组合中只能使用一次，且解集不能包含重复的组合
//
// 算法思路：
// 1. 先对数组排序，便于处理重复元素
// 2. 使用回溯算法（DFS）遍历所有可能的组合
// 3. 每次选择当前数字或跳过，但每个数字只能使用一次
// 4. 当和等于 target 时，记录当前组合
// 5. 当和大于 target 时，剪枝返回
// 6. 通过起始索引和重复元素处理避免重复组合
//
// 时间复杂度：O(2^n)，n 是候选数组长度
// 空间复杂度：O(target)，递归栈的深度最多为 target
func combinationSum2(candidates []int, target int) [][]int {
	// 先排序，便于处理重复元素
	sort.Ints(candidates)
	
	var result [][]int
	var path []int
	
	backtrack(candidates, target, 0, 0, &path, &result)
	
	return result
}

// backtrack 回溯函数
//
// 参数：
//   candidates: 候选数字数组（已排序）
//   target: 目标和
//   start: 当前搜索的起始索引，避免重复组合
//   currentSum: 当前路径的和
//   path: 当前路径（指针传递，避免拷贝）
//   result: 存储所有有效组合的结果集（指针传递）
func backtrack(
	candidates []int,
	target int,
	start int,
	currentSum int,
	path *[]int,
	result *[][]int,
) {
	// 找到一个有效组合
	if currentSum == target {
		// 复制当前路径到结果中
		pathCopy := make([]int, len(*path))
		copy(pathCopy, *path)
		*result = append(*result, pathCopy)
		return
	}
	
	// 剪枝：当前和已经超过目标值
	if currentSum > target {
		return
	}
	
	// 从 start 开始遍历，避免重复组合
	for i := start; i < len(candidates); i++ {
		num := candidates[i]
		
		// 剪枝优化：如果加上当前数字已经超过目标，后续更大的数字也不用尝试
		if currentSum+num > target {
			break // 由于数组已排序，可以直接 break
		}
		
		// 关键：跳过重复元素，避免产生重复组合
		// 在同一层递归中，如果当前元素与前一个元素相同，则跳过
		// 这样可以避免产生如 [1,2,2] 和 [1,2,2] 这样的重复组合
		if i > start && candidates[i] == candidates[i-1] {
			continue
		}
		
		// 选择当前数字
		*path = append(*path, num)
		
		// 递归：注意这里是 i+1，因为每个数字只能使用一次
		backtrack(candidates, target, i+1, currentSum+num, path, result)
		
		// 撤销选择（回溯）
		*path = (*path)[:len(*path)-1]
	}
}