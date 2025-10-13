impl Solution {
    /// 组合总和 - 回溯算法
    /// 找出所有可以使数字和为目标数 target 的不同组合
    /// 同一个数字可以无限制重复被选取
    /// 
    /// 算法思路：
    /// 1. 使用回溯算法（DFS）遍历所有可能的组合
    /// 2. 每次可以选择当前数字或跳过，选择当前数字时可以重复选择
    /// 3. 当和等于 target 时，记录当前组合
    /// 4. 当和大于 target 时，剪枝返回
    /// 5. 通过起始索引避免重复组合
    /// 
    /// 时间复杂度：O(S)，S 是所有可行解的长度之和
    /// 空间复杂度：O(target)，递归栈的深度最多为 target
    pub fn combination_sum(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let mut result: Vec<Vec<i32>> = Vec::new();
        let mut path: Vec<i32> = Vec::new();
        
        Self::backtrack(&candidates, target, 0, 0, &mut path, &mut result);
        
        result
    }
    
    /// 回溯函数
    /// 
    /// # Arguments
    /// * `candidates` - 候选数字数组
    /// * `target` - 目标和
    /// * `start` - 当前搜索的起始索引，避免重复组合
    /// * `current_sum` - 当前路径的和
    /// * `path` - 当前路径
    /// * `result` - 存储所有有效组合的结果集
    fn backtrack(
        candidates: &Vec<i32>,
        target: i32,
        start: usize,
        current_sum: i32,
        path: &mut Vec<i32>,
        result: &mut Vec<Vec<i32>>,
    ) {
        // 找到一个有效组合
        if current_sum == target {
            result.push(path.clone()); // 克隆当前路径
            return;
        }
        
        // 剪枝：当前和已经超过目标值
        if current_sum > target {
            return;
        }
        
        // 从 start 开始遍历，避免重复组合
        for i in start..candidates.len() {
            let num = candidates[i];
            
            // 剪枝优化：如果加上当前数字已经超过目标，跳过
            if current_sum + num > target {
                continue;
            }
            
            // 选择当前数字
            path.push(num);
            
            // 递归：注意这里是 i 而不是 i+1，因为可以重复使用当前数字
            Self::backtrack(candidates, target, i, current_sum + num, path, result);
            
            // 撤销选择（回溯）
            path.pop();
        }
    }
}