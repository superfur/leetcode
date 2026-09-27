from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        119. 杨辉三角 II
        只用一个长度为 rowIndex+1 的数组原地滚动更新：
        每处理一行就从右往左把 row[j] 加上 row[j-1]（右往左是关键，
        避免用本行已经更新过的值覆盖还没处理的旧值）。
        """
        row = [1] * (rowIndex + 1)
        for i in range(1, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] += row[j - 1]
        return row


if __name__ == "__main__":
    test_cases = [
        (3, [1, 3, 3, 1]),
        (0, [1]),
        (1, [1, 1]),
    ]
    solution = Solution()
    for i, (row_index, expected) in enumerate(test_cases, 1):
        result = solution.getRow(row_index)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (rowIndex={row_index}, got={result}, expected={expected})")
