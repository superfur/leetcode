from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        75. 颜色分类
        荷兰国旗算法，三指针一趟扫描原地排序
        Do not return anything, modify nums in-place instead.
        """
        low, current, high = 0, 0, len(nums) - 1
        while current <= high:
            if nums[current] == 0:
                nums[low], nums[current] = nums[current], nums[low]
                low += 1
                current += 1
            elif nums[current] == 2:
                nums[current], nums[high] = nums[high], nums[current]
                high -= 1
            else:
                current += 1


if __name__ == "__main__":
    test_cases = [
        {"input": {"nums": [2, 0, 2, 1, 1, 0]}, "expected": [0, 0, 1, 1, 2, 2]},
        {"input": {"nums": [2, 0, 1]}, "expected": [0, 1, 2]},
        {"input": {"nums": [0]}, "expected": [0]},
        {"input": {"nums": [2, 2, 1, 0, 0, 1]}, "expected": [0, 0, 1, 1, 2, 2]},
    ]
    for i, tc in enumerate(test_cases, 1):
        nums = tc["input"]["nums"][:]
        Solution().sortColors(nums)
        status = "PASS" if nums == tc["expected"] else "FAIL"
        print(f"测试用例 {i}: {status} (got={nums}, expected={tc['expected']})")
