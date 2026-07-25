public class Solution {
    /**
     * 79. 单词搜索
     * 回溯 DFS：枚举起点，四个方向递归搜索 word[k+1..]，
     * 走过一格后用 '#' 标记，回溯时还原，避免重复使用。
     */
    public boolean exist(char[][] board, String word) {
        int m = board.length;
        if (m == 0) return false;
        int n = board[0].length;

        return backtrack(board, word, m, n);
    }

    private boolean backtrack(char[][] board, String word, int m, int n) {
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dfs(board, word, i, j, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean dfs(char[][] board, String word, int i, int j, int k) {
        if (k == word.length()) {
            return true;
        }
        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length
                || board[i][j] != word.charAt(k)) {
            return false;
        }
        char saved = board[i][j];
        board[i][j] = '#';
        boolean found = dfs(board, word, i + 1, j, k + 1)
                || dfs(board, word, i - 1, j, k + 1)
                || dfs(board, word, i, j + 1, k + 1)
                || dfs(board, word, i, j - 1, k + 1);
        board[i][j] = saved;
        return found;
    }
}