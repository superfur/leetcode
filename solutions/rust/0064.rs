/*
 * 最小路径和（LeetCode 64）
 * m×n 网格，从左上角只能向右或向下走，到右下角的最小路径和。
 * DP 一维：dp[j] = min(dp[j], dp[j-1]) + grid[i][j]。时间 O(mn)，空间 O(n)。
 */
impl Solution {
    pub fn min_path_sum(grid: Vec<Vec<i32>>) -> i32 {
        if grid.is_empty() || grid[0].is_empty() {
            return 0;
        }
        let m = grid.len();
        let n = grid[0].len();
        let mut dp = vec![0; n];
        dp[0] = grid[0][0];
        for j in 1..n {
            dp[j] = dp[j - 1] + grid[0][j];
        }
        for i in 1..m {
            dp[0] += grid[i][0];
            for j in 1..n {
                dp[j] = dp[j].min(dp[j - 1]) + grid[i][j];
            }
        }
        dp[n - 1]
    }

    pub fn 最小路径和(nums: Vec<i32>, target: i32) -> Vec<i32> {
        // 占位实现（根据实际需要调整参数）
        vec![]
    }
}