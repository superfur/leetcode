from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        79. 单词搜索
        回溯 DFS：枚举起点，四个方向递归搜索 word[k+1..]，
        走过一格后用占位符标记，回溯时还原，避免重复使用。
        """
        if not board or not board[0] or not word:
            return False
        m, n = len(board), len(board[0])

        def dfs(i: int, j: int, k: int) -> bool:
            if k == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            saved = board[i][j]
            board[i][j] = "#"
            found = (dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or
                     dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1))
            board[i][j] = saved
            return found

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


if __name__ == "__main__":
    test_cases = [
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED", True),
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE", True),
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB", False),
        ([["A"]], "A", True),
        ([["a", "b"], ["c", "d"]], "abcd", False),
    ]
    solution = Solution()
    for i, (board, word, expected) in enumerate(test_cases, 1):
        # 深拷贝以隔离每次调用对 board 的原地修改
        result = solution.exist([row[:] for row in board], word)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (word={word!r}, got={result}, expected={expected})")