/**
 * 131. 分割回文串
 * 先用区间 DP 预处理 isPal[i][j]（s[i..j] 是否回文），
 * 再回溯：从位置 start 开始，枚举每个能切出回文前缀 s[start..end] 的位置，
 * 选中后递归处理 end + 1，走到字符串末尾就收集一个方案。
 */
function partition(s: string): string[][] {
    const n = s.length;
    const isPal: boolean[][] = Array.from({ length: n }, () => Array(n).fill(true));
    for (let i = n - 1; i >= 0; i--) {
        for (let j = i + 1; j < n; j++) {
            isPal[i][j] = s[i] === s[j] && isPal[i + 1][j - 1];
        }
    }

    const res: string[][] = [];
    const path: string[] = [];

    const back = (start: number): void => {
        if (start === n) {
            res.push([...path]);
            return;
        }
        for (let end = start; end < n; end++) {
            if (isPal[start][end]) {
                path.push(s.slice(start, end + 1));
                back(end + 1);
                path.pop();
            }
        }
    };

    back(0);
    return res;
}

export default partition;
