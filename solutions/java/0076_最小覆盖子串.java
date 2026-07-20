public class Solution {
    /**
     * 76. 最小覆盖子串
     * 滑动窗口 + 频率计数，时间复杂度 O(m+n)
     */
    public String minWindow(String s, String t) {
        if (s == null || t == null || s.isEmpty() || t.isEmpty()) {
            return "";
        }

        int[] need = new int[128];
        for (int i = 0; i < t.length(); i++) {
            need[t.charAt(i)]++;
        }
        int required = 0;
        for (int v : need) {
            if (v > 0) {
                required++;
            }
        }

        int formed = 0;
        int left = 0;
        int bestLeft = 0;
        int bestLength = Integer.MAX_VALUE;
        int[] window = new int[128];

        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            window[c]++;
            if (need[c] > 0 && window[c] == need[c]) {
                formed++;
            }

            while (formed == required && left <= right) {
                int currentLength = right - left + 1;
                if (currentLength < bestLength) {
                    bestLength = currentLength;
                    bestLeft = left;
                }

                char leftChar = s.charAt(left);
                window[leftChar]--;
                if (need[leftChar] > 0 && window[leftChar] < need[leftChar]) {
                    formed--;
                }
                left++;
            }
        }

        return bestLength == Integer.MAX_VALUE ? "" : s.substring(bestLeft, bestLeft + bestLength);
    }
}