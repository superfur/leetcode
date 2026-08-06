package main

// 84. 柱状图中最大的矩形
// 单调递增栈：栈中保存索引，对应高度严格递增。
// 遇到 heights[i] < heights[stack.top] 时弹栈并以弹出的高度为基准计算面积：
//   width = i - stack[len-2] - 1（栈空则为 i）。
// 末尾追加 0 哨兵确保所有柱子被清算。
func largestRectangleArea(heights []int) int {
	stack := make([]int, 0)
	maxArea := 0
	// 末尾追加 0 哨兵
	extended := append(heights, 0)
	for i, h := range extended {
		for len(stack) > 0 && extended[stack[len(stack)-1]] > h {
			top := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			height := extended[top]
			width := i
			if len(stack) > 0 {
				width = i - stack[len(stack)-1] - 1
			}
			if height*width > maxArea {
				maxArea = height * width
			}
		}
		stack = append(stack, i)
	}
	return maxArea
}