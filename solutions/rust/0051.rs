use std::collections::HashSet;

impl Solution {
    /*
     * N 皇后问题 - 回溯算法
     * 
     * 时间复杂度: O(n!)
     *   - 最坏情况下需要尝试所有可能的排列组合
     *   - 但由于剪枝优化，实际运行时间远小于 O(n!)
     * 空间复杂度: O(n)
     *   - 递归调用栈深度为 O(n)
     *   - 使用 Vec 存储每行皇后的列位置，空间为 O(n)
     * 
     * 思路:
     * 1. 使用回溯算法，逐行放置皇后
     * 2. 使用 Vec queens[i] 记录第 i 行皇后所在的列位置
     * 3. 检查冲突：
     *    - 列冲突：检查当前列是否已被占用
     *    - 主对角线冲突：行号 - 列号 = 常数（左上到右下）
     *    - 副对角线冲突：行号 + 列号 = 常数（右上到左下）
     * 4. 当所有行都放置了皇后，将结果转换为字符串列表格式
     * 
     * 优化:
     * - 使用三个 HashSet 来快速检查列和两个对角线的冲突
     * - 避免每次检查时遍历已放置的皇后
     * 
     * 示例:
     * n = 4 时，输出:
     * [[".Q..","...Q","Q...","..Q."], ["..Q.","Q...","...Q",".Q.."]]
     */
    pub fn solve_n_queens(n: i32) -> Vec<Vec<String>> {
        let mut result = Vec::new();
        // queens[i] 表示第 i 行皇后所在的列位置
        let mut queens = vec![-1; n as usize];
        // 使用 HashSet 快速检查列冲突
        let mut columns = HashSet::new();
        // 使用 HashSet 快速检查主对角线冲突（行号 - 列号 = 常数）
        let mut diagonals1 = HashSet::new();
        // 使用 HashSet 快速检查副对角线冲突（行号 + 列号 = 常数）
        let mut diagonals2 = HashSet::new();
        
        // 从第 0 行开始回溯
        Self::backtrack(
            &mut result,
            &mut queens,
            n as usize,
            0,
            &mut columns,
            &mut diagonals1,
            &mut diagonals2,
        );
        
        result
    }
    
    /*
     * 回溯函数
     * 
     * 参数:
     * - result: 结果列表
     * - queens: 记录每行皇后所在的列位置
     * - n: 棋盘大小
     * - row: 当前处理的行
     * - columns: 已占用的列集合
     * - diagonals1: 已占用的主对角线集合（行号 - 列号）
     * - diagonals2: 已占用的副对角线集合（行号 + 列号）
     */
    fn backtrack(
        result: &mut Vec<Vec<String>>,
        queens: &mut Vec<i32>,
        n: usize,
        row: usize,
        columns: &mut HashSet<i32>,
        diagonals1: &mut HashSet<i32>,
        diagonals2: &mut HashSet<i32>,
    ) {
        // 所有行都已放置皇后，找到一个有效解
        if row == n {
            result.push(Self::build_board(queens, n));
            return;
        }
        
        // 尝试在当前行的每一列放置皇后
        for col in 0..n {
            let col_i32 = col as i32;
            let row_i32 = row as i32;
            
            // 计算主对角线和副对角线的标识
            let diagonal1 = row_i32 - col_i32;
            let diagonal2 = row_i32 + col_i32;
            
            // 检查是否有冲突
            if columns.contains(&col_i32)
                || diagonals1.contains(&diagonal1)
                || diagonals2.contains(&diagonal2)
            {
                continue; // 有冲突，跳过
            }
            
            // 放置皇后
            queens[row] = col_i32;
            columns.insert(col_i32);
            diagonals1.insert(diagonal1);
            diagonals2.insert(diagonal2);
            
            // 递归处理下一行
            Self::backtrack(
                result, queens, n, row + 1, columns, diagonals1, diagonals2,
            );
            
            // 回溯：撤销当前选择
            columns.remove(&col_i32);
            diagonals1.remove(&diagonal1);
            diagonals2.remove(&diagonal2);
        }
    }
    
    /*
     * 根据 queens 数组构建棋盘字符串列表
     * 
     * 参数:
     * - queens: 每行皇后所在的列位置
     * - n: 棋盘大小
     * 
     * 返回:
     * - 棋盘字符串列表
     */
    fn build_board(queens: &[i32], n: usize) -> Vec<String> {
        let mut board = Vec::with_capacity(n);
        for i in 0..n {
            let mut row = vec!['.'; n];
            row[queens[i] as usize] = 'Q';
            board.push(row.iter().collect());
        }
        board
    }
}