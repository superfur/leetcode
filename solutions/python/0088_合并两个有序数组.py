from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        88. 合并两个有序数组
        从后往前双指针：i 指向 nums1 有效末尾，j 指向 nums2 末尾，
        k 指向 nums1 末尾。每次把较大的放到 k，然后相应指针前移。
        最后 nums2 若有剩余，复制到 nums1 前部。
        不使用额外数组，原地 O(1) 空间。
        """
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


# ---------- helpers ----------
def merge_copy(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
    """非破坏性版本用于本地测试（避免跨用例污染）"""
    nums1 = nums1[:]
    Solution().merge(nums1, m, nums2, n)
    return nums1


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
        ([2, 0], 1, [1], 1, [1, 2]),
        ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
        ([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3, [-1, 0, 0, 1, 2, 2, 3, 3, 3]),
    ]
    for i, (nums1, m, nums2, n, expected) in enumerate(test_cases, 1):
        result = merge_copy(nums1, m, nums2, n)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"测试用例 {i}: {status} "
            f"(nums1={nums1}, m={m}, nums2={nums2}, n={n}, "
            f"got={result}, expected={expected})"
        )