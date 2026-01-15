func canJump(nums []int) bool {
	// canJump 判断是否可以到达最后一个下标
	//
	// 时间复杂度: O(n)
	//   - 只需遍历数组一次
	// 空间复杂度: O(1)
	//   - 只使用了常数额外空间
	//
	// 思路: 贪心
	// 1. 维护当前能到达的最远位置 farthest
	// 2. 从左到右遍历数组：
	//    - 如果当前位置 i 已经超过 farthest，说明 i 不可达，直接返回 false
	//    - 否则更新 farthest = max(farthest, i + nums[i])
	// 3. 若 farthest >= 最后下标，则可以到达，返回 true
	//
	// 示例:
	// nums = [2,3,1,1,4]
	// i=0 farthest=max(0,0+2)=2
	// i=1 farthest=max(2,1+3)=4 >= 4 => true
	if len(nums) == 0 {
		return false
	}

	farthest := 0
	last := len(nums) - 1

	for i := 0; i < len(nums); i++ {
		if i > farthest {
			return false
		}
		reach := i + nums[i]
		if reach > farthest {
			farthest = reach
		}
		if farthest >= last {
			return true
		}
	}

	return true
}