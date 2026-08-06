/**
 * 84. 柱状图中最大的矩形
 * 给定 n 个非负整数表示柱状图柱子高度（宽为 1），求能勾勒出的最大矩形面积。
 * 单调递增栈：栈中保存索引，对应高度严格递增。
 * 遇到 heights[i] < heights[stack.top] 时弹栈并以弹出的高度为基准计算面积：
 *   width = i - stack[top-1] - 1（栈空则为 i）。
 * 末尾追加 0 哨兵确保所有柱子被清算。
 */
function largestRectangleArea(heights: number[]): number {
    const stack: number[] = [];
    let maxArea = 0;
    const extended = heights.concat([0]);
    for (let i = 0; i < extended.length; i++) {
        while (stack.length > 0 && extended[stack[stack.length - 1]] > extended[i]) {
            const top = stack.pop()!;
            const h = extended[top];
            const w = stack.length === 0 ? i : i - stack[stack.length - 1] - 1;
            maxArea = Math.max(maxArea, h * w);
        }
        stack.push(i);
    }
    return maxArea;
}

export default largestRectangleArea;