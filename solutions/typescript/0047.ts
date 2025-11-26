function permuteUnique(nums: number[]): number[][] {
    /**
     * 全排列 II - 回溯算法 + 剪枝去重
     * 
     * 时间复杂度: O(n! * n)，最坏情况下所有元素不同
     * 空间复杂度: O(n)，递归栈深度 + 临时排列
     * 
     * 思路:
     * 1. 先排序，让相同元素相邻
     * 2. 回溯生成排列，使用 used 数组标记已选元素
     * 3. 剪枝条件：当前元素与前一个相同，且前一个未被使用时跳过
     *    - 这确保了相同元素只能按顺序选取，避免重复排列
     */
    
    // 排序使相同元素相邻，便于去重
    nums.sort((a, b) => a - b);
    
    const result: number[][] = [];
    const current: number[] = [];
    const used: boolean[] = new Array(nums.length).fill(false);
    
    const backtrack = (): void => {
        // 找到一种完整排列
        if (current.length === nums.length) {
            result.push([...current]);
            return;
        }
        
        for (let i = 0; i < nums.length; i++) {
            // 已使用的元素跳过
            if (used[i]) continue;
            
            // 剪枝：当前元素与前一个相同，且前一个未使用时跳过
            // 目的是保证相同元素按原数组顺序选取，避免重复
            if (i > 0 && nums[i] === nums[i - 1] && !used[i - 1]) continue;
            
            // 选择当前元素
            used[i] = true;
            current.push(nums[i]);
            
            backtrack();
            
            // 回溯
            current.pop();
            used[i] = false;
        }
    };
    
    backtrack();
    return result;
};