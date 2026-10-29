import random
import re
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        139. 单词拆分
        dp[i] 表示 s 的前 i 个字符能否被拆成字典里的单词（dp[0] = True）。
        对每个 i 枚举「最后一个单词」的起点 j：dp[j] 为真且 s[j:i] 在字典里，则 dp[i] 为真。
        字典里最长的单词长度为 max_len，所以 j 只需要从 i - max_len 开始往后枚举，
        用集合判断单词是否存在。时间 O(n * max_len * max_len)。
        """
        words = set(wordDict)
        max_len = max(len(w) for w in words)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(max(0, i - max_len), i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[n]


if __name__ == "__main__":
    test_cases = [
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
        ("a", ["a"], True),
        ("a", ["b"], False),
        ("aaaaaaa", ["aaaa", "aaa"], True),
        ("aaaaaaa", ["aaaa", "aa"], False),
        ("cars", ["car", "ca", "rs"], True),
        ("a" * 299 + "b", ["a" * k for k in range(1, 21)], False),
        ("a" * 300, ["a" * 20, "a" * 19], True),
    ]
    solution = Solution()
    for i, (s, words, expected) in enumerate(test_cases, 1):
        result = solution.wordBreak(s, words)
        status = "PASS" if result == expected else "FAIL"
        shown = s if len(s) <= 20 else s[:8] + f"...(len={len(s)})"
        print(f"测试用例 {i}: {status} (s={shown!r}, got={result}, expected={expected})")

    random.seed(139)
    mismatches = 0
    for _ in range(500):
        words = list({"".join(random.choice("ab") for _ in range(random.randint(1, 4))) for _ in range(random.randint(1, 5))})
        s = "".join(random.choice("ab") for _ in range(random.randint(1, 14)))
        expected = re.fullmatch("(?:" + "|".join(words) + ")+", s) is not None
        if solution.wordBreak(s, words) != expected:
            mismatches += 1
            print(f"随机对拍不一致: s={s!r}, words={words}")
    print(f"测试用例 {len(test_cases) + 1}: {'PASS' if mismatches == 0 else 'FAIL'} (500 组随机数据与正则 fullmatch 对拍，不一致 {mismatches} 组)")
