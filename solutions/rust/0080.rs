/// 80. 删除有序数组中的重复项 II
/// 快慢双指针：每个元素至多出现两次。
/// 通用判断：slow < k 或 nums[fast] != nums[slow-k]（k=2）。
pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
    let k: usize = 2;
    let mut slow: usize = 0;
    for fast in 0..nums.len() {
        if slow < k || nums[fast] != nums[slow - k] {
            nums[slow] = nums[fast];
            slow += 1;
        }
    }
    slow as i32
}

impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        remove_duplicates(nums)
    }
}