package main

// 137. 只出现一次的数字 II
// 逐位统计：出现三次的数，每一位上的 1 的个数一定是 3 的倍数，
// 所以把所有数在第 i 位上的 1 加起来对 3 取模，余数就是答案在第 i 位的值。
// Go 的 int 是 64 位，而题目数据是 int32：用 int32 累积结果，
// 第 31 位置 1 时自然得到负数，再转回 int 返回。时间 O(32n)，空间 O(1)。
func singleNumber(nums []int) int {
	var result int32
	for i := 0; i < 32; i++ {
		ones := 0
		for _, x := range nums {
			ones += (x >> i) & 1
		}
		if ones%3 != 0 {
			result |= int32(1) << i
		}
	}
	return int(result)
}
