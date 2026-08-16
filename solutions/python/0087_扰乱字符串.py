from functools import lru_cache


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        """
        87. 扰乱字符串
        回溯枚举分割点 i：要么 s1[:i]/s1[i:] 与 s2[:i]/s2[i:] 同步扰乱，
        要么 s1[:i]/s1[i:] 与 s2[n-i:]/s2[:n-i]（交换）同步扰乱。
        剪枝：字符计数不等直接返回 false；用 lru_cache 记忆化。
        """
        @lru_cache(maxsize=None)
        def dfs(a: str, b: str) -> bool:
            if a == b:
                return True
            # 字符计数剪枝
            if sorted(a) != sorted(b):
                return False
            n = len(a)
            for i in range(1, n):
                # 不交换：a[:i] 对应 b[:i]，a[i:] 对应 b[i:]
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    return True
                # 交换：a[:i] 对应 b[n-i:]，a[i:] 对应 b[:n-i]
                if dfs(a[:i], b[n - i:]) and dfs(a[i:], b[:n - i]):
                    return True
            return False

        return dfs(s1, s2)


if __name__ == "__main__":
    test_cases = [
        ("great", "rgeat", True),
        ("abcde", "caebd", False),
        ("a", "a", True),
        ("a", "b", False),
        ("ab", "ba", True),
        ("abc", "cba", True),
    ]
    solution = Solution()
    for i, (s1, s2, expected) in enumerate(test_cases, 1):
        result = solution.isScramble(s1, s2)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (s1={s1!r}, s2={s2!r}, got={result}, expected={expected})")