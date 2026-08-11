package main

// 85. 最大矩形
// 逐行累加直方图高度 heights[j]，对每行 heights 调用单调栈求最大矩形。
func maximalRectangle(matrix [][]byte) int {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return 0
	}
	cols := len(matrix[0])
	heights := make([]int, cols)
	maxArea := 0
	for _, row := range matrix {
		for j := 0; j < cols; j++ {
			if row[j] == '1' {
				heights[j]++
			} else {
				heights[j] = 0
			}
		}
		if a := largestArea(heights); a > maxArea {
			maxArea = a
		}
	}
	return maxArea
}

func largestArea(heights []int) int {
	stack := make([]int, 0)
	best := 0
	extended := append(heights, 0) // 哨兵
	for i, h := range extended {
		for len(stack) > 0 && extended[stack[len(stack)-1]] > h {
			top := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			height := extended[top]
			width := i
			if len(stack) > 0 {
				width = i - stack[len(stack)-1] - 1
			}
			if height*width > best {
				best = height * width
			}
		}
		stack = append(stack, i)
	}
	return best
}