/**
 * N 皇后问题 - 回溯算法
 * 
 * 时间复杂度: O(n!)
 *   - 最坏情况下需要尝试所有可能的排列组合
 *   - 但由于剪枝优化，实际运行时间远小于 O(n!)
 * 空间复杂度: O(n)
 *   - 递归调用栈深度为 O(n)
 *   - 使用数组存储每行皇后的列位置，空间为 O(n)
 * 
 * 思路:
 * 1. 使用回溯算法，逐行放置皇后
 * 2. 使用数组 queens[i] 记录第 i 行皇后所在的列位置
 * 3. 检查冲突：
 *    - 列冲突：检查当前列是否已被占用
 *    - 主对角线冲突：行号 - 列号 = 常数（左上到右下）
 *    - 副对角线冲突：行号 + 列号 = 常数（右上到左下）
 * 4. 当所有行都放置了皇后，将结果转换为字符串列表格式
 * 
 * 优化:
 * - 使用三个 Set 来快速检查列和两个对角线的冲突
 * - 避免每次检查时遍历已放置的皇后
 * 
 * 示例:
 * n = 4 时，输出:
 * [[".Q..","...Q","Q...","..Q."], ["..Q.","Q...","...Q",".Q.."]]
 */
function solveNQueens(n: number): string[][] {
    const result: string[][] = [];
    // queens[i] 表示第 i 行皇后所在的列位置
    const queens: number[] = new Array(n).fill(-1);
    // 使用 Set 快速检查列冲突
    const columns = new Set<number>();
    // 使用 Set 快速检查主对角线冲突（行号 - 列号 = 常数）
    const diagonals1 = new Set<number>();
    // 使用 Set 快速检查副对角线冲突（行号 + 列号 = 常数）
    const diagonals2 = new Set<number>();
    
    // 从第 0 行开始回溯
    backtrack(result, queens, n, 0, columns, diagonals1, diagonals2);
    
    return result;
}

/**
 * 回溯函数
 * 
 * @param result 结果列表
 * @param queens 记录每行皇后所在的列位置
 * @param n 棋盘大小
 * @param row 当前处理的行
 * @param columns 已占用的列集合
 * @param diagonals1 已占用的主对角线集合（行号 - 列号）
 * @param diagonals2 已占用的副对角线集合（行号 + 列号）
 */
function backtrack(
    result: string[][],
    queens: number[],
    n: number,
    row: number,
    columns: Set<number>,
    diagonals1: Set<number>,
    diagonals2: Set<number>
): void {
    // 所有行都已放置皇后，找到一个有效解
    if (row === n) {
        result.push(buildBoard(queens, n));
        return;
    }
    
    // 尝试在当前行的每一列放置皇后
    for (let col = 0; col < n; col++) {
        // 计算主对角线和副对角线的标识
        const diagonal1 = row - col;
        const diagonal2 = row + col;
        
        // 检查是否有冲突
        if (columns.has(col) || diagonals1.has(diagonal1) || diagonals2.has(diagonal2)) {
            continue; // 有冲突，跳过
        }
        
        // 放置皇后
        queens[row] = col;
        columns.add(col);
        diagonals1.add(diagonal1);
        diagonals2.add(diagonal2);
        
        // 递归处理下一行
        backtrack(result, queens, n, row + 1, columns, diagonals1, diagonals2);
        
        // 回溯：撤销当前选择
        columns.delete(col);
        diagonals1.delete(diagonal1);
        diagonals2.delete(diagonal2);
    }
}

/**
 * 根据 queens 数组构建棋盘字符串列表
 * 
 * @param queens 每行皇后所在的列位置
 * @param n 棋盘大小
 * @returns 棋盘字符串列表
 */
function buildBoard(queens: number[], n: number): string[] {
    const board: string[] = [];
    for (let i = 0; i < n; i++) {
        const row = new Array(n).fill('.');
        row[queens[i]] = 'Q';
        board.push(row.join(''));
    }
    return board;
}