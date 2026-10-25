from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        136. 只出现一次的数字
        位运算：a ^ a = 0，a ^ 0 = a，且异或满足交换律和结合律。
        把所有数依次异或起来，成对出现的数两两抵消，剩下的就是只出现一次的那个。
        时间 O(n)，空间 O(1)。
        """
        result = 0
        for x in nums:
            result ^= x
        return result


if __name__ == "__main__":
    test_cases = [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
        ([-1, -1, -2], -2),
        ([0, 5, 5], 0),
        ([30000, -30000, 30000], -30000),
        ([7, 3, 5, 3, 5], 7),
    ]
    solution = Solution()
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.singleNumber(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (nums={nums}, got={result}, expected={expected})")
