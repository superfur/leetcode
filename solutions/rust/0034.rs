impl Solution {
    pub fn search_range(nums: Vec<i32>, target: i32) -> Vec<i32> {
        if nums.is_empty() {
            return vec![-1, -1];
        }
        
        let mut left = 0;
        let mut right = nums.len().saturating_sub(1);
        let mut left_bound = -1;
        let mut right_bound = -1;
        
        // 查找左边界
        while left <= right {
            let mid = left + (right - left) / 2;
            
            if nums[mid] == target {
                left_bound = mid as i32;
                right = mid.saturating_sub(1); // 继续在左半部分搜索
            } else if nums[mid] < target {
                left = mid + 1;
            } else {
                right = mid.saturating_sub(1);
            }
        }
        
        // 如果左边界不存在，直接返回
        if left_bound == -1 {
            return vec![-1, -1];
        }
        
        // 重置边界，查找右边界
        left = left_bound as usize;
        right = nums.len().saturating_sub(1);
        
        while left <= right {
            let mid = left + (right - left) / 2;
            
            if nums[mid] == target {
                right_bound = mid as i32;
                left = mid + 1; // 继续在右半部分搜索
            } else if nums[mid] < target {
                left = mid + 1;
            } else {
                right = mid.saturating_sub(1);
            }
        }
        
        vec![left_bound, right_bound]
    }
}