impl Solution {
    /// 120. 三角形最小路径和
    /// 自底向上一维滚动 DP：dp[j] 表示从当前行第 j 个位置走到底部的最小路径和。
    /// 从倒数第二行开始，dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
    /// （dp[j] 是正下方，dp[j+1] 是右下方，取较小的再加上当前值），
    /// 一路滚动到第 0 行，dp[0] 就是答案。
    pub fn minimum_total(triangle: Vec<Vec<i32>>) -> i32 {
        let n = triangle.len();
        let mut dp = triangle[n - 1].clone();
        for i in (0..n - 1).rev() {
            for j in 0..triangle[i].len() {
                dp[j] = triangle[i][j] + dp[j].min(dp[j + 1]);
            }
        }
        dp[0]
    }
}
