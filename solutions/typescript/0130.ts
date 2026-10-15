/**
 Do not return anything, modify board in-place instead.

 130. 被围绕的区域
 反向思考：只有「和边界上的 O 连通」的 O 不会被捕获。
 先从四条边上的 O 出发做洪泛（用显式栈，避免 200x200 时递归爆栈），
 把它们临时标成 'A'；然后整盘扫一遍：剩下的 'O' 是被围绕的 → 'X'，'A' 还原成 'O'。
 */
function solve(board: string[][]): void {
    const m = board.length;
    const n = board[0].length;
    const stack: [number, number][] = [];

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if ((i === 0 || i === m - 1 || j === 0 || j === n - 1) && board[i][j] === 'O') {
                board[i][j] = 'A';
                stack.push([i, j]);
            }
        }
    }

    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    while (stack.length > 0) {
        const [x, y] = stack.pop()!;
        for (const [dx, dy] of dirs) {
            const nx = x + dx;
            const ny = y + dy;
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && board[nx][ny] === 'O') {
                board[nx][ny] = 'A';
                stack.push([nx, ny]);
            }
        }
    }

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (board[i][j] === 'O') board[i][j] = 'X';
            else if (board[i][j] === 'A') board[i][j] = 'O';
        }
    }
}

export default solve;
