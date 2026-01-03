from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        最大子数组和 - Kadane 算法（贪心/动态规划）
        
        时间复杂度: O(n)，只需遍历一次数组
        空间复杂度: O(1)，只使用常数个变量
        
        思路:
        1. 使用贪心思想：如果当前子数组的和为负数，则重新开始
           因为负数会拖累后续元素的和，不如从下一个元素重新开始
        2. 维护两个变量：
           - current_sum: 当前子数组的和
           - max_sum: 全局最大子数组和
        3. 遍历数组，对于每个元素：
           - 如果 current_sum < 0，则重新开始（current_sum = nums[i]）
           - 否则，继续累加（current_sum += nums[i]）
           - 更新 max_sum = max(max_sum, current_sum)
        
        动态规划理解:
        - dp[i] 表示以 nums[i] 结尾的最大子数组和
        - 状态转移：dp[i] = max(nums[i], dp[i-1] + nums[i])
        - 可以优化为只用一个变量，因为只需要前一个状态
        
        示例:
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        i=0: current_sum=-2, max_sum=-2
        i=1: current_sum=1 (重新开始), max_sum=1
        i=2: current_sum=-2, max_sum=1
        i=3: current_sum=4 (重新开始), max_sum=4
        i=4: current_sum=3, max_sum=4
        i=5: current_sum=5, max_sum=5
        i=6: current_sum=6, max_sum=6
        i=7: current_sum=1, max_sum=6
        i=8: current_sum=5, max_sum=6
        返回 6
        """
        # 当前子数组的和
        current_sum = nums[0]
        # 全局最大子数组和
        max_sum = nums[0]
        
        # 从第二个元素开始遍历
        for i in range(1, len(nums)):
            # 如果当前子数组和为负数，则重新开始
            # 否则继续累加
            if current_sum < 0:
                current_sum = nums[i]
            else:
                current_sum += nums[i]
            
            # 更新全局最大值
            max_sum = max(max_sum, current_sum)
        
        return max_sum