impl Solution {
    /// 缺失的第一个正数 - 原地哈希法
    /// 找出未排序数组中没有出现的最小的正整数
    /// 
    /// 核心思想：
    /// 1. 最小的正整数一定在 [1, n+1] 范围内（n 为数组长度）
    /// 2. 使用原地哈希：将数字 i 放到索引 i-1 的位置
    /// 3. 第一遍：将 1~n 范围内的数字放到正确位置
    /// 4. 第二遍：找到第一个不满足 nums[i] === i+1 的位置
    /// 
    /// 算法步骤：
    /// 1. 遍历数组，对于每个位置 i：
    ///    - 如果 nums[i] 在 [1, n] 范围内，且不在正确位置
    ///    - 将其交换到索引 nums[i]-1 的位置
    ///    - 重复直到当前位置的数字在正确位置或不在范围内
    /// 2. 再次遍历数组，找到第一个 nums[i] !== i+1 的位置
    /// 3. 返回 i+1，如果都正确则返回 n+1
    /// 
    /// 时间复杂度：O(n)，每个元素最多被移动一次
    /// 空间复杂度：O(1)，只使用常数级别额外空间
    pub fn first_missing_positive(nums: Vec<i32>) -> i32 {
        let mut nums = nums;
        let n = nums.len();
        
        // 第一步：将每个数字放到它应该在的位置
        // 数字 i 应该放在索引 i-1 的位置
        let mut i = 0;
        while i < n {
            // 当前数字在有效范围内 [1, n]，且不在正确位置
            // 需要持续交换直到当前位置的数字正确或无效
            let num = nums[i];
            
            if num > 0 && num <= n as i32 {
                let target_index = (num - 1) as usize;
                
                // 目标位置的值与当前值不同（避免死循环）
                if nums[target_index] != num {
                    // 交换 nums[i] 和 nums[target_index]
                    nums.swap(i, target_index);
                    // 不增加 i，继续检查当前位置
                    continue;
                }
            }
            
            i += 1;
        }
        
        // 第二步：找到第一个不满足 nums[i] === i+1 的位置
        for i in 0..n {
            if nums[i] != (i + 1) as i32 {
                return (i + 1) as i32;
            }
        }
        
        // 如果所有位置都正确，说明数组是 [1,2,3,...,n]
        // 缺失的最小正整数是 n+1
        (n + 1) as i32
    }
}