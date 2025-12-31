// maxSubArray 返回数组中连续子数组的最大和
//
// 时间复杂度: O(n)
//   - 只需遍历数组一次
// 空间复杂度: O(1)
//   - 只使用了常数额外空间
//
// 思路: 使用 Kadane 算法（动态规划/贪心思想）
// 1. 遍历数组，维护两个变量：
//    - currentSum: 以当前元素结尾的最大子数组和
//    - maxSum: 全局最大子数组和
// 2. 对于每个元素：
//    - 如果 currentSum < 0，说明之前的子数组是负贡献，应该舍弃
//      从当前元素重新开始（currentSum = nums[i]）
//    - 否则，将当前元素加入子数组（currentSum += nums[i]）
//    - 更新全局最大值 maxSum = max(maxSum, currentSum)
//
// 核心思想: 当累加和变为负数时，说明这部分对后续没有贡献，
//           应该丢弃，从下一个元素重新开始计算
//
// 示例:
// nums = [-2,1,-3,4,-1,2,1,-5,4]
// 最大子数组为 [4,-1,2,1]，和为 6
func maxSubArray(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	
	maxSum := nums[0]
	currentSum := nums[0]
	
	// 从第二个元素开始遍历
	for i := 1; i < len(nums); i++ {
		// 如果当前累加和为负，舍弃之前的部分，从当前元素重新开始
		if currentSum < 0 {
			currentSum = nums[i]
		} else {
			// 否则继续累加当前元素
			currentSum += nums[i]
		}
		
		// 更新全局最大值
		if currentSum > maxSum {
			maxSum = currentSum
		}
	}
	
	return maxSum
}