import random
from typing import Dict, List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        140. 单词拆分 II
        记忆化回溯：dfs(start) 返回后缀 s[start:] 的所有拆分句子。
        枚举第一个单词 s[start:end]（长度不超过字典最长单词），在字典里就把它拼到 dfs(end) 的每个句子前面；
        start == n 时返回 [""]，表示「恰好拆完」，拼接时据此决定要不要加空格。
        按起点缓存结果，相同的后缀不会被重复展开。
        """
        words = set(wordDict)
        max_len = max(len(w) for w in words)
        n = len(s)
        memo: Dict[int, List[str]] = {}

        def dfs(start: int) -> List[str]:
            if start == n:
                return [""]
            if start in memo:
                return memo[start]
            res: List[str] = []
            for end in range(start + 1, min(n, start + max_len) + 1):
                word = s[start:end]
                if word in words:
                    for tail in dfs(end):
                        res.append(word if not tail else word + " " + tail)
            memo[start] = res
            return res

        return dfs(0)


def brute_force(s: str, words: List[str]) -> List[str]:
    n = len(s)
    word_set = set(words)
    res = []
    for mask in range(1 << (n - 1)):
        parts, last = [], 0
        for i in range(n - 1):
            if mask >> i & 1:
                parts.append(s[last:i + 1])
                last = i + 1
        parts.append(s[last:])
        if all(p in word_set for p in parts):
            res.append(" ".join(parts))
    return res


if __name__ == "__main__":
    test_cases = [
        ("catsanddog", ["cat", "cats", "and", "sand", "dog"], ["cats and dog", "cat sand dog"]),
        (
            "pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"],
            ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"],
        ),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], []),
        ("a", ["a"], ["a"]),
        ("a", ["b"], []),
        ("aaa", ["a", "aa", "aaa"], ["a a a", "a aa", "aa a", "aaa"]),
        ("abc", ["abc", "a", "bc", "ab", "c"], ["abc", "a bc", "ab c"]),
    ]
    solution = Solution()
    for i, (s, words, expected) in enumerate(test_cases, 1):
        result = solution.wordBreak(s, words)
        status = "PASS" if sorted(result) == sorted(expected) else "FAIL"
        print(f"测试用例 {i}: {status} (s={s!r}, got={result}, expected={expected})")

    dictionary = ["a" * k for k in range(1, 11)]
    count = len(solution.wordBreak("a" * 20, dictionary))
    ways = [1] + [0] * 20
    for i in range(1, 21):
        ways[i] = sum(ways[i - k] for k in range(1, 11) if i - k >= 0)
    print(f"测试用例 {len(test_cases) + 1}: {'PASS' if count == ways[20] else 'FAIL'} (20 个 a，句子数={count}，期望 {ways[20]})")

    random.seed(140)
    mismatches = 0
    for _ in range(500):
        words = list({"".join(random.choice("ab") for _ in range(random.randint(1, 3))) for _ in range(random.randint(1, 5))})
        s = "".join(random.choice("ab") for _ in range(random.randint(1, 12)))
        if sorted(solution.wordBreak(s, words)) != sorted(brute_force(s, words)):
            mismatches += 1
            print(f"随机对拍不一致: s={s!r}, words={words}")
    print(f"测试用例 {len(test_cases) + 2}: {'PASS' if mismatches == 0 else 'FAIL'} (500 组随机数据与枚举全部切分点的暴力解对拍，不一致 {mismatches} 组)")
