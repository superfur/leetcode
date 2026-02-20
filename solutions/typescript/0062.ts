/**
 * 不同路径：m×n 网格，从左上角只能向右或向下走，到右下角的路径数。
 * DP: dp[i][j] = dp[i-1][j] + dp[i][j-1]，首行首列为 1。时间 O(mn)，空间 O(n) 可压成一维。
 */
function uniquePaths(m: number, n: number): number {
    const dp: number[] = Array(n).fill(1);

    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            dp[j] += dp[j - 1];
        }
    }

    return dp[n - 1];
}

function 不同路径(...args: any[]): any {
    const m = args[0] as number;
    const n = args[1] as number;
    return uniquePaths(m, n);
}

export default 不同路径;
