from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        78. 子集
        回溯枚举所有子集（幂集），数组元素互不相同
        """
        result: List[List[int]] = []
        path: List[int] = []

        def dfs(start: int) -> None:
            result.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i + 1)
                path.pop()

        dfs(0)
        return result


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
        ([0], [[], [0]]),
        ([1, 2], [[], [1], [2], [1, 2]]),
    ]
    solution = Solution()
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.subsets(nums)
        as_set = {tuple(sorted(c)) for c in result}
        target_set = {tuple(sorted(c)) for c in expected}
        ok = as_set == target_set and len(result) == len(expected)
        status = "PASS" if ok else "FAIL"
        print(f"测试用例 {i}: {status} (nums={nums}, got={len(result)}, expected={len(expected)})")