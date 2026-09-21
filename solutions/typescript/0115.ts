/**
 * 115. 不同的子序列
 * 一维滚动 DP：dp[j] 表示当前已处理的 s 前缀中，
 * 有多少种方式能选出 t 的前 j 个字符作为子序列。
 * dp[0] 恒为 1（空串永远只有一种"什么都不选"的方式）。
 * s[i-1] === t[j-1] 时，dp[j] 既可以不用当前这个 s 字符
 * （沿用旧的 dp[j]），也可以用它去匹配 t[j-1]（累加旧的 dp[j-1]），
 * 所以要按 j 从大到小更新，避免用本轮已经更新过的值。
 */
function numDistinct(s: string, t: string): number {
    const n = t.length;
    const dp: number[] = new Array(n + 1).fill(0);
    dp[0] = 1;
    for (const ch of s) {
        for (let j = n; j >= 1; j--) {
            if (ch === t[j - 1]) {
                dp[j] += dp[j - 1];
            }
        }
    }
    return dp[n];
}

export default numDistinct;
