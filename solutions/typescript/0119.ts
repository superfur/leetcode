/**
 * 119. 杨辉三角 II
 * 只用一个长度为 rowIndex+1 的数组原地滚动更新：
 * 每处理一行就从右往左把 row[j] 加上 row[j-1]（右往左是关键，
 * 避免用本行已经更新过的值覆盖还没处理的旧值）。
 */
function getRow(rowIndex: number): number[] {
    const row: number[] = new Array(rowIndex + 1).fill(1);
    for (let i = 1; i <= rowIndex; i++) {
        for (let j = i - 1; j > 0; j--) {
            row[j] += row[j - 1];
        }
    }
    return row;
}

export default getRow;
