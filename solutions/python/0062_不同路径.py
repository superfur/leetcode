def unique_paths(m: int, n: int) -> int:
    """
    不同路径：m×n 网格，从左上角只能向右或向下走，到右下角的路径数。
    DP 一维：dp[j] += dp[j-1]。时间 O(mn)，空间 O(n)。
    """
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[n - 1]


def 不同路径(*args, **kwargs):
    """支持 (m, n) 或 m=..., n=..."""
    if args and len(args) >= 2:
        m, n = args[0], args[1]
    elif "m" in kwargs and "n" in kwargs:
        m, n = kwargs["m"], kwargs["n"]
    else:
        return 0
    return unique_paths(m, n)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return unique_paths(m, n)


if __name__ == "__main__":
    test_cases = [
        (3, 7, 28),
        (3, 2, 3),
        (7, 3, 28),
    ]
    for i, (m, n, expected) in enumerate(test_cases, 1):
        got = unique_paths(m, n)
        status = "通过" if got == expected else "失败"
        print(f"测试用例 {i}: {status} (m={m}, n={n}, 期望={expected}, 实际={got})")
