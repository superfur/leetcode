/**
 * 组合总和 II - 回溯算法
 * 找出所有可以使数字和为目标数 target 的不同组合
 * 每个数字在每个组合中只能使用一次，且解集不能包含重复的组合
 * 
 * 算法思路：
 * 1. 先对数组排序，便于处理重复元素
 * 2. 使用回溯算法（DFS）遍历所有可能的组合
 * 3. 每次选择当前数字或跳过，但每个数字只能使用一次
 * 4. 当和等于 target 时，记录当前组合
 * 5. 当和大于 target 时，剪枝返回
 * 6. 通过起始索引和重复元素处理避免重复组合
 * 
 * 时间复杂度：O(2^n)，n 是候选数组长度
 * 空间复杂度：O(target)，递归栈的深度最多为 target
 * 
 * @param candidates - 候选数字数组（可能包含重复元素）
 * @param target - 目标和
 * @returns 所有和为 target 的不同组合
 */
function combinationSum2(candidates: number[], target: number): number[][] {
    // 先排序，便于处理重复元素
    candidates.sort((a, b) => a - b);
    
    const result: number[][] = [];
    const path: number[] = [];
    
    /**
     * 回溯函数
     * @param start - 当前搜索的起始索引，避免重复组合
     * @param currentSum - 当前路径的和
     */
    function backtrack(start: number, currentSum: number): void {
        // 找到一个有效组合
        if (currentSum === target) {
            result.push([...path]); // 复制当前路径
            return;
        }
        
        // 剪枝：当前和已经超过目标值
        if (currentSum > target) {
            return;
        }
        
        // 从 start 开始遍历，避免重复组合
        for (let i = start; i < candidates.length; i++) {
            const num = candidates[i];
            
            // 剪枝优化：如果加上当前数字已经超过目标，后续更大的数字也不用尝试
            if (currentSum + num > target) {
                break; // 由于数组已排序，可以直接 break
            }
            
            // 关键：跳过重复元素，避免产生重复组合
            // 在同一层递归中，如果当前元素与前一个元素相同，则跳过
            // 这样可以避免产生如 [1,2,2] 和 [1,2,2] 这样的重复组合
            if (i > start && candidates[i] === candidates[i - 1]) {
                continue;
            }
            
            // 选择当前数字
            path.push(num);
            
            // 递归：注意这里是 i+1，因为每个数字只能使用一次
            backtrack(i + 1, currentSum + num);
            
            // 撤销选择（回溯）
            path.pop();
        }
    }
    
    // 从索引 0 开始搜索
    backtrack(0, 0);
    
    return result;
};