function minPathSum(grid: number[][]): number {
    if (!grid || grid.length === 0 || grid[0].length === 0) {
        return 0;
    }
    const m = grid.length;
    const n = grid[0].length;
    const dp: number[] = new Array(n).fill(0);
    dp[0] = grid[0][0];
    for (let j = 1; j < n; j++) {
        dp[j] = dp[j - 1] + grid[0][j];
    }
    for (let i = 1; i < m; i++) {
        dp[0] += grid[i][0];
        for (let j = 1; j < n; j++) {
            dp[j] = Math.min(dp[j], dp[j - 1]) + grid[i][j];
        }
    }
    return dp[n - 1];
}

function 最小路径和(...args: any[]): any {
    if (args.length >= 1 && Array.isArray(args[0])) {
        return minPathSum(args[0]);
    }
    return 0;
}

export default minPathSum;