package main

// 91. 解码方法
// 动态规划：dp[i] 表示 s[:i] 的解码方法数。
// 单字符有效（非 '0'）时可从 dp[i-1] 转移；
// 双字符在 10~26 之间时可从 dp[i-2] 转移。
// 用两个变量滚动即可，无需数组。
func numDecodings(s string) int {
	n := len(s)
	prev2, prev1 := 1, 0
	if s[0] != '0' {
		prev1 = 1
	}
	for i := 2; i <= n; i++ {
		cur := 0
		if s[i-1] != '0' {
			cur += prev1
		}
		twoDigit := int(s[i-2]-'0')*10 + int(s[i-1]-'0')
		if twoDigit >= 10 && twoDigit <= 26 {
			cur += prev2
		}
		prev2, prev1 = prev1, cur
	}
	return prev1
}
