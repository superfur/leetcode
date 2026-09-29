/**
 * 120. 三角形最小路径和
 * 自底向上一维滚动 DP：dp[j] 表示从当前行第 j 个位置走到底部的最小路径和。
 * 从倒数第二行开始，dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
 * （dp[j] 是正下方，dp[j+1] 是右下方，取较小的再加上当前值），
 * 一路滚动到第 0 行，dp[0] 就是答案。
 */
function minimumTotal(triangle: number[][]): number {
    const dp = [...triangle[triangle.length - 1]];
    for (let i = triangle.length - 2; i >= 0; i--) {
        for (let j = 0; j < triangle[i].length; j++) {
            dp[j] = triangle[i][j] + Math.min(dp[j], dp[j + 1]);
        }
    }
    return dp[0];
}

export default minimumTotal;
