impl Solution {
    pub fn search_range(nums: Vec<i32>, target: i32) -> Vec<i32> {
        if nums.is_empty() {
            return vec![-1, -1];
        }
        
        // 查找左边界
        let left_bound = Self::find_left_bound(&nums, target);
        if left_bound == -1 {
            return vec![-1, -1];
        }
        
        // 查找右边界
        let right_bound = Self::find_right_bound(&nums, target);
        
        vec![left_bound, right_bound]
    }
    
    fn find_left_bound(nums: &[i32], target: i32) -> i32 {
        let mut left = 0;
        let mut right = nums.len() - 1;
        let mut result = -1;
        
        while left <= right {
            let mid = left + (right - left) / 2;
            
            if nums[mid] == target {
                result = mid as i32;
                if mid == 0 { break; } // 防止下溢
                right = mid - 1;
            } else if nums[mid] < target {
                left = mid + 1;
            } else {
                if mid == 0 { break; } // 防止下溢
                right = mid - 1;
            }
        }
        
        result
    }
    
    fn find_right_bound(nums: &[i32], target: i32) -> i32 {
        let mut left = 0;
        let mut right = nums.len() - 1;
        let mut result = -1;
        
        while left <= right {
            let mid = left + (right - left) / 2;
            
            if nums[mid] == target {
                result = mid as i32;
                left = mid + 1;
            } else if nums[mid] < target {
                left = mid + 1;
            } else {
                if mid == 0 { break; } // 防止下溢
                right = mid - 1;
            }
        }
        
        result
    }
}