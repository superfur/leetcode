class Solution {
    public String longestPalindrome(String s) {
        if (s.length() <= 1) {
            return s;
        }
        
        int maxLen = 1;
        int begin = 0;
        
        // 创建二维动态规划数组
        boolean[][] dp = new boolean[s.length()][s.length()];
        
        // 单个字符都是回文
        for (int i = 0; i < s.length(); i++) {
            dp[i][i] = true;
        }
        
        // 动态规划填充
        for (int j = 1; j < s.length(); j++) {
            for (int i = 0; i < j; i++) {
                if (s.charAt(i) != s.charAt(j)) {
                    dp[i][j] = false;
                } else {
                    if (j - i < 3) {
                        dp[i][j] = true;
                    } else {
                        dp[i][j] = dp[i + 1][j - 1];
                    }
                    
                    if (dp[i][j] && j - i + 1 > maxLen) {
                        maxLen = j - i + 1;
                        begin = i;
                    }
                }
            }
        }
        
        return s.substring(begin, begin + maxLen);
    }
}