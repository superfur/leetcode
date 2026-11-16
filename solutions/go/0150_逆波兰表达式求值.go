package main

import "strconv"

// 150. 逆波兰表达式求值
// 用栈从左到右扫描：遇到数字就入栈；遇到运算符就弹出两个操作数计算，再把结果压回栈。
// 注意弹出的顺序：先弹出的是右操作数 b，后弹出的是左操作数 a，结果是 a op b（减法、除法顺序不能反）。
// Go 的整数除法本来就是向零截断，直接用 / 即可。
// 时间 O(n)，空间 O(n)。
func evalRPN(tokens []string) int {
	stack := make([]int, 0, len(tokens))
	for _, token := range tokens {
		switch token {
		case "+", "-", "*", "/":
			b := stack[len(stack)-1]
			a := stack[len(stack)-2]
			stack = stack[:len(stack)-2]
			var r int
			switch token {
			case "+":
				r = a + b
			case "-":
				r = a - b
			case "*":
				r = a * b
			default:
				r = a / b
			}
			stack = append(stack, r)
		default:
			num, _ := strconv.Atoi(token)
			stack = append(stack, num)
		}
	}
	return stack[0]
}
