impl Solution {
    pub fn longest_valid_parentheses(s: String) -> i32 {
        let n = s.len();
        if n < 2 {
            return 0;
        }
        
        // dp[i] 表示以第i个字符结尾的最长有效括号长度
        let mut dp = vec![0; n];
        let mut max_len = 0;
        let s_bytes = s.as_bytes();
        
        for i in 1..n {
            if s_bytes[i] == b')' {
                if s_bytes[i - 1] == b'(' {
                    // 情况1: s[i-1] == '('，直接匹配
                    if i >= 2 {
                        dp[i] = dp[i - 2] + 2;
                    } else {
                        dp[i] = 2;
                    }
                } else if dp[i - 1] > 0 {
                    // 情况2: s[i-1] == ')'，需要找到匹配的左括号
                    // 检查 s[i-dp[i-1]-1] 是否是 '('
                    let left_index = i - dp[i - 1] - 1;
                    if left_index < n && s_bytes[left_index] == b'(' {
                        dp[i] = dp[i - 1] + 2;
                        // 还要加上 left_index 前面的有效括号长度
                        if left_index > 0 {
                            dp[i] += dp[left_index - 1];
                        }
                    }
                }
                max_len = max_len.max(dp[i]);
            }
        }
        
        max_len as i32
    }
}