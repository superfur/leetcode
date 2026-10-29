class Solution {
    /**
     * 140. 单词拆分 II
     * 记忆化回溯：dfs(start) 返回后缀 s[start..] 的所有拆分句子。
     * 枚举第一个单词 s.substring(start, end)（长度不超过字典最长单词），在字典里就把它拼到 dfs(end) 的每个句子前面；
     * start == n 时返回 [""]，表示「恰好拆完」，拼接时据此决定要不要加空格。
     * 按起点缓存结果，相同的后缀不会被重复展开。
     */
    public List<String> wordBreak(String s, List<String> wordDict) {
        Set<String> words = new HashSet<>(wordDict);
        int maxLen = 0;
        for (String w : words) {
            maxLen = Math.max(maxLen, w.length());
        }
        return dfs(0, s, words, maxLen, new HashMap<>());
    }

    private List<String> dfs(int start, String s, Set<String> words, int maxLen, Map<Integer, List<String>> memo) {
        int n = s.length();
        if (start == n) {
            List<String> base = new ArrayList<>();
            base.add("");
            return base;
        }
        if (memo.containsKey(start)) {
            return memo.get(start);
        }

        List<String> res = new ArrayList<>();
        for (int end = start + 1; end <= Math.min(n, start + maxLen); end++) {
            String word = s.substring(start, end);
            if (words.contains(word)) {
                for (String tail : dfs(end, s, words, maxLen, memo)) {
                    res.add(tail.isEmpty() ? word : word + " " + tail);
                }
            }
        }
        memo.put(start, res);
        return res;
    }
}
