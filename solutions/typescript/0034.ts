function searchRange(nums: number[], target: number): number[] {
    if (nums.length === 0) {
        return [-1, -1];
    }
    
    // 查找左边界
    const leftBound = findLeftBound(nums, target);
    if (leftBound === -1) {
        return [-1, -1];
    }
    
    // 查找右边界
    const rightBound = findRightBound(nums, target);
    
    return [leftBound, rightBound];
}

function findLeftBound(nums: number[], target: number): number {
    let left = 0;
    let right = nums.length - 1;
    let result = -1;
    
    while (left <= right) {
        const mid = Math.floor(left + (right - left) / 2);
        
        if (nums[mid] === target) {
            result = mid;
            if (mid === 0) break; // 防止下溢
            right = mid - 1;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            if (mid === 0) break; // 防止下溢
            right = mid - 1;
        }
    }
    
    return result;
}

function findRightBound(nums: number[], target: number): number {
    let left = 0;
    let right = nums.length - 1;
    let result = -1;
    
    while (left <= right) {
        const mid = Math.floor(left + (right - left) / 2);
        
        if (nums[mid] === target) {
            result = mid;
            left = mid + 1;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            if (mid === 0) break; // 防止下溢
            right = mid - 1;
        }
    }
    
    return result;
}