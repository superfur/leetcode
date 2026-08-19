from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        90. 子集 II
        排序 + 回溯：排序后，遇到与上一个未取元素相同的数就跳过，
        保证同一层只展开一次相同值，从而避免重复子集。
        """
        nums.sort()
        result: List[List[int]] = []
        path: List[int] = []

        def backtrack(start: int) -> None:
            result.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return result


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 2], [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]),
        ([0], [[], [0]]),
        ([1, 1, 2], [[], [1], [1, 1], [1, 1, 2], [1, 2], [2]]),
        ([4, 4, 4, 1, 4], [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4],
                            [1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]]),
    ]
    solution = Solution()
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.subsetsWithDup(nums[:])
        # 内部子集各自排序，再把外层排序，统一比较
        norm = lambda lst: sorted([sorted(s) for s in lst])
        status = "PASS" if norm(result) == norm(expected) else "FAIL"
        print(f"测试用例 {i}: {status} (nums={nums})")