/**
 * 139. 单词拆分
 * dp[i] 表示 s 的前 i 个字符能否被拆成字典里的单词（dp[0] = true）。
 * 对每个 i 枚举「最后一个单词」的起点 j：dp[j] 为真且 s.slice(j, i) 在字典里，则 dp[i] 为真。
 * 字典里最长的单词长度为 maxLen，所以 j 只需要从 i - maxLen 开始往后枚举，
 * 用集合判断单词是否存在。时间 O(n * maxLen * maxLen)。
 */
function wordBreak(s: string, wordDict: string[]): boolean {
    const words = new Set<string>(wordDict);
    let maxLen = 0;
    for (const w of words) maxLen = Math.max(maxLen, w.length);

    const n = s.length;
    const dp: boolean[] = Array(n + 1).fill(false);
    dp[0] = true;
    for (let i = 1; i <= n; i++) {
        for (let j = Math.max(0, i - maxLen); j < i; j++) {
            if (dp[j] && words.has(s.slice(j, i))) {
                dp[i] = true;
                break;
            }
        }
    }
    return dp[n];
}

export default wordBreak;
