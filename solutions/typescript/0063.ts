/**
 * 不同路径 II：m×n 网格中有障碍物(1表示)，从左上角到右下角的路径数。
 * DP 一维：dp[j] = 0(有障碍) 或 dp[j] + dp[j-1](无障碍)。时间 O(mn)，空间 O(n)。
 */
function uniquePathsWithObstacles(obstacleGrid: number[][]): number {
    if (!obstacleGrid || obstacleGrid.length === 0 || obstacleGrid[0].length === 0) {
        return 0;
    }

    const m = obstacleGrid.length;
    const n = obstacleGrid[0].length;
    const dp: number[] = new Array(n).fill(0);

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (obstacleGrid[i][j] === 1) {
                dp[j] = 0;
            } else if (j === 0) {
                dp[j] = (i === 0 || dp[j] === 1) ? 1 : 0;
            } else {
                dp[j] = dp[j] + dp[j - 1];
            }
        }
    }

    return dp[n - 1];
}

function 不同路径Ii(...args: any[]): any {
    const grid = args[0] as number[][];
    return uniquePathsWithObstacles(grid);
}

export default 不同路径Ii;
