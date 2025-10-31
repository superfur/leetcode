impl Solution {
    /// 接雨水 - 双指针法
    /// 计算柱子排列后能接多少雨水
    /// 
    /// 核心思想：
    /// 1. 对于位置 i，能接的水量 = min(左边最大高度, 右边最大高度) - height[i]
    /// 2. 使用双指针从两端向中间移动
    /// 3. 维护 left_max 和 right_max
    /// 4. 如果 left_max < right_max，说明左边是瓶颈，处理左边
    /// 5. 否则右边是瓶颈，处理右边
    /// 
    /// 算法步骤：
    /// 1. 初始化左右指针 left=0, right=n-1
    /// 2. 初始化 left_max=0, right_max=0 和结果 result=0
    /// 3. 当 left < right 时：
    ///    - 如果 height[left] < height[right]：
    ///      * 如果 height[left] >= left_max，更新 left_max
    ///      * 否则累加 left_max - height[left] 到结果
    ///      * left++
    ///    - 否则：
    ///      * 如果 height[right] >= right_max，更新 right_max
    ///      * 否则累加 right_max - height[right] 到结果
    ///      * right--
    /// 4. 返回结果
    /// 
    /// 时间复杂度：O(n)，一次遍历
    /// 空间复杂度：O(1)，只使用常数级别额外空间
    pub fn trap(height: Vec<i32>) -> i32 {
        let n = height.len();
        if n == 0 {
            return 0;
        }
        
        let mut left = 0;           // 左指针
        let mut right = n - 1;      // 右指针
        let mut left_max = 0;       // 左边最大高度
        let mut right_max = 0;      // 右边最大高度
        let mut result = 0;         // 接水总量
        
        // 双指针从两端向中间移动
        while left < right {
            // 左边柱子较矮，左边是瓶颈
            if height[left] < height[right] {
                // 如果当前柱子高于或等于左边最大高度，更新最大高度
                if height[left] >= left_max {
                    left_max = height[left];
                } else {
                    // 否则可以接水：left_max - height[left]
                    result += left_max - height[left];
                }
                left += 1;
            } else {
                // 右边柱子较矮或相等，右边是瓶颈
                // 如果当前柱子高于或等于右边最大高度，更新最大高度
                if height[right] >= right_max {
                    right_max = height[right];
                } else {
                    // 否则可以接水：right_max - height[right]
                    result += right_max - height[right];
                }
                right -= 1;
            }
        }
        
        result
    }
}