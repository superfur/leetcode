class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 使用位运算来记录数字出现情况，每个数字对应一个位
        rows = [0] * 9    # 9行，每行用一个整数记录
        cols = [0] * 9    # 9列，每列用一个整数记录
        boxes = [0] * 9   # 9个宫格，每个宫格用一个整数记录
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                
                # 跳过空白格
                if num == '.':
                    continue
                
                # 将字符转换为数字(1-9)，并转换为对应的位索引(0-8)
                digit = int(num) - 1
                bit = 1 << digit  # 设置对应的位
                
                # 计算宫格索引
                box_idx = (i // 3) * 3 + (j // 3)
                
                # 检查是否已经存在：使用位运算检查
                if (rows[i] & bit) != 0 or (cols[j] & bit) != 0 or (boxes[box_idx] & bit) != 0:
                    return False
                
                # 设置对应的位
                rows[i] |= bit
                cols[j] |= bit
                boxes[box_idx] |= bit
        
        return True