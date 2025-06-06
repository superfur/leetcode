package main

import (
	"sort"
)
func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	// 合并两个数组
	merged := append(nums1, nums2...)
	
	// 对合并后的数组进行排序
	sort.Ints(merged)
	
	// 计算中位数
	length := len(merged)
	middle := length / 2
	
	if length%2 == 1 {
		return float64(merged[middle])
	} else {
		return float64(merged[middle-1]+merged[middle]) / 2.0
	}
}

func main() {
	// 测试用例
	nums1 := []int{1, 3}
	nums2 := []int{2}
	result := findMedianSortedArrays(nums1, nums2)
	println(result)
}

