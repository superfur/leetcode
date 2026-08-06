from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        84. 柱状图中最大的矩形
        单调递增栈：栈中保存索引，对应高度严格递增。
        遇到 heights[i] < heights[stack.top] 时弹栈并以弹出的高度为基准计算面积：
        width = i - stack[-1] - 1（栈空则为 i）。
        末尾追加一个 0 哨兵，确保所有柱子被清算。
        """
        stack: List[int] = []
        max_area = 0
        # 末尾追加 0 哨兵，避免最后还要单独 flush 栈
        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > h:
                top = stack.pop()
                height = heights[top]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area


if __name__ == "__main__":
    test_cases = [
        ([2, 1, 5, 6, 2, 3], 10),
        ([2, 4], 4),
        ([], 0),
        ([1], 1),
        ([0, 0, 0], 0),
        ([4, 2, 0, 3, 2, 5], 6),
        ([1, 2, 3, 4, 5], 9),
    ]
    solution = Solution()
    for i, (heights, expected) in enumerate(test_cases, 1):
        result = solution.largestRectangleArea(heights)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (heights={heights}, got={result}, expected={expected})")