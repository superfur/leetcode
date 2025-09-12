from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        算法步骤：
        1. 从右往左找到第一个满足 nums[i] < nums[i+1] 的位置 i
        2. 从右往左找到第一个满足 nums[j] > nums[i] 的位置 j  
        3. 交换 nums[i] 和 nums[j]
        4. 反转从位置 i+1 到数组末尾的部分
        """
        n = len(nums)
        if n <= 1:
            return
        
        # 步骤1: 从右往左找到第一个满足 nums[i] < nums[i+1] 的位置 i
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # 如果找不到这样的位置，说明整个数组是降序的，直接反转整个数组
        if i == -1:
            self.reverse(nums, 0, n - 1)
            return
        
        # 步骤2: 从右往左找到第一个满足 nums[j] > nums[i] 的位置 j
        j = n - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        
        # 步骤3: 交换 nums[i] 和 nums[j]
        nums[i], nums[j] = nums[j], nums[i]
        
        # 步骤4: 反转从位置 i+1 到数组末尾的部分
        self.reverse(nums, i + 1, n - 1)
    
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        """反转数组中从 start 到 end 的部分"""
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1