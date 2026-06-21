from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0


if __name__ == "__main__":
    import copy

    test_cases = [
        {"input": [[1, 1, 1], [1, 0, 1], [1, 1, 1]], "expected": [[1, 0, 1], [0, 0, 0], [1, 0, 1]]},
        {"input": [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]], "expected": [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]},
        {"input": [[1]], "expected": [[1]]},
        {"input": [[0]], "expected": [[0]]},
        {"input": [[1, 0]], "expected": [[0, 0]]},
        {"input": [[1], [0]], "expected": [[0], [0]]},
    ]
    for i, tc in enumerate(test_cases, 1):
        matrix = copy.deepcopy(tc["input"])
        Solution().setZeroes(matrix)
        status = "PASS" if matrix == tc["expected"] else "FAIL"
        print(f"测试用例 {i}: {status} (got={matrix}, expected={tc['expected']})")
