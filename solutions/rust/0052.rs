impl Solution {
    /*
     * N 皇后问题 II - 返回不同解决方案的数量
     * 
     * 时间复杂度: O(n!)
     *   - 最坏情况下需要尝试所有可能的排列组合
     *   - 但由于剪枝优化，实际运行时间远小于 O(n!)
     * 空间复杂度: O(n)
     *   - 递归调用栈深度为 O(n)
     * 
     * 思路:
     * 1. 使用回溯算法，逐行放置皇后
     * 2. 使用位运算优化冲突检查：
     *    - cols: 列占用情况（第 j 列被占用，则第 j 位为 1）
     *    - diag1: 主对角线占用情况（row - col + n - 1 映射到位号）
     *    - diag2: 副对角线占用情况（row + col 映射到位号）
     * 3. 当所有行都放置了皇后，计数加一
     * 
     * 优化:
     * - 使用位运算代替 HashSet，大幅提升性能
     * - 位运算检查冲突的时间复杂度为 O(1)
     */
    pub fn total_n_queens(n: i32) -> i32 {
        let mut count = 0;
        let n_usize = n as usize;
        
        /*
         * 回溯函数
         * 
         * 参数:
         * - row: 当前要放置皇后的行号
         * - cols: 已被占用的列集合（第 j 列占用，则第 j 位为 1）
         * - diag1: 主对角线集合（row - col 固定，用 (row - col + n - 1) 映射到 [0, 2n-2]）
         * - diag2: 副对角线集合（row + col 固定，直接用 row + col 映射到 [0, 2n-2]）
         */
        fn backtrack(
            n: usize,
            row: usize,
            cols: u32,
            diag1: u32,
            diag2: u32,
            count: &mut i32,
        ) {
            // 所有行都已放置皇后，找到一个有效解
            if row == n {
                *count += 1;
                return;
            }
            
            // 尝试在当前行的每一列放置皇后
            for col in 0..n {
                let d1 = row as i32 - col as i32 + n as i32 - 1;
                let d2 = row + col;
                
                let col_bit = 1u32 << col;
                let d1_bit = 1u32 << d1;
                let d2_bit = 1u32 << d2;
                
                // 检查是否有冲突
                if (cols & col_bit) != 0 {
                    continue;
                }
                if (diag1 & d1_bit) != 0 {
                    continue;
                }
                if (diag2 & d2_bit) != 0 {
                    continue;
                }
                
                // 递归处理下一行
                backtrack(
                    n,
                    row + 1,
                    cols | col_bit,
                    diag1 | d1_bit,
                    diag2 | d2_bit,
                    count,
                );
            }
        }
        
        backtrack(n_usize, 0, 0, 0, 0, &mut count);
        count
    }
}