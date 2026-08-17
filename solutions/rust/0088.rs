/// 88. 合并两个有序数组
/// 从后往前双指针：i 指向 nums1 有效末尾，j 指向 nums2 末尾，
/// k 指向 nums1 末尾。把较大的放到 k，相应指针前移。
/// 最后 nums2 若有剩余，复制到 nums1 前部。
/// mid/i/j 用 i32 避免 0-1 下溢（参见 [[rust-usize-mid-underflow]]）。
pub fn merge(nums1: &mut Vec<i32>, m: i32, nums2: &mut Vec<i32>, n: i32) {
    let mut i: i32 = m - 1;
    let mut j: i32 = n - 1;
    let mut k: i32 = m + n - 1;
    while i >= 0 && j >= 0 {
        if nums1[i as usize] >= nums2[j as usize] {
            nums1[k as usize] = nums1[i as usize];
            i -= 1;
        } else {
            nums1[k as usize] = nums2[j as usize];
            j -= 1;
        }
        k -= 1;
    }
    while j >= 0 {
        nums1[k as usize] = nums2[j as usize];
        j -= 1;
        k -= 1;
    }
}

impl Solution {
    pub fn merge(nums1: &mut Vec<i32>, m: i32, nums2: &mut Vec<i32>, n: i32) {
        merge(nums1, m, nums2, n);
    }
}