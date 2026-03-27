package com.leetcode;

import java.util.Arrays;

public class Solution {
    /**
     * 不同路径 II：m×n 网格中有障碍物(1表示)，从左上角到右下角的路径数。
     * DP 一维：dp[j] = 0(有障碍) 或 dp[j] + dp[j-1](无障碍)。时间 O(mn)，空间 O(n)。
     */
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if (obstacleGrid == null || obstacleGrid.length == 0 || obstacleGrid[0].length == 0) {
            return 0;
        }

        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        int[] dp = new int[n];
        Arrays.fill(dp, 0);

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (obstacleGrid[i][j] == 1) {
                    dp[j] = 0;
                } else if (j == 0) {
                    dp[j] = (i == 0 || dp[j] == 1) ? 1 : 0;
                } else {
                    dp[j] = dp[j] + dp[j - 1];
                }
            }
        }

        return dp[n - 1];
    }

    /** 兼容 Object... args 的入口 */
    public Object 不同路径Ii(Object... args) {
        int[][] grid = (int[][]) args[0];
        return uniquePathsWithObstacles(grid);
    }
}
