from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        77. 组合
        回溯 + 剪枝，返回 [1, n] 中所有 k 个数的组合
        """
        result: List[List[int]] = []
        path: List[int] = []

        def dfs(start: int) -> None:
            if len(path) == k:
                result.append(path[:])
                return
            # 剪枝: i <= n - (k - len(path)) + 1
            upper = n - (k - len(path)) + 1
            for i in range(start, upper + 1):
                path.append(i)
                dfs(i + 1)
                path.pop()

        dfs(1)
        return result


if __name__ == "__main__":
    test_cases = [
        (4, 2, [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]),
        (1, 1, [[1]]),
        (5, 3, [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5],
                 [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5]]),
    ]
    solution = Solution()
    for i, (n, k, expected) in enumerate(test_cases, 1):
        result = solution.combine(n, k)
        as_set = {tuple(c) for c in result}
        target_set = {tuple(c) for c in expected}
        status = "PASS" if as_set == target_set and len(result) == len(expected) else "FAIL"
        print(f"测试用例 {i}: {status} (n={n},k={k}, got={len(result)}, expected={len(expected)})")