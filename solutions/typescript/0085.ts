/**
 * 85. 最大矩形
 * 给定仅含 '0' 和 '1' 的二维二进制矩阵，找出只包含 '1' 的最大矩形面积。
 * 逐行累加直方图高度 heights[j] = 当前位置及上方连续 1 的数量，
 * 对每行 heights 调用 84 题单调栈解法。
 */
function maximalRectangle(matrix: string[][]): number {
    if (matrix.length === 0 || matrix[0].length === 0) return 0;
    const cols = matrix[0].length;
    const heights = new Array(cols).fill(0);
    let maxArea = 0;
    for (const row of matrix) {
        for (let j = 0; j < cols; j++) {
            heights[j] = row[j] === "1" ? heights[j] + 1 : 0;
        }
        maxArea = Math.max(maxArea, largest(heights));
    }
    return maxArea;
}

function largest(heights: number[]): number {
    const stack: number[] = [];
    let best = 0;
    const extended = heights.concat([0]);
    for (let i = 0; i < extended.length; i++) {
        while (stack.length > 0 && extended[stack[stack.length - 1]] > extended[i]) {
            const top = stack.pop()!;
            const h = extended[top];
            const w = stack.length === 0 ? i : i - stack[stack.length - 1] - 1;
            best = Math.max(best, h * w);
        }
        stack.push(i);
    }
    return best;
}

export default maximalRectangle;