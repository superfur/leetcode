from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        85. 最大矩形
        逐行累加直方图高度 heights[j] = 当前位置及上方连续 1 的数量，
        对每行 heights 调用 largestRectangleArea（单调栈）。
        """
        if not matrix or not matrix[0]:
            return 0
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0
        for row in matrix:
            for j in range(cols):
                heights[j] = heights[j] + 1 if row[j] == "1" else 0
            max_area = max(max_area, self._largest(heights))
        return max_area

    @staticmethod
    def _largest(heights: List[int]) -> int:
        # 内联 84 题单调栈实现 + 末尾 0 哨兵
        stack: List[int] = []
        best = 0
        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > h:
                top = stack.pop()
                height = heights[top]
                width = i if not stack else i - stack[-1] - 1
                best = max(best, height * width)
            stack.append(i)
        return best


if __name__ == "__main__":
    test_cases = [
        ([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]], 6),
        ([["0"]], 0),
        ([["1"]], 1),
        ([], 0),
        ([["1","1"],["1","1"]], 4),
        ([["1","0"],["0","1"]], 1),
    ]
    solution = Solution()
    for i, (matrix, expected) in enumerate(test_cases, 1):
        result = solution.maximalRectangle(matrix)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (got={result}, expected={expected})")