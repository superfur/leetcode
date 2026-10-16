class Solution {
    /**
     * 131. 分割回文串
     * 先用区间 DP 预处理 isPal[i][j]（s[i..j] 是否回文），
     * 再回溯：从位置 start 开始，枚举每个能切出回文前缀 s[start..end] 的位置，
     * 选中后递归处理 end + 1，走到字符串末尾就收集一个方案。
     */
    public List<List<String>> partition(String s) {
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

        List<List<String>> res = new ArrayList<>();
        back(0, s, isPal, new ArrayList<>(), res);
        return res;
    }

    private void back(int start, String s, boolean[][] isPal, List<String> path, List<List<String>> res) {
        if (start == s.length()) {
            res.add(new ArrayList<>(path));
            return;
        }
        for (int end = start; end < s.length(); end++) {
            if (isPal[start][end]) {
                path.add(s.substring(start, end + 1));
                back(end + 1, s, isPal, path, res);
                path.remove(path.size() - 1);
            }
        }
    }
}
