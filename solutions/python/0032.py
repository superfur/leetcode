class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0
        
        # dp[i] 表示以第i个字符结尾的最长有效括号长度
        dp = [0] * n
        max_len = 0
        
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    # 情况1: s[i-1] == '('，直接匹配
                    if i >= 2:
                        dp[i] = dp[i - 2] + 2
                    else:
                        dp[i] = 2
                elif dp[i - 1] > 0:
                    # 情况2: s[i-1] == ')'，需要找到匹配的左括号
                    # 检查 s[i-dp[i-1]-1] 是否是 '('
                    left_index = i - dp[i - 1] - 1
                    if left_index >= 0 and s[left_index] == '(':
                        dp[i] = dp[i - 1] + 2
                        # 还要加上 left_index 前面的有效括号长度
                        if left_index > 0:
                            dp[i] += dp[left_index - 1]
                max_len = max(max_len, dp[i])
        
        return max_len