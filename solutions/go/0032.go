func longestValidParentheses(s string) int {
    n := len(s)
    if n < 2 {
        return 0
    }
    
    // dp[i] 表示以第i个字符结尾的最长有效括号长度
    dp := make([]int, n)
    maxLen := 0
    
    for i := 1; i < n; i++ {
        if s[i] == ')' {
            if s[i-1] == '(' {
                // 情况1: s[i-1] == '('，直接匹配
                if i >= 2 {
                    dp[i] = dp[i-2] + 2
                } else {
                    dp[i] = 2
                }
            } else if dp[i-1] > 0 {
                // 情况2: s[i-1] == ')'，需要找到匹配的左括号
                // 检查 s[i-dp[i-1]-1] 是否是 '('
                leftIndex := i - dp[i-1] - 1
                if leftIndex >= 0 && s[leftIndex] == '(' {
                    dp[i] = dp[i-1] + 2
                    // 还要加上 leftIndex 前面的有效括号长度
                    if leftIndex > 0 {
                        dp[i] += dp[leftIndex-1]
                    }
                }
            }
            maxLen = max(maxLen, dp[i])
        }
    }
    
    return maxLen
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}