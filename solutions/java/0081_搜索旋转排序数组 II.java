public class Solution {
    /**
     * 81. 搜索旋转排序数组 II
     * 允许重复的二分：nums[mid] == nums[right] 时无法判断哪半有序，
     * 退化为 right--。最坏 O(n)，平均 O(log n)。
     */
    public boolean search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        while (left <= right) {
            int mid = (left + right) >>> 1;
            if (nums[mid] == target) return true;
            if (nums[mid] == nums[right]) {
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
}