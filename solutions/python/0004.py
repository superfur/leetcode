class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        middle = len(merged) // 2
        if len(merged) % 2 == 1:
            return merged[middle]
        else:
            return (merged[middle - 1] + merged[middle]) / 2


