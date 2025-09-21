class Solution {
    public int[] searchRange(int[] nums, int target) {
        if (nums.length == 0) {
            return new int[]{-1, -1};
        }
        
        int left = 0;
        int right = nums.length - 1;
        int leftBound = -1;
        int rightBound = -1;
        
        // 查找左边界
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (nums[mid] == target) {
                leftBound = mid;
                right = mid - 1; // 继续在左半部分搜索
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        // 如果左边界不存在，直接返回
        if (leftBound == -1) {
            return new int[]{-1, -1};
        }
        
        // 重置边界，查找右边界
        left = leftBound;
        right = nums.length - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (nums[mid] == target) {
                rightBound = mid;
                left = mid + 1; // 继续在右半部分搜索
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return new int[]{leftBound, rightBound};
    }
}