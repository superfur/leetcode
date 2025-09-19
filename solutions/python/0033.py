class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # 如果找到目标值，直接返回
            if nums[mid] == target:
                return mid
            
            # 判断哪一半是有序的
            if nums[left] <= nums[mid]:
                # 左半部分是有序的
                if nums[left] <= target < nums[mid]:
                    # 目标值在左半部分
                    right = mid - 1
                else:
                    # 目标值在右半部分
                    left = mid + 1
            else:
                # 右半部分是有序的
                if nums[mid] < target <= nums[right]:
                    # 目标值在右半部分
                    left = mid + 1
                else:
                    # 目标值在左半部分
                    right = mid - 1
        
        return -1
