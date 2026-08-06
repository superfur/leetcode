public class Solution {
    /**
     * 84. 柱状图中最大的矩形
     * 单调递增栈：栈中保存索引，对应高度严格递增。
     * 遇到 heights[i] < heights[stack.top] 时弹栈并以弹出的高度为基准计算面积：
     *   width = i - stack[len-2] - 1（栈空则为 i）。
     * 末尾追加 0 哨兵确保所有柱子被清算。
     */
    public int largestRectangleArea(int[] heights) {
        java.util.Deque<Integer> stack = new java.util.ArrayDeque<>();
        int maxArea = 0;
        int n = heights.length;
        for (int i = 0; i <= n; i++) {
            int h = (i == n) ? 0 : heights[i];
            while (!stack.isEmpty() && heights[stack.peek()] > h) {
                int top = stack.pop();
                int height = heights[top];
                int width = stack.isEmpty() ? i : i - stack.peek() - 1;
                maxArea = Math.max(maxArea, height * width);
            }
            stack.push(i);
        }
        return maxArea;
    }
}