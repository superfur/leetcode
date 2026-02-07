from typing import List


def generate_matrix(n: int) -> List[List[int]]:
    """
    螺旋矩阵 II - 边界模拟法

    时间复杂度: O(n²)，填充 n² 个元素
    空间复杂度: O(1)，除了结果矩阵外只使用常数个变量

    思路:
    1. 创建 n×n 矩阵，定义四个边界：top, bottom, left, right
    2. 按照 右->下->左->上 的顺序填充数字 1 到 n²
    3. 每完成一个方向，更新对应的边界
    4. 当 num > n² 时停止

    示例: n = 3 -> [[1,2,3],[8,9,4],[7,6,5]]
    """
    matrix = [[0] * n for _ in range(n)]

    top, bottom = 0, n - 1
    left, right = 0, n - 1
    num = 1

    while num <= n * n:
        # 向右：填充 top 行
        for j in range(left, right + 1):
            matrix[top][j] = num
            num += 1
        top += 1

        # 向下：填充 right 列
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # 向左：填充 bottom 行（若有剩余行）
        if top <= bottom:
            for j in range(right, left - 1, -1):
                matrix[bottom][j] = num
                num += 1
            bottom -= 1

        # 向上：填充 left 列（若有剩余列）
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    return matrix


class Solution:
    """LeetCode 驱动需要的 Solution 类"""

    def generateMatrix(self, n: int) -> List[List[int]]:
        return generate_matrix(n)
