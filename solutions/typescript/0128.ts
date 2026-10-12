/**
 * 128. 最长连续序列
 * 哈希集合去重，只从「序列起点」（x - 1 不在集合里）出发往后数 x+1, x+2, ...，
 * 每个数最多被数一次，所以整体 O(n)。
 */
function longestConsecutive(nums: number[]): number {
    const set = new Set<number>(nums);
    let best = 0;
    for (const x of set) {
        if (set.has(x - 1)) continue;
        let end = x;
        while (set.has(end + 1)) end++;
        best = Math.max(best, end - x + 1);
    }
    return best;
}

export default longestConsecutive;
