public class Solution {
    /**
     * 88. 合并两个有序数组
     * 从后往前双指针：i 指向 nums1 有效末尾，j 指向 nums2 末尾，
     * k 指向 nums1 末尾。把较大的放到 k，相应指针前移。
     * 最后 nums2 若有剩余，复制到 nums1 前部。
     */
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m - 1;
        int j = n - 1;
        int k = m + n - 1;
        while (i >= 0 && j >= 0) {
            if (nums1[i] >= nums2[j]) {
                nums1[k] = nums1[i];
                i--;
            } else {
                nums1[k] = nums2[j];
                j--;
            }
            k--;
        }
        while (j >= 0) {
            nums1[k] = nums2[j];
            j--;
            k--;
        }
    }
}