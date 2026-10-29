/**
 * 140. 单词拆分 II
 * 记忆化回溯：dfs(start) 返回后缀 s[start..] 的所有拆分句子。
 * 枚举第一个单词 s.slice(start, end)（长度不超过字典最长单词），在字典里就把它拼到 dfs(end) 的每个句子前面；
 * start === n 时返回 [""]，表示「恰好拆完」，拼接时据此决定要不要加空格。
 * 按起点缓存结果，相同的后缀不会被重复展开。
 */
function wordBreak(s: string, wordDict: string[]): string[] {
    const words = new Set<string>(wordDict);
    let maxLen = 0;
    for (const w of words) maxLen = Math.max(maxLen, w.length);
    const n = s.length;
    const memo = new Map<number, string[]>();

    const dfs = (start: number): string[] => {
        if (start === n) return [""];
        const cached = memo.get(start);
        if (cached) return cached;

        const res: string[] = [];
        for (let end = start + 1; end <= Math.min(n, start + maxLen); end++) {
            const word = s.slice(start, end);
            if (words.has(word)) {
                for (const tail of dfs(end)) {
                    res.push(tail === "" ? word : word + " " + tail);
                }
            }
        }
        memo.set(start, res);
        return res;
    };

    return dfs(0);
}

export default wordBreak;
