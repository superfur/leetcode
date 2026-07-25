/// 79. 单词搜索
/// 回溯 DFS：枚举起点，四个方向递归搜索 word[k+1..]，
/// 走过一格后用 '\0' 标记，回溯时还原，避免重复使用。
/// 注意：调用站点不做边界守卫，统一交给 dfs 内部处理，
/// 这样当 k == word.len() 时即使递归到越界位置也能正确返回 true。
pub fn exist(board: Vec<Vec<char>>, word: String) -> bool {
    let m = board.len();
    if m == 0 {
        return false;
    }
    let n = board[0].len();
    let word_chars: Vec<char> = word.chars().collect();

    fn dfs(
        i: i32,
        j: i32,
        k: usize,
        m: usize,
        n: usize,
        board: &mut Vec<Vec<char>>,
        word: &[char],
    ) -> bool {
        if k == word.len() {
            return true;
        }
        if i < 0 || j < 0 || (i as usize) >= m || (j as usize) >= n {
            return false;
        }
        let iu = i as usize;
        let ju = j as usize;
        if board[iu][ju] != word[k] {
            return false;
        }
        let saved = board[iu][ju];
        board[iu][ju] = '\0';
        let found = dfs(i - 1, j, k + 1, m, n, board, word)
            || dfs(i + 1, j, k + 1, m, n, board, word)
            || dfs(i, j - 1, k + 1, m, n, board, word)
            || dfs(i, j + 1, k + 1, m, n, board, word);
        board[iu][ju] = saved;
        found
    }

    for i in 0..m as i32 {
        for j in 0..n as i32 {
            let mut board_copy = board.clone();
            if dfs(i, j, 0, m, n, &mut board_copy, &word_chars) {
                return true;
            }
        }
    }
    false
}

impl Solution {
    pub fn exist(board: Vec<Vec<char>>, word: String) -> bool {
        exist(board, word)
    }
}