/*
 * 不同路径 II（LeetCode 63）
 * m×n 网格中有障碍物(1表示)，从左上角到右下角的路径数。
 * DP 一维：dp[j] = 0(有障碍) 或 dp[j] + dp[j-1](无障碍)。时间 O(mn)，空间 O(n)。
 */
impl Solution {
    pub fn unique_paths_with_obstacles(obstacle_grid: Vec<Vec<i32>>) -> i32 {
        if obstacle_grid.is_empty() || obstacle_grid[0].is_empty() {
            return 0;
        }

        let m = obstacle_grid.len();
        let n = obstacle_grid[0].len();
        let mut dp = vec![0; n];

        for i in 0..m {
            for j in 0..n {
                if obstacle_grid[i][j] == 1 {
                    dp[j] = 0;
                } else if j == 0 {
                    dp[j] = if i == 0 || dp[j] == 1 { 1 } else { 0 };
                } else {
                    dp[j] = dp[j] + dp[j - 1];
                }
            }
        }

        dp[n - 1]
    }
}
