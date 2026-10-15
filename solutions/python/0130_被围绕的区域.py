from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        130. 被围绕的区域
        反向思考：只有「和边界上的 O 连通」的 O 不会被捕获。
        先从四条边上的 O 出发做洪泛（用显式栈，避免 200x200 时递归爆栈），
        把它们临时标成 'A'；然后整盘扫一遍：剩下的 'O' 是被围绕的 → 'X'，'A' 还原成 'O'。
        """
        m, n = len(board), len(board[0])
        stack = []
        for i in range(m):
            for j in range(n):
                if (i in (0, m - 1) or j in (0, n - 1)) and board[i][j] == "O":
                    board[i][j] = "A"
                    stack.append((i, j))

        while stack:
            x, y = stack.pop()
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == "O":
                    board[nx][ny] = "A"
                    stack.append((nx, ny))

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "A":
                    board[i][j] = "O"


if __name__ == "__main__":
    test_cases = [
        (
            [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]],
            [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]],
        ),
        ([["X"]], [["X"]]),
        ([["O"]], [["O"]]),
        ([["O", "O"], ["O", "O"]], [["O", "O"], ["O", "O"]]),
        (
            [["X", "X", "X"], ["X", "O", "X"], ["X", "X", "X"]],
            [["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]],
        ),
        (
            [["O", "X", "O"], ["X", "O", "X"], ["O", "X", "O"]],
            [["O", "X", "O"], ["X", "X", "X"], ["O", "X", "O"]],
        ),
        ([["O", "O", "O"]], [["O", "O", "O"]]),
    ]
    solution = Solution()
    for i, (board, expected) in enumerate(test_cases, 1):
        solution.solve(board)
        status = "PASS" if board == expected else "FAIL"
        print(f"测试用例 {i}: {status} (got={board}, expected={expected})")

    big = [["O"] * 200 for _ in range(200)]
    solution.solve(big)
    print(f"测试用例 {len(test_cases) + 1}: {'PASS' if all(c == 'O' for r in big for c in r) else 'FAIL'} (200x200 全 O，不应爆栈)")
