package main

// 75. 颜色分类
// 荷兰国旗算法，三指针一趟扫描原地排序
func sortColors(nums []int) {
	low, current, high := 0, 0, len(nums)-1
	for current <= high {
		switch nums[current] {
		case 0:
			nums[low], nums[current] = nums[current], nums[low]
			low++
			current++
		case 2:
			nums[current], nums[high] = nums[high], nums[current]
			high--
		default:
			current++
		}
	}
}
