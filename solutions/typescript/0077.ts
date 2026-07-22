/**
 * 77. 组合
 * 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
 */
function combine(n: number, k: number): number[][] {
    const result: number[][] = [];
    const path: number[] = [];

    const dfs = (start: number): void => {
        if (path.length === k) {
            result.push([...path]);
            return;
        }
        // 剪枝: i 最大值 = n - (k - path.length) + 1，否则剩余元素不足
        const upper = n - (k - path.length) + 1;
        for (let i = start; i <= upper; i++) {
            path.push(i);
            dfs(i + 1);
            path.pop();
        }
    };

    dfs(1);
    return result;
}

export default combine;
