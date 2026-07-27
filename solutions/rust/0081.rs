/// 81. 搜索旋转排序数组 II
/// 允许重复的二分：nums[mid] == nums[right] 时无法判断哪半有序，
/// 退化为 right -= 1。最坏 O(n)，平均 O(log n)。
/// mid 用 i32 以便做 signed 比较，usize::saturating_sub/边界检查都交给内部处理，
/// 避免 mid = 0 时 mid - 1 下溢为 usize::MAX 的坑。
pub fn search(nums: Vec<i32>, target: i32) -> bool {
    if nums.is_empty() {
        return false;
    }
    let m = nums.len();
    let n = m;
    let mut left: i32 = 0;
    let mut right: i32 = (m as i32) - 1;

    while left <= right {
        let mid = left + (right - left) / 2;
        let mid_u = mid as usize;
        let right_u = right as usize;

        if nums[mid_u] == target {
            return true;
        }
        if nums[mid_u] == nums[right_u] {
            // 退化：right--，但要避免 right 越过 left 引发死循环 / 下溢
            if right == left {
                return false;
            }
            right -= 1;
        } else if nums[mid_u] < nums[right_u] {
            // 右半有序 [mid+1, right]
            if nums[mid_u] < target && target <= nums[right_u] {
                left = mid + 1;
            } else if mid > 0 {
                right = mid - 1;
            } else {
                return false;
            }
        } else {
            // 左半有序 [left, mid-1]
            if nums[left as usize] <= target && target < nums[mid_u] {
                if mid > 0 {
                    right = mid - 1;
                } else {
                    return false;
                }
            } else {
                left = mid + 1;
            }
        }
    }
    let _ = n;
    false
}

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> bool {
        search(nums, target)
    }
}