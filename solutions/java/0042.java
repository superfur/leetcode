class Solution {
    /**
     * 接雨水 - 双指针法
     * 计算柱子排列后能接多少雨水
     * 
     * 核心思想：
     * 1. 对于位置 i，能接的水量 = min(左边最大高度, 右边最大高度) - height[i]
     * 2. 使用双指针从两端向中间移动
     * 3. 维护 leftMax 和 rightMax
     * 4. 如果 leftMax < rightMax，说明左边是瓶颈，处理左边
     * 5. 否则右边是瓶颈，处理右边
     * 
     * 算法步骤：
     * 1. 初始化左右指针 left=0, right=n-1
     * 2. 初始化 leftMax=0, rightMax=0 和结果 result=0
     * 3. 当 left < right 时：
     *    - 如果 height[left] < height[right]：
     *      * 如果 height[left] >= leftMax，更新 leftMax
     *      * 否则累加 leftMax - height[left] 到结果
     *      * left++
     *    - 否则：
     *      * 如果 height[right] >= rightMax，更新 rightMax
     *      * 否则累加 rightMax - height[right] 到结果
     *      * right--
     * 4. 返回结果
     * 
     * 时间复杂度：O(n)，一次遍历
     * 空间复杂度：O(1)，只使用常数级别额外空间
     * 
     * @param height 柱子高度数组
     * @return 能接的雨水总量
     */
    public int trap(int[] height) {
        int n = height.length;
        if (n == 0) {
            return 0;
        }
        
        int left = 0;           // 左指针
        int right = n - 1;      // 右指针
        int leftMax = 0;        // 左边最大高度
        int rightMax = 0;       // 右边最大高度
        int result = 0;         // 接水总量
        
        // 双指针从两端向中间移动
        while (left < right) {
            // 左边柱子较矮，左边是瓶颈
            if (height[left] < height[right]) {
                // 如果当前柱子高于或等于左边最大高度，更新最大高度
                if (height[left] >= leftMax) {
                    leftMax = height[left];
                } else {
                    // 否则可以接水：leftMax - height[left]
                    result += leftMax - height[left];
                }
                left++;
            } else {
                // 右边柱子较矮或相等，右边是瓶颈
                // 如果当前柱子高于或等于右边最大高度，更新最大高度
                if (height[right] >= rightMax) {
                    rightMax = height[right];
                } else {
                    // 否则可以接水：rightMax - height[right]
                    result += rightMax - height[right];
                }
                right--;
            }
        }
        
        return result;
    }
}