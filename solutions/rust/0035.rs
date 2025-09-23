impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        if nums.is_empty() {
            return 0;
        }
        let mut left: isize = 0;
        let mut right: isize = nums.len() as isize - 1;
        while left <= right {
            let mid = left + (right - left) / 2;
            let val = nums[mid as usize];
            if val == target {
                return mid as i32;
            } else if val < target {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        left as i32
    }
}