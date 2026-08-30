/**
 * 97. 交错字符串
 * 一维滚动 DP：dp[j] 表示 s3 的前 i+j 个字符能否由
 * s1 的前 i 个字符和 s2 的前 j 个字符交错组成（i 随外层循环推进）。
 * 长度不匹配直接返回 false。
 */
function isInterleave(s1: string, s2: string, s3: string): boolean {
    const m = s1.length;
    const n = s2.length;
    if (m + n !== s3.length) return false;

    const dp: boolean[] = new Array(n + 1).fill(false);
    dp[0] = true;
    for (let j = 1; j <= n; j++) {
        dp[j] = dp[j - 1] && s2[j - 1] === s3[j - 1];
    }

    for (let i = 1; i <= m; i++) {
        dp[0] = dp[0] && s1[i - 1] === s3[i - 1];
        for (let j = 1; j <= n; j++) {
            dp[j] = (dp[j] && s1[i - 1] === s3[i + j - 1]) || (dp[j - 1] && s2[j - 1] === s3[i + j - 1]);
        }
    }

    return dp[n];
}

export default isInterleave;
