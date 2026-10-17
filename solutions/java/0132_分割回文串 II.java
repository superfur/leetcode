class Solution {
    /**
     * 132. 分割回文串 II
     * 先用区间 DP 预处理 isPal[i][j]（s[i..j] 是否回文）；
     * 再令 dp[i] 为 s[0..i] 的最少分割次数：
     * 若 s[0..i] 本身是回文则为 0，否则枚举最后一段回文 s[j+1..i]，取 dp[j] + 1 的最小值。
     * 时间 O(n^2)。
     */
    public int minCut(String s) {
        int n = s.length();
        boolean[][] isPal = new boolean[n][n];
        for (boolean[] row : isPal) {
            Arrays.fill(row, true);
        }
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i + 1; j < n; j++) {
                isPal[i][j] = s.charAt(i) == s.charAt(j) && isPal[i + 1][j - 1];
            }
        }

        int[] dp = new int[n];
        for (int i = 0; i < n; i++) {
            if (isPal[0][i]) {
                dp[i] = 0;
                continue;
            }
            int best = i;
            for (int j = 0; j < i; j++) {
                if (isPal[j + 1][i] && dp[j] + 1 < best) {
                    best = dp[j] + 1;
                }
            }
            dp[i] = best;
        }
        return dp[n - 1];
    }
}
