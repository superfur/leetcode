from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        81. 搜索旋转排序数组 II
        允许重复的二分：nums[mid] == nums[right] 时无法判断哪半有序，
        退化为 right -= 1。最坏 O(n)，平均 O(log n)。
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[right]:
                right -= 1
            elif nums[mid] < nums[right]:
                # 右半有序 [mid+1, right]
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # 左半有序 [left, mid-1]
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return False


if __name__ == "__main__":
    test_cases = [
        ([2, 5, 6, 0, 0, 1, 2], 0, True),
        ([2, 5, 6, 0, 0, 1, 2], 3, False),
        ([1, 0, 1, 1, 1], 0, True),
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], 2, True),
        ([1, 1], 0, False),
    ]
    solution = Solution()
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = solution.search(nums, target)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (target={target}, got={result}, expected={expected})")