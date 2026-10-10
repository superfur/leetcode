from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        127. 单词接龙
        BFS：从 beginWord 出发，每次把某一位换成 a~z，命中字典的单词就入队，
        并立刻从字典里删掉（等价于标记已访问）。
        第一次碰到 endWord 时的步数（按单词个数计，起点算 1）就是答案。
        """
        words = set(wordList)
        if endWord not in words:
            return 0

        queue = deque([(beginWord, 1)])
        words.discard(beginWord)
        letters = "abcdefghijklmnopqrstuvwxyz"

        while queue:
            word, steps = queue.popleft()
            for i in range(len(word)):
                for c in letters:
                    if c == word[i]:
                        continue
                    nw = word[:i] + c + word[i + 1:]
                    if nw in words:
                        if nw == endWord:
                            return steps + 1
                        words.remove(nw)
                        queue.append((nw, steps + 1))
        return 0


if __name__ == "__main__":
    test_cases = [
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5),
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0),
        ("a", "c", ["a", "b", "c"], 2),
        ("hot", "dog", ["hot", "dog"], 0),
        ("hot", "dog", ["hot", "dog", "dot"], 3),
        ("abc", "xyz", ["abd", "xyz"], 0),
    ]
    solution = Solution()
    for i, (begin, end, words, expected) in enumerate(test_cases, 1):
        result = solution.ladderLength(begin, end, words)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (begin={begin}, end={end}, got={result}, expected={expected})")
