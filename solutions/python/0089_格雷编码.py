from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        """
        89. 格雷编码
        经典公式：gray(i) = i ^ (i >> 1)。
        验证：相邻 i 与 i+1 的 gray 只差一位；
        首位 i=0 的 gray 是 0；末位 i=2^n-1 与 i=0 的 gray 只差一位。
        """
        return [i ^ (i >> 1) for i in range(1 << n)]


if __name__ == "__main__":
    test_cases = [
        (1, [0, 1]),
        (2, [0, 1, 3, 2]),
        (3, [0, 1, 3, 2, 6, 7, 5, 4]),
        (4, [0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8]),
        (0, [0]),
    ]
    solution = Solution()
    for i, (n, expected) in enumerate(test_cases, 1):
        result = solution.grayCode(n)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (n={n}, got={result}, expected={expected})")