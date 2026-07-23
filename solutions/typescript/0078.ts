/**
 * 78. 子集
 * 给定一个不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
 * 解集不能包含重复子集，可以按任意顺序返回。
 */
function subsets(nums: number[]): number[][] {
    const result: number[][] = [];
    const path: number[] = [];

    const dfs = (start: number): void => {
        result.push([...path]);
        for (let i = start; i < nums.length; i++) {
            path.push(nums[i]);
            dfs(i + 1);
            path.pop();
        }
    };

    dfs(0);
    return result;
}

export default subsets;