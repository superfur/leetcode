/**
 * 91. 解码方法
 * 动态规划：dp[i] 表示 s.slice(0, i) 的解码方法数。
 * 单字符有效（非 '0'）时可从 dp[i-1] 转移；
 * 双字符在 10~26 之间时可从 dp[i-2] 转移。
 * 用两个变量滚动即可，无需数组。
 */
function numDecodings(s: string): number {
    const n = s.length;
    let prev2 = 1;
    let prev1 = s[0] !== '0' ? 1 : 0;

    for (let i = 2; i <= n; i++) {
        let cur = 0;
        if (s[i - 1] !== '0') cur += prev1;
        const twoDigit = Number(s.slice(i - 2, i));
        if (twoDigit >= 10 && twoDigit <= 26) cur += prev2;
        prev2 = prev1;
        prev1 = cur;
    }

    return prev1;
}

export default numDecodings;
