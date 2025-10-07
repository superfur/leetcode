class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        数独求解器：使用回溯 + 位掩码算法
        - 用三个位掩码数组记录每行/列/宫已使用的数字
        - 空格按候选数最少优先排序，减少回溯分支
        - 逐格尝试可用数字，递归求解；失败则回溯
        """
        N = 9
        FULL_MASK = (1 << 9) - 1  # 0b1_1111_1111，对应数字1-9的可用位
        
        # 初始化位掩码数组和空位列表
        row_masks = [0] * N  # 第i行已使用数字的位掩码
        col_masks = [0] * N  # 第j列已使用数字的位掩码
        box_masks = [0] * N  # 第k宫已使用数字的位掩码
        empties = []         # 所有空格的位置坐标
        
        def get_box_index(r: int, c: int) -> int:
            """计算位置(r,c)所属的宫格索引"""
            return (r // 3) * 3 + (c // 3)
        
        # 预处理：统计已填数字到掩码中，收集空格
        for r in range(N):
            for c in range(N):
                ch = board[r][c]
                if ch == '.':
                    empties.append((r, c))
                    continue
                
                # 将字符'1'-'9'转换为位索引0-8
                digit = int(ch) - 1
                bit = 1 << digit
                row_masks[r] |= bit
                col_masks[c] |= bit
                box_masks[get_box_index(r, c)] |= bit
        
        def count_bits(x: int) -> int:
            """Kernighan算法：统计二进制中1的个数"""
            count = 0
            while x != 0:
                x &= (x - 1)  # 清除最低位的1
                count += 1
            return count
        
        # 启发式排序：空格按候选数（可用位数量）升序排序
        def get_candidate_count(r: int, c: int) -> int:
            """计算位置(r,c)的候选数字个数"""
            used = row_masks[r] | col_masks[c] | box_masks[get_box_index(r, c)]
            available = FULL_MASK & ~used
            return count_bits(available)
        
        empties.sort(key=lambda pos: get_candidate_count(pos[0], pos[1]))
        
        def dfs(idx: int) -> bool:
            """
            深度优先搜索回溯求解
            Args:
                idx: 当前处理的空格索引
            Returns:
                bool: 是否找到解
            """
            # 所有空格填完，找到解
            if idx == len(empties):
                return True
            
            r, c = empties[idx]
            box_idx = get_box_index(r, c)
            
            # 计算当前位置的可用数字位集合
            used = row_masks[r] | col_masks[c] | box_masks[box_idx]
            available = FULL_MASK & ~used  # 可用数字的位掩码
            
            # 尝试每个可用数字
            while available != 0:
                # 取最低位的1（选择一个候选数字）
                bit = available & (-available)  # 获取最低位1
                digit = bit.bit_length() - 1    # 转换为数字0-8
                ch = str(digit + 1)             # 转换为字符'1'-'9'
                
                # 放置该数字
                board[r][c] = ch
                row_masks[r] |= bit
                col_masks[c] |= bit
                box_masks[box_idx] |= bit
                
                # 递归求解下一个空格
                if dfs(idx + 1):
                    return True
                
                # 回溯：撤销放置
                board[r][c] = '.'
                row_masks[r] &= ~bit
                col_masks[c] &= ~bit
                box_masks[box_idx] &= ~bit
                
                # 移除当前候选，尝试下一个
                available &= (available - 1)
            
            # 所有候选都失败，回溯到上一层
            return False
        
        # 开始求解
        dfs(0)