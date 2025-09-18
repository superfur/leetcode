impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut left = 0;
        let mut right = nums.len().saturating_sub(1);
        
        while left <= right {
            let mid = left + (right - left) / 2;
            
            // 如果找到目标值，直接返回
            if nums[mid] == target {
                return mid as i32;
            }
            
            // 判断哪一半是有序的
            if nums[left] <= nums[mid] {
                // 左半部分是有序的
                if nums[left] <= target && target < nums[mid] {
                    // 目标值在左半部分
                    right = mid.saturating_sub(1);
                } else {
                    // 目标值在右半部分
                    left = mid + 1;
                }
            } else {
                // 右半部分是有序的
                if nums[mid] < target && target <= nums[right] {
                    // 目标值在右半部分
                    left = mid + 1;
                } else {
                    // 目标值在左半部分
                    right = mid.saturating_sub(1);
                }
            }
        }
        
        -1
    }
}