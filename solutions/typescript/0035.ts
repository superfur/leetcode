function searchInsert(nums: number[], target: number): number {
    let left = 0;
    let right = nums.length - 1;
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        
        if (nums[mid] === target) {
            return mid; // 找到目标值，返回索引
        } else if (nums[mid] < target) {
            left = mid + 1; // 目标值在右半部分
        } else {
            right = mid - 1; // 目标值在左半部分
        }
    }
    
    // 如果没找到目标值，left 就是应该插入的位置
    return left;
};