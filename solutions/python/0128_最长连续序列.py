from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        128. 最长连续序列
        哈希集合去重，只从「序列起点」（x - 1 不在集合里）出发往后数 x+1, x+2, ...，
        每个数最多被数一次，所以整体 O(n)。
        """
        num_set = set(nums)
        best = 0
        for x in num_set:
            if x - 1 in num_set:
                continue
            end = x
            while end + 1 in num_set:
                end += 1
            best = max(best, end - x + 1)
        return best


if __name__ == "__main__":
    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([1, 0, 1, 2], 3),
        ([], 0),
        ([5], 1),
        ([1, 1, 1], 1),
        ([-1000000000, 1000000000], 1),
        ([-2, -1, 0, 1], 4),
    ]
    solution = Solution()
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.longestConsecutive(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (nums={nums}, got={result}, expected={expected})")
