/**
 * 118. 杨辉三角
 * 逐行生成：每行首尾都是 1，中间第 j 个数等于上一行第 j-1 和第 j 个数之和。
 */
function generate(numRows: number): number[][] {
    const result: number[][] = [];
    for (let i = 0; i < numRows; i++) {
        const row = new Array(i + 1).fill(1);
        for (let j = 1; j < i; j++) {
            row[j] = result[i - 1][j - 1] + result[i - 1][j];
        }
        result.push(row);
    }
    return result;
}

export default generate;
