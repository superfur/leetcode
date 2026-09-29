class Solution {
    /**
     * 120. 三角形最小路径和
     * 自底向上一维滚动 DP：dp[j] 表示从当前行第 j 个位置走到底部的最小路径和。
     * 从倒数第二行开始，dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
     * （dp[j] 是正下方，dp[j+1] 是右下方，取较小的再加上当前值），
     * 一路滚动到第 0 行，dp[0] 就是答案。
     */
    public int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.size();
        int[] dp = new int[n];
        List<Integer> last = triangle.get(n - 1);
        for (int j = 0; j < n; j++) {
            dp[j] = last.get(j);
        }
        for (int i = n - 2; i >= 0; i--) {
            List<Integer> row = triangle.get(i);
            for (int j = 0; j < row.size(); j++) {
                dp[j] = row.get(j) + Math.min(dp[j], dp[j + 1]);
            }
        }
        return dp[0];
    }
}
