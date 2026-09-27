from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        118. 杨辉三角
        逐行生成：每行首尾都是 1，中间第 j 个数等于上一行第 j-1 和第 j 个数之和。
        """
        result: List[List[int]] = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]
            result.append(row)
        return result


if __name__ == "__main__":
    test_cases = [
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
        (1, [[1]]),
    ]
    solution = Solution()
    for i, (num_rows, expected) in enumerate(test_cases, 1):
        result = solution.generate(num_rows)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (numRows={num_rows}, got={result}, expected={expected})")
