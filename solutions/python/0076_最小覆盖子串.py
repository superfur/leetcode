from typing import Dict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        76. 最小覆盖子串
        滑动窗口 + 频率计数，时间复杂度 O(m+n)
        """
        if not t or not s:
            return ""

        need: Dict[str, int] = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        required = len(need)
        formed = 0
        left = 0
        best_left = 0
        best_length = float("inf")
        window_count: Dict[str, int] = {}

        for right, ch in enumerate(s):
            window_count[ch] = window_count.get(ch, 0) + 1
            if ch in need and window_count[ch] == need[ch]:
                formed += 1

            while formed == required and left <= right:
                current_length = right - left + 1
                if current_length < best_length:
                    best_length = current_length
                    best_left = left

                left_ch = s[left]
                window_count[left_ch] -= 1
                if left_ch in need and window_count[left_ch] < need[left_ch]:
                    formed -= 1
                left += 1

        return "" if best_length == float("inf") else s[best_left: best_left + best_length]


if __name__ == "__main__":
    test_cases = [
        {"input": {"s": "ADOBECODEBANC", "t": "ABC"}, "expected": "BANC"},
        {"input": {"s": "a", "t": "a"}, "expected": "a"},
        {"input": {"s": "a", "t": "aa"}, "expected": ""},
        {"input": {"s": "ab", "t": "b"}, "expected": "b"},
        {"input": {"s": "bba", "t": "ab"}, "expected": "ba"},
        {"input": {"s": "bbaac", "t": "abc"}, "expected": "baac"},
    ]
    solution = Solution()
    for i, tc in enumerate(test_cases, 1):
        result = solution.minWindow(tc["input"]["s"], tc["input"]["t"])
        status = "PASS" if result == tc["expected"] else "FAIL"
        print(f"测试用例 {i}: {status} (got={result!r}, expected={tc['expected']!r})")