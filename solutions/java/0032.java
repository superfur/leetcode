class Solution {
    public int longestValidParentheses(String s) {
        int n = s.length();
        if (n < 2) {
            return 0;
        }
        
        // dp[i] 表示以第i个字符结尾的最长有效括号长度
        int[] dp = new int[n];
        int maxLen = 0;
        
        for (int i = 1; i < n; i++) {
            if (s.charAt(i) == ')') {
                if (s.charAt(i - 1) == '(') {
                    // 情况1: s[i-1] == '('，直接匹配
                    if (i >= 2) {
                        dp[i] = dp[i - 2] + 2;
                    } else {
                        dp[i] = 2;
                    }
                } else if (dp[i - 1] > 0) {
                    // 情况2: s[i-1] == ')'，需要找到匹配的左括号
                    // 检查 s[i-dp[i-1]-1] 是否是 '('
                    int leftIndex = i - dp[i - 1] - 1;
                    if (leftIndex >= 0 && s.charAt(leftIndex) == '(') {
                        dp[i] = dp[i - 1] + 2;
                        // 还要加上 leftIndex 前面的有效括号长度
                        if (leftIndex > 0) {
                            dp[i] += dp[leftIndex - 1];
                        }
                    }
                }
                maxLen = Math.max(maxLen, dp[i]);
            }
        }
        
        return maxLen;
    }
}