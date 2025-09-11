/**
 Do not return anything, modify nums in-place instead.
 */
 function nextPermutation(nums: number[]): void {
    const n = nums.length;
    if (n <= 1) {
        return;
    }
    
    // 从右往左找第一个降序的位置
    let i = n - 2;
    while (i >= 0 && nums[i] >= nums[i + 1]) {
        i--;
    }
    
    if (i >= 0) {
        // 找到了降序位置，从右往左找第一个大于nums[i]的位置
        let j = n - 1;
        while (j > i && nums[j] <= nums[i]) {
            j--;
        }
        
        // 交换nums[i]和nums[j]
        [nums[i], nums[j]] = [nums[j], nums[i]];
    }
    
    // 反转从i+1到末尾的部分
    reverse(nums, i + 1, n - 1);
};

// 辅助函数：反转数组指定范围
function reverse(nums: number[], start: number, end: number): void {
    while (start < end) {
        [nums[start], nums[end]] = [nums[end], nums[start]];
        start++;
        end--;
    }
}