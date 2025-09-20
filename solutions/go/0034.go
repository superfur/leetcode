func searchRange(nums []int, target int) []int {
    if len(nums) == 0 {
        return []int{-1, -1}
    }
    
    left, right := 0, len(nums)-1
    leftBound, rightBound := -1, -1
    
    // 查找左边界
    for left <= right {
        mid := left + (right-left)/2
        
        if nums[mid] == target {
            leftBound = mid
            right = mid - 1 // 继续在左半部分搜索
        } else if nums[mid] < target {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
    
    // 如果左边界不存在，直接返回
    if leftBound == -1 {
        return []int{-1, -1}
    }
    
    // 重置边界，查找右边界
    left, right = leftBound, len(nums)-1
    
    for left <= right {
        mid := left + (right-left)/2
        
        if nums[mid] == target {
            rightBound = mid
            left = mid + 1 // 继续在右半部分搜索
        } else if nums[mid] < target {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
    
    return []int{leftBound, rightBound}
}