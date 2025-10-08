class Solution {
    // 数独求解器：使用回溯 + 位掩码算法
    // - 用三个位掩码数组记录每行/列/宫已使用的数字
    // - 空格按候选数最少优先排序，减少回溯分支
    // - 逐格尝试可用数字，递归求解；失败则回溯
    
    private static final int N = 9;
    private static final int FULL_MASK = (1 << 9) - 1; // 0b1_1111_1111
    
    private int[] rowMasks;    // 第i行已使用数字的位掩码
    private int[] colMasks;    // 第j列已使用数字的位掩码
    private int[] boxMasks;    // 第k宫已使用数字的位掩码
    private int[][] empties;   // 所有空格的位置坐标
    private int emptyCount;    // 空格数量
    
    public void solveSudoku(char[][] board) {
        rowMasks = new int[N];
        colMasks = new int[N];
        boxMasks = new int[N];
        empties = new int[81][2];  // 最多81个空格
        emptyCount = 0;
        
        // 预处理：统计已填数字到掩码中，收集空格
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                char ch = board[r][c];
                if (ch == '.') {
                    empties[emptyCount][0] = r;
                    empties[emptyCount][1] = c;
                    emptyCount++;
                    continue;
                }
                
                // 将字符'1'-'9'转换为位索引0-8
                int digit = ch - '1';
                int bit = 1 << digit;
                rowMasks[r] |= bit;
                colMasks[c] |= bit;
                boxMasks[getBoxIndex(r, c)] |= bit;
            }
        }
        
        // 启发式排序：空格按候选数（可用位数量）升序排序
        sortEmptiesByCandidate();
        
        // 开始回溯求解
        dfs(0, board);
    }
    
    /**
     * 计算位置(r,c)所属的宫格索引
     */
    private int getBoxIndex(int r, int c) {
        return (r / 3) * 3 + (c / 3);
    }
    
    /**
     * Kernighan算法：统计二进制中1的个数
     */
    private int countBits(int x) {
        int count = 0;
        while (x != 0) {
            x &= (x - 1);  // 清除最低位的1
            count++;
        }
        return count;
    }
    
    /**
     * 计算位置(r,c)的候选数字个数
     */
    private int getCandidateCount(int r, int c) {
        int used = rowMasks[r] | colMasks[c] | boxMasks[getBoxIndex(r, c)];
        int available = FULL_MASK & ~used;
        return countBits(available);
    }
    
    /**
     * 启发式排序：空格按候选数升序排序
     */
    private void sortEmptiesByCandidate() {
        // 使用插入排序（对于小规模数据效率高）
        for (int i = 1; i < emptyCount; i++) {
            int[] curr = empties[i];
            int currCount = getCandidateCount(curr[0], curr[1]);
            int j = i - 1;
            
            while (j >= 0 && getCandidateCount(empties[j][0], empties[j][1]) > currCount) {
                empties[j + 1] = empties[j];
                j--;
            }
            empties[j + 1] = curr;
        }
    }
    
    /**
     * 深度优先搜索回溯求解
     * @param idx 当前处理的空格索引
     * @param board 数独棋盘
     * @return 是否找到解
     */
    private boolean dfs(int idx, char[][] board) {
        // 所有空格填完，找到解
        if (idx == emptyCount) {
            return true;
        }
        
        int r = empties[idx][0];
        int c = empties[idx][1];
        int boxIdx = getBoxIndex(r, c);
        
        // 计算当前位置的可用数字位集合
        int used = rowMasks[r] | colMasks[c] | boxMasks[boxIdx];
        int available = FULL_MASK & ~used;  // 可用数字的位掩码
        
        // 尝试每个可用数字
        while (available != 0) {
            // 取最低位的1（选择一个候选数字）
            int bit = available & (-available);  // 获取最低位1
            int digit = Integer.numberOfTrailingZeros(bit);  // 转换为数字0-8
            char ch = (char) ('1' + digit);  // 转换为字符'1'-'9'
            
            // 放置该数字
            board[r][c] = ch;
            rowMasks[r] |= bit;
            colMasks[c] |= bit;
            boxMasks[boxIdx] |= bit;
            
            // 递归求解下一个空格
            if (dfs(idx + 1, board)) {
                return true;
            }
            
            // 回溯：撤销放置
            board[r][c] = '.';
            rowMasks[r] &= ~bit;
            colMasks[c] &= ~bit;
            boxMasks[boxIdx] &= ~bit;
            
            // 移除当前候选，尝试下一个
            available &= (available - 1);
        }
        
        // 所有候选都失败，回溯到上一层
        return false;
    }
}