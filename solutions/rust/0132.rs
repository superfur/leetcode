impl Solution {
    /// 132. 分割回文串 II
    /// 先用区间 DP 预处理 is_pal[i][j]（s[i..j] 是否回文）；
    /// 再令 dp[i] 为 s[0..i] 的最少分割次数：
    /// 若 s[0..i] 本身是回文则为 0，否则枚举最后一段回文 s[j+1..i]，取 dp[j] + 1 的最小值。
    /// 时间 O(n^2)。
    pub fn min_cut(s: String) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut is_pal = vec![vec![true; n]; n];
        for i in (0..n).rev() {
            for j in (i + 1)..n {
                is_pal[i][j] = bytes[i] == bytes[j] && (j - i < 2 || is_pal[i + 1][j - 1]);
            }
        }

        let mut dp = vec![0i32; n];
        for i in 0..n {
            if is_pal[0][i] {
                dp[i] = 0;
                continue;
            }
            let mut best = i as i32;
            for j in 0..i {
                if is_pal[j + 1][i] && dp[j] + 1 < best {
                    best = dp[j] + 1;
                }
            }
            dp[i] = best;
        }
        dp[n - 1]
    }
}
