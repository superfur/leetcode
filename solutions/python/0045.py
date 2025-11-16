# function jump(nums: number[]): number {
#     const n = nums.length;
#     if (n <= 1) {
#         return 0;
#     }

#     let jumps = 0;
#     let currentEnd = 0;
#     let farthest = 0;

#     for (let i = 0; i < n - 1; i++) {
#         farthest = Math.max(farthest, i + nums[i]);

#         if (i === currentEnd) {
#             jumps++;
#             currentEnd = farthest;

#             if (currentEnd >= n - 1) {
#                 break;
#             }
#         }
#     }

#     return jumps;
# };

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        jumps = 0
        current_end = 0
        farthest = 0
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
                if current_end >= n - 1:
                    break
        return jumps