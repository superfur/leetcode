/**
 * 79. 单词搜索
 * 给定 m x n 二维字符网格 board 和字符串 word，
 * 判断 word 是否能由水平/垂直相邻的单元格字母按顺序构成（同一单元格不可复用）。
 * 回溯 DFS：原地用 '#' 标记走过位置，回溯时还原。
 */
function exist(board: string[][], word: string): boolean {
    const m = board.length;
    if (m === 0) return false;
    const n = board[0].length;

    const dfs = (i: number, j: number, k: number): boolean => {
        if (k === word.length) return true;
        if (i < 0 || i >= m || j < 0 || j >= n || board[i][j] !== word[k]) {
            return false;
        }
        const saved = board[i][j];
        board[i][j] = "#";
        const found = dfs(i + 1, j, k + 1) ||
                      dfs(i - 1, j, k + 1) ||
                      dfs(i, j + 1, k + 1) ||
                      dfs(i, j - 1, k + 1);
        board[i][j] = saved;
        return found;
    };

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (dfs(i, j, 0)) return true;
        }
    }
    return false;
}

export default exist;