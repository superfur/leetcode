public class Solution {
    /**
     * 91. 解码方法
     * 动态规划：dp[i] 表示 s.substring(0, i) 的解码方法数。
     * 单字符有效（非 '0'）时可从 dp[i-1] 转移；
     * 双字符在 10~26 之间时可从 dp[i-2] 转移。
     * 用两个变量滚动即可，无需数组。
     */
    public int numDecodings(String s) {
        int n = s.length();
        int prev2 = 1;
        int prev1 = s.charAt(0) != '0' ? 1 : 0;

        for (int i = 2; i <= n; i++) {
            int cur = 0;
            if (s.charAt(i - 1) != '0') {
                cur += prev1;
            }
            int twoDigit = (s.charAt(i - 2) - '0') * 10 + (s.charAt(i - 1) - '0');
            if (twoDigit >= 10 && twoDigit <= 26) {
                cur += prev2;
            }
            prev2 = prev1;
            prev1 = cur;
        }

        return prev1;
    }
}
