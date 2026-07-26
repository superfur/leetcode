public class Solution {
    /**
     * 80. 删除有序数组中的重复项 II
     * 快慢双指针：每个元素至多出现两次。
     * 通用判断：slow < k || nums[fast] != nums[slow - k]（k=2）。
     */
    public int removeDuplicates(int[] nums) {
        int k = 2;
        int slow = 0;
        for (int fast = 0; fast < nums.length; fast++) {
            if (slow < k || nums[fast] != nums[slow - k]) {
                nums[slow] = nums[fast];
                slow++;
            }
        }
        return slow;
    }
}