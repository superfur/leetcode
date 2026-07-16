from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        74. 搜索二维矩阵
        把二维矩阵视作一维有序数组，使用二分查找
        """
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            row, col = divmod(mid, n)
            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


if __name__ == "__main__":
    test_cases = [
        {"input": {"matrix": [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], "target": 3}, "expected": True},
        {"input": {"matrix": [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], "target": 13}, "expected": False},
        {"input": {"matrix": [[1]], "target": 1}, "expected": True},
        {"input": {"matrix": [[1]], "target": 2}, "expected": False},
        {"input": {"matrix": [[1, 3]], "target": 3}, "expected": True},
        {"input": {"matrix": [[1, 3], [5, 7]], "target": 4}, "expected": False},
    ]
    for i, tc in enumerate(test_cases, 1):
        result = Solution().searchMatrix(tc["input"]["matrix"], tc["input"]["target"])
        status = "PASS" if result == tc["expected"] else "FAIL"
        print(f"测试用例 {i}: {status} (got={result}, expected={tc['expected']})")