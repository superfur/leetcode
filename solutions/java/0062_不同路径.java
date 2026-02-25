import java.util.Arrays;

public class Solution {
    /**
     * 不同路径：m×n 网格，从左上角只能向右或向下走，到右下角的路径数。
     * DP 一维：dp[j] 表示到达当前行第 j 列的路径数，dp[j] += dp[j-1]。
     * 时间 O(mn)，空间 O(n)。
     */
    public int uniquePaths(int m, int n) {
        int[] dp = new int[n];
        Arrays.fill(dp, 1);

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[j] += dp[j - 1];
            }
        }
        return dp[n - 1];
    }

    /** 兼容 Object... args 的入口 */
    public Object 不同路径(Object... args) {
        int m = (int) args[0];
        int n = (int) args[1];
        return uniquePaths(m, n);
    }
}
