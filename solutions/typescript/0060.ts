/**
 * 排列序列 - 返回由 1..n 组成的所有排列中字典序第 k 个（1-indexed）
 *
 * 时间复杂度: O(n²)，每次从数组中 remove 为 O(n)
 * 空间复杂度: O(n)
 */
function getPermutation(n: number, k: number): string {
    if (n <= 0 || k <= 0) return "";

    const fact: number[] = [1];
    for (let i = 1; i <= n; i++) fact[i] = fact[i - 1] * i;
    if (k > fact[n]) return "";

    const nums: number[] = [];
    for (let i = 1; i <= n; i++) nums.push(i);

    let k0 = k - 1; // 转为 0-index
    const res: string[] = [];

    for (let i = n; i >= 1; i--) {
        const f = fact[i - 1];
        const idx = Math.floor(k0 / f);
        res.push(String(nums[idx]));
        nums.splice(idx, 1);
        k0 %= f;
    }

    return res.join("");
}

function 排列序列(...args: any[]): any {
    const n = args[0] as number;
    const k = args[1] as number;
    return getPermutation(n, k);
}

export default 排列序列;
