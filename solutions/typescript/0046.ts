function permute(nums: number[]): number[][] {
    /**
     * 全排列 - 回溯算法
     * 
     * 时间复杂度: O(n! * n)，其中 n 是数组长度
     *   - n! 种排列，每种排列需要 O(n) 时间复制
     * 空间复杂度: O(n)，递归栈深度为 n，临时排列长度为 n
     * 
     * 思路:
     * 1. 使用回溯算法生成所有排列
     * 2. 维护一个当前排列和一个标记数组（记录已使用的元素）
     * 3. 递归尝试每个未使用的元素
     * 4. 当排列长度等于原数组长度时，保存结果
     * 5. 回溯时恢复状态（移除元素，标记为未使用）
     */
    
    const result: number[][] = [];
    const current: number[] = [];
    const used: boolean[] = new Array(nums.length).fill(false);
    
    const backtrack = (): void => {
        // 如果当前排列长度等于原数组长度，说明找到了一种排列
        if (current.length === nums.length) {
            // 创建副本并添加到结果中
            result.push([...current]);
            return;
        }
        
        // 尝试每个未使用的元素
        for (let i = 0; i < nums.length; i++) {
            if (!used[i]) {
                // 选择当前元素
                used[i] = true;
                current.push(nums[i]);
                
                // 递归尝试下一个位置
                backtrack();
                
                // 回溯：撤销选择
                current.pop();
                used[i] = false;
            }
        }
    };
    
    backtrack();
    return result;
};