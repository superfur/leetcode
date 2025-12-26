class Solution {
    /**
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
     * - 使用位运算代替 Set，大幅提升性能
     * - 位运算检查冲突的时间复杂度为 O(1)
     * 
     * 示例:
     * n = 4 时，返回 2
     */
    public int totalNQueens(int n) {
        int[] count = new int[1]; // 使用数组来在嵌套方法中修改计数
        
        /**
         * 回溯函数
         * @param row 当前要放置皇后的行号
         * @param cols 已被占用的列集合（第 j 列占用，则第 j 位为 1）
         * @param diag1 主对角线集合（row - col 固定，用 (row - col + n - 1) 映射到 [0, 2n-2]）
         * @param diag2 副对角线集合（row + col 固定，直接用 row + col 映射到 [0, 2n-2]）
         */
        backtrack(n, 0, 0, 0, 0, count);
        
        return count[0];
    }
    
    private void backtrack(int n, int row, int cols, int diag1, int diag2, int[] count) {
        // 所有行都已放置皇后，找到一个有效解
        if (row == n) {
            count[0]++;
            return;
        }
        
        // 尝试在当前行的每一列放置皇后
        for (int col = 0; col < n; col++) {
            int d1 = row - col + n - 1;
            int d2 = row + col;
            
            int colBit = 1 << col;
            int d1Bit = 1 << d1;
            int d2Bit = 1 << d2;
            
            // 检查是否有冲突
            if ((cols & colBit) != 0) {
                continue;
            }
            if ((diag1 & d1Bit) != 0) {
                continue;
            }
            if ((diag2 & d2Bit) != 0) {
                continue;
            }
            
            // 递归处理下一行
            backtrack(n, row + 1, cols | colBit, diag1 | d1Bit, diag2 | d2Bit, count);
        }
    }
}