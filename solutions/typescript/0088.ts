/**
 * 88. 合并两个有序数组
 * 给定两个非递减数组 nums1 和 nums2，把 nums2 合并到 nums1 上使结果仍非递减。
 * nums1 的长度为 m + n，后 n 位为占位 0。
 * 从后往前双指针：i 指向 nums1 有效末尾，j 指向 nums2 末尾，k 指向 nums1 末尾。
 */
function merge(nums1: number[], m: number, nums2: number[], n: number): void {
    let i = m - 1;
    let j = n - 1;
    let k = m + n - 1;
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

export default merge;