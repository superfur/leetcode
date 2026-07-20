/**
 * 76. 最小覆盖子串
 */
function minWindow(s: string, t: string): string {
    const need: Record<string, number> = {};
    for (const ch of t) {
        need[ch] = (need[ch] ?? 0) + 1;
    }

    const required = Object.keys(need).length;
    let left = 0;
    let formed = 0;
    let bestLeft = 0;
    let bestLength = Infinity;
    const windowCount: Record<string, number> = {};

    for (let right = 0; right < s.length; right++) {
        const c = s[right];
        windowCount[c] = (windowCount[c] ?? 0) + 1;

        if (need[c] !== undefined && windowCount[c] === need[c]) {
            formed++;
        }

        while (formed === required && left <= right) {
            const currentLength = right - left + 1;
            if (currentLength < bestLength) {
                bestLength = currentLength;
                bestLeft = left;
            }

            const leftChar = s[left];
            windowCount[leftChar]--;
            if (need[leftChar] !== undefined && windowCount[leftChar] < need[leftChar]) {
                formed--;
            }
            left++;
        }
    }

    return bestLength === Infinity ? '' : s.slice(bestLeft, bestLeft + bestLength);
}

export default minWindow;
