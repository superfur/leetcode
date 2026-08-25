/**
 * 93. 复原 IP 地址
 * 回溯：依次切出长度 1~3 的一段作为一个 IP 段，
 * 段值需在 0~255 之间且不能有前导 0（除了单独的 "0"）；
 * 切出 4 段且恰好用完所有字符时才是一个合法答案。
 */
function restoreIpAddresses(s: string): string[] {
    const n = s.length;
    const result: string[] = [];
    const segments: string[] = [];

    const backtrack = (start: number): void => {
        if (segments.length === 4) {
            if (start === n) result.push(segments.join("."));
            return;
        }
        if (n - start > (4 - segments.length) * 3) return;
        for (let length = 1; length <= 3 && start + length <= n; length++) {
            const segment = s.slice(start, start + length);
            if (length > 1 && segment[0] === "0") break;
            if (Number(segment) > 255) break;
            segments.push(segment);
            backtrack(start + length);
            segments.pop();
        }
    };

    backtrack(0);
    return result;
}

export default restoreIpAddresses;
