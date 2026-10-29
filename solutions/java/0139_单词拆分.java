class Solution {
    /**
     * 139. 单词拆分
     * dp[i] 表示 s 的前 i 个字符能否被拆成字典里的单词（dp[0] = true）。
     * 对每个 i 枚举「最后一个单词」的起点 j：dp[j] 为真且 s.substring(j, i) 在字典里，则 dp[i] 为真。
     * 字典里最长的单词长度为 maxLen，所以 j 只需要从 i - maxLen 开始往后枚举，
     * 用 HashSet 判断单词是否存在。时间 O(n * maxLen * maxLen)。
     */
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> words = new HashSet<>(wordDict);
        int maxLen = 0;
        for (String w : words) {
            maxLen = Math.max(maxLen, w.length());
        }

        int n = s.length();
        boolean[] dp = new boolean[n + 1];
        dp[0] = true;
        for (int i = 1; i <= n; i++) {
            for (int j = Math.max(0, i - maxLen); j < i; j++) {
                if (dp[j] && words.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[n];
    }
}
