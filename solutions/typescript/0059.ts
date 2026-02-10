function generateMatrix(n: number): number[][] {
    const matrix: number[][] = Array.from({ length: n }, () => Array(n).fill(0));

    let top = 0;
    let bottom = n - 1;
    let left = 0;
    let right = n - 1;
    let num = 1;
    const max = n * n;

    while (num <= max) {
        // 向右：填充 top 行
        for (let j = left; j <= right && num <= max; j++) {
            matrix[top][j] = num++;
        }
        top++;

        // 向下：填充 right 列
        for (let i = top; i <= bottom && num <= max; i++) {
            matrix[i][right] = num++;
        }
        right--;

        // 向左：填充 bottom 行
        for (let j = right; j >= left && num <= max; j--) {
            matrix[bottom][j] = num++;
        }
        bottom--;

        // 向上：填充 left 列
        for (let i = bottom; i >= top && num <= max; i--) {
            matrix[i][left] = num++;
        }
        left++;
    }

    return matrix;
}

export default generateMatrix;