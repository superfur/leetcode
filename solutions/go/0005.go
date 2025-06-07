package main

func longestPalindrome(s string) string {
	if len(s) <= 1 {
		return s
	}
	
	maxLen := 1
	begin := 0
	
	// 创建二维动态规划数组
	dp := make([][]bool, len(s))
	for i := range dp {
		dp[i] = make([]bool, len(s))
	}
	
	// 单个字符都是回文
	for i := 0; i < len(s); i++ {
		dp[i][i] = true
	}
	
	// 动态规划填充
	for j := 1; j < len(s); j++ {
		for i := 0; i < j; i++ {
			if s[i] != s[j] {
				dp[i][j] = false
			} else {
				if j-i < 3 {
					dp[i][j] = true
				} else {
					dp[i][j] = dp[i+1][j-1]
				}
				
				if dp[i][j] && j-i+1 > maxLen {
					maxLen = j - i + 1
					begin = i
				}
			}
		}
	}
	
	return s[begin : begin+maxLen]
}

