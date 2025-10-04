class Solution {
    public boolean isValidSudoku(char[][] board) {
        // 使用位运算来记录数字出现情况，每个数字对应一个位
        int[] rows = new int[9];    // 9行，每行用一个整数记录
        int[] cols = new int[9];    // 9列，每列用一个整数记录
        int[] boxes = new int[9];   // 9个宫格，每个宫格用一个整数记录
        
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char num = board[i][j];
                
                // 跳过空白格
                if (num == '.') {
                    continue;
                }
                
                // 将字符转换为数字(1-9)，并转换为对应的位索引(0-8)
                int digit = num - '1';  // '1' -> 0, '2' -> 1, ...
                int bit = 1 << digit;   // 设置对应的位
                
                // 计算宫格索引
                int boxIdx = (i / 3) * 3 + (j / 3);
                
                // 检查是否已经存在：使用位运算检查
                if ((rows[i] & bit) != 0 || (cols[j] & bit) != 0 || (boxes[boxIdx] & bit) != 0) {
                    return false;
                }
                
                // 设置对应的位
                rows[i] |= bit;
                cols[j] |= bit;
                boxes[boxIdx] |= bit;
            }
        }
        
        return true;
    }
}