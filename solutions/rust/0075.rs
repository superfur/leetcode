/// 75. 颜色分类
/// 荷兰国旗算法，三指针一趟扫描原地排序
pub fn sort_colors(nums: &mut Vec<i32>) {
    let mut low = 0usize;
    let mut current = 0usize;
    let mut high = nums.len();

    while current < high {
        match nums[current] {
            0 => {
                nums.swap(low, current);
                low += 1;
                current += 1;
            }
            2 => {
                high -= 1;
                nums.swap(current, high);
            }
            _ => {
                current += 1;
            }
        }
    }
}

impl Solution {
    pub fn sort_colors(nums: &mut Vec<i32>) {
        sort_colors(nums);
    }
}
