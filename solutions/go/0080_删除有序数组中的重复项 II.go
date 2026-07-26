package main

// 80. 删除有序数组中的重复项 II
// 快慢双指针：每个元素至多出现两次。
// 通用判断：slow < k 或 nums[fast] != nums[slow-k]（k=2）。
func removeDuplicates(nums []int) int {
	k := 2
	slow := 0
	for fast := 0; fast < len(nums); fast++ {
		if slow < k || nums[fast] != nums[slow-k] {
			nums[slow] = nums[fast]
			slow++
		}
	}
	return slow
}