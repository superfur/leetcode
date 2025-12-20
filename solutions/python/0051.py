class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        N 皇后问题 - 回溯算法
        
        时间复杂度: O(n!)
          - 最坏情况下需要尝试所有可能的排列组合
          - 但由于剪枝优化，实际运行时间远小于 O(n!)
        空间复杂度: O(n)
          - 递归调用栈深度为 O(n)
          - 使用列表存储每行皇后的列位置，空间为 O(n)
        
        思路:
        1. 使用回溯算法，逐行放置皇后
        2. 使用列表 queens[i] 记录第 i 行皇后所在的列位置
        3. 检查冲突：
           - 列冲突：检查当前列是否已被占用
           - 主对角线冲突：行号 - 列号 = 常数（左上到右下）
           - 副对角线冲突：行号 + 列号 = 常数（右上到左下）
        4. 当所有行都放置了皇后，将结果转换为字符串列表格式
        
        优化:
        - 使用三个 Set 来快速检查列和两个对角线的冲突
        - 避免每次检查时遍历已放置的皇后
        
        示例:
        n = 4 时，输出:
        [[".Q..","...Q","Q...","..Q."], ["..Q.","Q...","...Q",".Q.."]]
        """
        result = []
        # queens[i] 表示第 i 行皇后所在的列位置
        queens = [-1] * n
        # 使用 Set 快速检查列冲突
        columns = set()
        # 使用 Set 快速检查主对角线冲突（行号 - 列号 = 常数）
        diagonals1 = set()
        # 使用 Set 快速检查副对角线冲突（行号 + 列号 = 常数）
        diagonals2 = set()
        
        # 从第 0 行开始回溯
        self._backtrack(result, queens, n, 0, columns, diagonals1, diagonals2)
        
        return result
    
    def _backtrack(self, result: List[List[str]], queens: List[int], n: int, 
                   row: int, columns: set, diagonals1: set, diagonals2: set) -> None:
        """
        回溯函数
        
        Args:
            result: 结果列表
            queens: 记录每行皇后所在的列位置
            n: 棋盘大小
            row: 当前处理的行
            columns: 已占用的列集合
            diagonals1: 已占用的主对角线集合（行号 - 列号）
            diagonals2: 已占用的副对角线集合（行号 + 列号）
        """
        # 所有行都已放置皇后，找到一个有效解
        if row == n:
            result.append(self._build_board(queens, n))
            return
        
        # 尝试在当前行的每一列放置皇后
        for col in range(n):
            # 计算主对角线和副对角线的标识
            diagonal1 = row - col
            diagonal2 = row + col
            
            # 检查是否有冲突
            if col in columns or diagonal1 in diagonals1 or diagonal2 in diagonals2:
                continue  # 有冲突，跳过
            
            # 放置皇后
            queens[row] = col
            columns.add(col)
            diagonals1.add(diagonal1)
            diagonals2.add(diagonal2)
            
            # 递归处理下一行
            self._backtrack(result, queens, n, row + 1, columns, diagonals1, diagonals2)
            
            # 回溯：撤销当前选择
            columns.remove(col)
            diagonals1.remove(diagonal1)
            diagonals2.remove(diagonal2)
    
    def _build_board(self, queens: List[int], n: int) -> List[str]:
        """
        根据 queens 列表构建棋盘字符串列表
        
        Args:
            queens: 每行皇后所在的列位置
            n: 棋盘大小
        
        Returns:
            棋盘字符串列表
        """
        board = []
        for i in range(n):
            row = ['.'] * n
            row[queens[i]] = 'Q'
            board.append(''.join(row))
        return board