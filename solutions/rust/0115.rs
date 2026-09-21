impl Solution {
    /// 115. 不同的子序列
    /// 一维滚动 DP：dp[j] 表示当前已处理的 s 前缀中，
    /// 有多少种方式能选出 t 的前 j 个字符作为子序列。
    /// dp[0] 恒为 1（空串永远只有一种“什么都不选”的方式）。
    /// s[i-1] == t[j-1] 时，dp[j] 既可以不用当前这个 s 字符
    /// （沿用旧的 dp[j]），也可以用它去匹配 t[j-1]（累加旧的 dp[j-1]），
    /// 所以要按 j 从大到小更新，避免用本轮已经更新过的值。
    pub fn num_distinct(s: String, t: String) -> i32 {
        let s = s.as_bytes();
        let t = t.as_bytes();
        let n = t.len();
        let mut dp = vec![0i64; n + 1];
        dp[0] = 1;
        for &ch in s {
            for j in (1..=n).rev() {
                if ch == t[j - 1] {
                    dp[j] += dp[j - 1];
                }
            }
        }
        dp[n] as i32
    }
}
