import random
from typing import List


class Solution:
    def minCut(self, s: str) -> int:
        """
        132. 分割回文串 II
        先用区间 DP 预处理 is_pal[i][j]（s[i..j] 是否回文）；
        再令 dp[i] 为 s[0..i] 的最少分割次数：
        若 s[0..i] 本身是回文则为 0，否则枚举最后一段回文 s[j+1..i]，取 dp[j] + 1 的最小值。
        时间 O(n^2)。
        """
        n = len(s)
        is_pal = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                is_pal[i][j] = s[i] == s[j] and is_pal[i + 1][j - 1]

        dp = [0] * n
        for i in range(n):
            if is_pal[0][i]:
                dp[i] = 0
                continue
            best = i
            for j in range(i):
                if is_pal[j + 1][i] and dp[j] + 1 < best:
                    best = dp[j] + 1
            dp[i] = best
        return dp[n - 1]


def brute_force(s: str) -> int:
    n = len(s)
    best = n - 1

    def back(start: int, parts: int) -> None:
        nonlocal best
        if start == n:
            best = min(best, parts - 1)
            return
        for end in range(start, n):
            piece = s[start:end + 1]
            if piece == piece[::-1]:
                back(end + 1, parts + 1)

    back(0, 0)
    return best


if __name__ == "__main__":
    test_cases = [
        ("aab", 1),
        ("a", 0),
        ("ab", 1),
        ("aba", 0),
        ("abc", 2),
        ("aaaa", 0),
        ("abcba", 0),
        ("ababbbabbababa", 3),
        ("a" * 2000, 0),
        ("ab" * 1000, 1),
    ]
    solution = Solution()
    for i, (s, expected) in enumerate(test_cases, 1):
        result = solution.minCut(s)
        status = "PASS" if result == expected else "FAIL"
        shown = s if len(s) <= 20 else s[:8] + "..." + f"(len={len(s)})"
        print(f"测试用例 {i}: {status} (s={shown!r}, got={result}, expected={expected})")

    random.seed(132)
    mismatches = 0
    for _ in range(500):
        s = "".join(random.choice("abc") for _ in range(random.randint(1, 10)))
        if solution.minCut(s) != brute_force(s):
            mismatches += 1
            print(f"随机对拍不一致: s={s!r}")
    print(f"测试用例 {len(test_cases) + 1}: {'PASS' if mismatches == 0 else 'FAIL'} (500 个随机小串与暴力回溯对拍，不一致 {mismatches} 个)")
