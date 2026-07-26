from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        80. 删除有序数组中的重复项 II
        快慢双指针：每个元素至多出现两次。
        通用判断：slow < k 或 nums[fast] != nums[slow - k]（k=2）。
        """
        if not nums:
            return 0
        slow = 0
        k = 2
        for fast in range(len(nums)):
            if slow < k or nums[fast] != nums[slow - k]:
                nums[slow] = nums[fast]
                slow += 1
        return slow


if __name__ == "__main__":
    test_cases = [
        ([1, 1, 1, 2, 2, 3], 5, [1, 1, 2, 2, 3]),
        ([0, 0, 1, 1, 1, 1, 2, 3, 3], 7, [0, 0, 1, 1, 2, 3, 3]),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
        ([1, 1, 1, 1], 2, [1, 1]),
    ]
    solution = Solution()
    for i, (nums, expected_len, expected_prefix) in enumerate(test_cases, 1):
        original = nums[:]
        got_len = solution.removeDuplicates(nums)
        got_prefix = nums[:got_len]
        ok = got_len == expected_len and got_prefix == expected_prefix
        status = "PASS" if ok else "FAIL"
        print(
            f"测试用例 {i}: {status} "
            f"(input={original}, len={got_len} (expected {expected_len}), "
            f"prefix={got_prefix} (expected {expected_prefix}))"
        )