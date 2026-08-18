package main

// 89. 格雷编码
// 经典公式：gray(i) = i ^ (i >> 1)。
func grayCode(n int) []int {
	size := 1 << n
	result := make([]int, size)
	for i := 0; i < size; i++ {
		result[i] = i ^ (i >> 1)
	}
	return result
}