/**
 * 89. 格雷编码
 * 给定 n，返回任一有效的 n 位格雷码序列。
 * 经典公式：gray(i) = i ^ (i >> 1)。生成的序列天然满足：
 *   1) 长度为 2^n；2) 首项为 0；3) 相邻项仅 1 位不同；4) 首尾仅 1 位不同。
 */
function grayCode(n: number): number[] {
    const result: number[] = [];
    for (let i = 0; i < 1 << n; i++) {
        result.push(i ^ (i >> 1));
    }
    return result;
}

export default grayCode;