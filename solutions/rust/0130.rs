impl Solution {
    /// 130. 被围绕的区域
    /// 反向思考：只有「和边界上的 O 连通」的 O 不会被捕获。
    /// 先从四条边上的 O 出发做洪泛（用显式栈，避免 200x200 时递归过深），
    /// 把它们临时标成 'A'；然后整盘扫一遍：剩下的 'O' 是被围绕的 → 'X'，'A' 还原成 'O'。
    pub fn solve(board: &mut Vec<Vec<char>>) {
        let m = board.len();
        let n = board[0].len();
        let mut stack: Vec<(usize, usize)> = Vec::new();

        for i in 0..m {
            for j in 0..n {
                if (i == 0 || i == m - 1 || j == 0 || j == n - 1) && board[i][j] == 'O' {
                    board[i][j] = 'A';
                    stack.push((i, j));
                }
            }
        }

        let dirs: [(i32, i32); 4] = [(1, 0), (-1, 0), (0, 1), (0, -1)];
        while let Some((x, y)) = stack.pop() {
            for (dx, dy) in dirs.iter() {
                let nx = x as i32 + dx;
                let ny = y as i32 + dy;
                if nx >= 0 && nx < m as i32 && ny >= 0 && ny < n as i32 {
                    let (nx, ny) = (nx as usize, ny as usize);
                    if board[nx][ny] == 'O' {
                        board[nx][ny] = 'A';
                        stack.push((nx, ny));
                    }
                }
            }
        }

        for row in board.iter_mut() {
            for cell in row.iter_mut() {
                if *cell == 'O' {
                    *cell = 'X';
                } else if *cell == 'A' {
                    *cell = 'O';
                }
            }
        }
    }
}
