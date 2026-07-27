/**
 * 81. 搜索旋转排序数组 II
 * 给定旋转后的非降序数组（允许重复）和 target，
 * 判断 target 是否存在。
 * 允许重复的二分：nums[mid] === nums[right] 时无法判断哪半有序，
 * 退化为 right--。最坏 O(n)。
 */
function search(nums: number[], target: number): boolean {
    let left = 0;
    let right = nums.length - 1;
    while (left <= right) {
        const mid = (left + right) >> 1;
        if (nums[mid] === target) return true;
        if (nums[mid] === nums[right]) {
            right--;
        } else if (nums[mid] < nums[right]) {
            // 右半有序 [mid+1, right]
            if (nums[mid] < target && target <= nums[right]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        } else {
            // 左半有序 [left, mid-1]
            if (nums[left] <= target && target < nums[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
    }
    return false;
}

export default search;