class Solution {
    public boolean isMatch(String s, String p) {
        int i = 0, j = 0;
        int starIdx = -1;
        int match = 0;
        int m = s.length();
        int n = p.length();

        while (i < m) {
            if (j < n && (p.charAt(j) == s.charAt(i) || p.charAt(j) == '?')) {
                i++;
                j++;
            } else if (j < n && p.charAt(j) == '*') {
                starIdx = j;
                match = i;
                j++;
            } else if (starIdx != -1) {
                j = starIdx + 1;
                match++;
                i = match;
            } else {
                return false;
            }
        }

        while (j < n && p.charAt(j) == '*') {
            j++;
        }

        return j == n;
    }
}