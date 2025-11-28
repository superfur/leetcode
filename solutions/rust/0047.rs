impl Solution {
    /*
     * 全排列 II - 回溯算法（处理重复元素）
     * 
     * 时间复杂度: O(n! * n)，其中 n 是数组长度
     *   - 虽然有重复元素，但最坏情况下仍然是 n! 种排列
     *   - 每种排列需要 O(n) 时间复制
     * 空间复杂度: O(n)，递归栈深度为 n，临时排列长度为 n
     * 
     * 思路:
     * 1. 先对数组排序，使相同元素相邻
     * 2. 使用回溯算法生成所有排列
     * 3. 维护一个当前排列和一个标记数组（记录已使用的元素）
     * 4. 在回溯过程中，如果当前元素与前一个元素相同，且前一个元素未被使用，则跳过
     *    这样可以避免生成重复的排列
     * 5. 当排列长度等于原数组长度时，保存结果
     * 6. 回溯时恢复状态（移除元素，标记为未使用）
     * ·
     * 去重原理:
     * - 对于相同元素 [a, a, b]，如果第一个 a 未被使用，第二个 a 被使用
     * - 此时选择第一个 a 会生成与之前相同的排列，所以应该跳过
     * - 只有当相同元素中，前面的元素已被使用时，才可以选择当前元素
     */
    pub fn permute_unique(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut nums = nums;
        // 先排序，使相同元素相邻
        nums.sort();
        
        let mut result: Vec<Vec<i32>> = Vec::new();
        let mut current: Vec<i32> = Vec::new();
        let mut used: Vec<bool> = vec![false; nums.len()];
        
        Self::backtrack(&nums, &mut result, &mut current, &mut used);
        
        result
    }
    
    fn backtrack(
        nums: &[i32],
        result: &mut Vec<Vec<i32>>,
        current: &mut Vec<i32>,
        used: &mut Vec<bool>,
    ) {
        // 如果当前排列长度等于原数组长度，说明找到了一种排列
        if current.len() == nums.len() {
            // 创建副本并添加到结果中
            result.push(current.clone());
            return;
        }
        
        // 尝试每个未使用的元素
        for i in 0..nums.len() {
            // 如果当前元素已被使用，跳过
            if used[i] {
                continue;
            }
            
            // 去重：如果当前元素与前一个元素相同，且前一个元素未被使用，则跳过
            // 这样可以避免生成重复的排列
            if i > 0 && nums[i] == nums[i - 1] && !used[i - 1] {
                continue;
            }
            
            // 选择当前元素
            used[i] = true;
            current.push(nums[i]);
            
            // 递归尝试下一个位置
            Self::backtrack(nums, result, current, used);
            
            // 回溯：撤销选择
            current.pop();
            used[i] = false;
        }
    }
}