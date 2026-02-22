/*
 * 不同路径（LeetCode 62）
 * m×n 网格，从左上角只能向右或向下走，到右下角的路径数。
 * DP 一维：dp[j] += dp[j-1]。时间 O(mn)，空间 O(n)。
 */
impl Solution {
    pub fn unique_paths(m: i32, n: i32) -> i32 {
        let (m, n) = (m as usize, n as usize);
        let mut dp = vec![1i32; n];

        for _ in 1..m {
            for j in 1..n {
                dp[j] += dp[j - 1];
            }
        }

        dp[n - 1]
    }
}
