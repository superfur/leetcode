/**
 * 87. 扰乱字符串
 * 给定两个等长字符串，判断 s2 是否为 s1 的扰乱字符串。
 * 回溯枚举分割点 i：要么 s1[:i]/s1[i:] 与 s2[:i]/s2[i:] 同步扰乱，
 * 要么 s1[:i]/s1[i:] 与 s2[n-i:]/s2[:n-i]（交换）同步扰乱。
 * 剪枝：字符计数不等直接返回 false；用 Map 记忆化。
 */
function isScramble(s1: string, s2: string): boolean {
    const memo = new Map<string, boolean>();
    const key = (a: string, b: string) => `${a}#${b}`;

    function dfs(a: string, b: string): boolean {
        const k = key(a, b);
        if (memo.has(k)) return memo.get(k)!;
        if (a === b) {
            memo.set(k, true);
            return true;
        }
        // 字符计数剪枝（26 个小写字母）
        const cnt = new Array(26).fill(0);
        for (let i = 0; i < a.length; i++) {
            cnt[a.charCodeAt(i) - 97]++;
            cnt[b.charCodeAt(i) - 97]--;
        }
        if (cnt.some((x) => x !== 0)) {
            memo.set(k, false);
            return false;
        }
        const n = a.length;
        for (let i = 1; i < n; i++) {
            // 不交换
            if (dfs(a.slice(0, i), b.slice(0, i)) && dfs(a.slice(i), b.slice(i))) {
                memo.set(k, true);
                return true;
            }
            // 交换
            if (dfs(a.slice(0, i), b.slice(n - i)) && dfs(a.slice(i), b.slice(0, n - i))) {
                memo.set(k, true);
                return true;
            }
        }
        memo.set(k, false);
        return false;
    }

    return dfs(s1, s2);
}

export default isScramble;