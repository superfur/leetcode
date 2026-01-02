class Solution {
    /**
     * 最大子数组和 - Kadane 算法（贪心/动态规划）
     * 
     * 时间复杂度: O(n)，只需遍历一次数组
     * 空间复杂度: O(1)，只使用常数个变量
     * 
     * 思路:
     * 1. 使用贪心思想：如果当前子数组的和为负数，则重新开始
     *    因为负数会拖累后续元素的和，不如从下一个元素重新开始
     * 2. 维护两个变量：
     *    - currentSum: 当前子数组的和
     *    - maxSum: 全局最大子数组和
     * 3. 遍历数组，对于每个元素：
     *    - 如果 currentSum < 0，则重新开始（currentSum = nums[i]）
     *    - 否则，继续累加（currentSum += nums[i]）
     *    - 更新 maxSum = max(maxSum, currentSum)
     * 
     * 动态规划理解:
     * - dp[i] 表示以 nums[i] 结尾的最大子数组和
     * - 状态转移：dp[i] = max(nums[i], dp[i-1] + nums[i])
     * - 可以优化为只用一个变量，因为只需要前一个状态
     * 
     * 示例:
     * nums = [-2,1,-3,4,-1,2,1,-5,4]
     * i=0: currentSum=-2, maxSum=-2
     * i=1: currentSum=1 (重新开始), maxSum=1
     * i=2: currentSum=-2, maxSum=1
     * i=3: currentSum=4 (重新开始), maxSum=4
     * i=4: currentSum=3, maxSum=4
     * i=5: currentSum=5, maxSum=5
     * i=6: currentSum=6, maxSum=6
     * i=7: currentSum=1, maxSum=6
     * i=8: currentSum=5, maxSum=6
     * 返回 6
     */
    public int maxSubArray(int[] nums) {
        // 当前子数组的和
        int currentSum = nums[0];
        // 全局最大子数组和
        int maxSum = nums[0];
        
        // 从第二个元素开始遍历
        for (int i = 1; i < nums.length; i++) {
            // 如果当前子数组和为负数，则重新开始
            // 否则继续累加
            if (currentSum < 0) {
                currentSum = nums[i];
            } else {
                currentSum += nums[i];
            }
            
            // 更新全局最大值
            maxSum = Math.max(maxSum, currentSum);
        }
        
        return maxSum;
    }
}