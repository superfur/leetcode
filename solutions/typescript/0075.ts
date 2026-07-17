/**
 * 75. 颜色分类
 * Do not return anything, modify nums in-place instead.
 */
function sortColors(nums: number[]): void {
    let low = 0;
    let current = 0;
    let high = nums.length - 1;

    while (current <= high) {
        if (nums[current] === 0) {
            [nums[low], nums[current]] = [nums[current], nums[low]];
            low++;
            current++;
        } else if (nums[current] === 2) {
            [nums[current], nums[high]] = [nums[high], nums[current]];
            high--;
        } else {
            current++;
        }
    }
}

export default sortColors;
