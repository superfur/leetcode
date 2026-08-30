impl Solution {
    /// 97. 交错字符串
    /// 一维滚动 DP：dp[j] 表示 s3 的前 i+j 个字符能否由
    /// s1 的前 i 个字符和 s2 的前 j 个字符交错组成（i 随外层循环推进）。
    /// 长度不匹配直接返回 false。
    pub fn is_interleave(s1: String, s2: String, s3: String) -> bool {
        let s1 = s1.as_bytes();
        let s2 = s2.as_bytes();
        let s3 = s3.as_bytes();
        let (m, n) = (s1.len(), s2.len());
        if m + n != s3.len() {
            return false;
        }

        let mut dp = vec![false; n + 1];
        dp[0] = true;
        for j in 1..=n {
            dp[j] = dp[j - 1] && s2[j - 1] == s3[j - 1];
        }

        for i in 1..=m {
            dp[0] = dp[0] && s1[i - 1] == s3[i - 1];
            for j in 1..=n {
                dp[j] = (dp[j] && s1[i - 1] == s3[i + j - 1]) || (dp[j - 1] && s2[j - 1] == s3[i + j - 1]);
            }
        }

        dp[n]
    }
}
