impl Solution {
    pub fn next_permutation(nums: &mut Vec<i32>) {
        let n = nums.len();
        if n <= 1 {
            return;
        }
        
        // 从右往左找第一个降序的位置
        let mut i = n - 2;
        while i > 0 && nums[i] >= nums[i + 1] {
            i -= 1;
        }
        
        if nums[i] < nums[i + 1] {
            // 找到了降序位置，从右往左找第一个大于nums[i]的位置
            let mut j = n - 1;
            while j > i && nums[j] <= nums[i] {
                j -= 1;
            }
            
            // 交换nums[i]和nums[j]
            nums.swap(i, j);
            
            // 反转从i+1到末尾的部分
            nums[i + 1..].reverse();
        } else {
            // 整个数组是降序的，直接反转整个数组
            nums.reverse();
        }
    }
}