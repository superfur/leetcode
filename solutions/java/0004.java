import java.util.Arrays;

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // 合并两个数组
        int[] merged = new int[nums1.length + nums2.length];
        System.arraycopy(nums1, 0, merged, 0, nums1.length);
        System.arraycopy(nums2, 0, merged, nums1.length, nums2.length);
        
        // 排序合并后的数组
        Arrays.sort(merged);
        
        // 计算中位数
        int middle = merged.length / 2;
        if (merged.length % 2 == 1) {
            return merged[middle];
        } else {
            return (merged[middle - 1] + merged[middle]) / 2.0;
        }
    }
}
