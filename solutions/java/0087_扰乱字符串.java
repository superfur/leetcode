public class Solution {
    /**
     * 87. 扰乱字符串
     * 回溯枚举分割点 i：要么 s1[:i]/s1[i:] 与 s2[:i]/s2[i:] 同步扰乱，
     * 要么 s1[:i]/s1[i:] 与 s2[n-i:]/s2[:n-i]（交换）同步扰乱。
     * 剪枝：字符计数不等直接返回 false；用 HashMap<(s1,s2),Boolean> 记忆化。
     */
    public boolean isScramble(String s1, String s2) {
        java.util.Map<String, Boolean> memo = new java.util.HashMap<>();

        return dfs(s1, s2, memo);
    }

    private boolean dfs(String a, String b, java.util.Map<String, Boolean> memo) {
        String key = a + "#" + b;
        if (memo.containsKey(key)) return memo.get(key);
        if (a.equals(b)) {
            memo.put(key, true);
            return true;
        }
        // 字符计数剪枝
        int[] cnt = new int[26];
        for (int i = 0; i < a.length(); i++) {
            cnt[a.charAt(i) - 'a']++;
            cnt[b.charAt(i) - 'a']--;
        }
        for (int c : cnt) {
            if (c != 0) {
                memo.put(key, false);
                return false;
            }
        }
        int n = a.length();
        for (int i = 1; i < n; i++) {
            // 不交换
            if (dfs(a.substring(0, i), b.substring(0, i), memo)
                    && dfs(a.substring(i), b.substring(i), memo)) {
                memo.put(key, true);
                return true;
            }
            // 交换
            if (dfs(a.substring(0, i), b.substring(n - i), memo)
                    && dfs(a.substring(i), b.substring(0, n - i), memo)) {
                memo.put(key, true);
                return true;
            }
        }
        memo.put(key, false);
        return false;
    }
}