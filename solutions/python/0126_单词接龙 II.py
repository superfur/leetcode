from collections import defaultdict
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
        126. 单词接龙 II
        BFS 逐层扩展，记录每个单词在最短路径上的所有前驱（只记录首次被发现的那一层），
        第一次碰到 endWord 就停；然后从 endWord 沿前驱表回溯到 beginWord，还原所有最短路径。
        """
        words = set(wordList)
        if endWord not in words:
            return []

        parents = defaultdict(list)
        visited = {beginWord}
        level = {beginWord}
        found = False
        letters = "abcdefghijklmnopqrstuvwxyz"

        while level and not found:
            nxt = set()
            for w in level:
                for i in range(len(w)):
                    for c in letters:
                        if c == w[i]:
                            continue
                        nw = w[:i] + c + w[i + 1:]
                        if nw in words and nw not in visited:
                            parents[nw].append(w)
                            nxt.add(nw)
                            if nw == endWord:
                                found = True
            visited |= nxt
            level = nxt

        if not found:
            return []

        res: List[List[str]] = []
        path = [endWord]

        def back(w: str) -> None:
            if w == beginWord:
                res.append(path[::-1])
                return
            for p in parents[w]:
                path.append(p)
                back(p)
                path.pop()

        back(endWord)
        return res


if __name__ == "__main__":
    test_cases = [
        (
            "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"],
            [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]],
        ),
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], []),
        ("a", "c", ["a", "b", "c"], [["a", "c"]]),
        (
            "red", "tax", ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"],
            [["red", "ted", "tad", "tax"], ["red", "ted", "tex", "tax"], ["red", "rex", "tex", "tax"]],
        ),
        ("abc", "xyz", ["abd", "xyz"], []),
    ]
    solution = Solution()
    for i, (begin, end, words, expected) in enumerate(test_cases, 1):
        result = solution.findLadders(begin, end, words)
        status = "PASS" if sorted(result) == sorted(expected) else "FAIL"
        print(f"测试用例 {i}: {status} (got={result}, expected={expected})")
