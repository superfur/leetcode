/**
 * 90. 子集 II
 * 排序 + 回溯：同一层若 nums[i] === nums[i-1] 则跳过，
 * 保证对相同值只展开一次，避免重复子集。
 */
function subsetsWithDup(nums: number[]): number[][] {
    nums.sort((a, b) => a - b);
    const result: number[][] = [];
    const path: number[] = [];

    const backtrack = (start: number): void => {
        result.push([...path]);
        for (let i = start; i < nums.length; i++) {
            if (i > start && nums[i] === nums[i - 1]) continue;
            path.push(nums[i]);
            backtrack(i + 1);
            path.pop();
        }
    };

    backtrack(0);
    return result;
}

export default subsetsWithDup;