package main

// 136. 只出现一次的数字
// 位运算：a ^ a = 0，a ^ 0 = a，且异或满足交换律和结合律。
// 把所有数依次异或起来，成对出现的数两两抵消，剩下的就是只出现一次的那个。
// 时间 O(n)，空间 O(1)。
func singleNumber(nums []int) int {
	result := 0
	for _, x := range nums {
		result ^= x
	}
	return result
}
