class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        left, right = 0, len(nums) - 1
        left_bound = right_bound = -1
        
        # 查找左边界
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                left_bound = mid
                right = mid - 1  # 继续在左半部分搜索
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # 如果左边界不存在，直接返回
        if left_bound == -1:
            return [-1, -1]
        
        # 重置边界，查找右边界
        left, right = left_bound, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                right_bound = mid
                left = mid + 1  # 继续在右半部分搜索
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return [left_bound, right_bound]
        