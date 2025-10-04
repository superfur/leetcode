impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        // 使用位运算来记录数字出现情况，每个数字对应一个位
        let mut rows = [0u16; 9];  // 9行，每行用一个16位整数记录
        let mut cols = [0u16; 9];  // 9列，每列用一个16位整数记录
        let mut boxes = [0u16; 9]; // 9个宫格，每个宫格用一个16位整数记录
        
        for i in 0..9 {
            for j in 0..9 {
                let num = board[i][j];
                
                // 跳过空白格
                if num == '.' {
                    continue;
                }
                
                // 将字符转换为数字(1-9)，并转换为对应的位索引(0-8)
                let digit = num as usize - '1' as usize;
                let bit = 1 << digit; // 设置对应的位
                
                // 计算宫格索引
                let box_idx = (i / 3) * 3 + (j / 3);
                
                // 检查是否已经存在：使用位运算检查
                if (rows[i] & bit) != 0 || (cols[j] & bit) != 0 || (boxes[box_idx] & bit) != 0 {
                    return false;
                }
                
                // 设置对应的位
                rows[i] |= bit;
                cols[j] |= bit;
                boxes[box_idx] |= bit;
            }
        }
        
        true
    }
}