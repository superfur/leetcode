public class Solution {
    /**
     * 85. 最大矩形
     * 逐行累加直方图高度 heights[j]，对每行 heights 调用单调栈求最大矩形。
     */
    public int maximalRectangle(char[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }
        int cols = matrix[0].length;
        int[] heights = new int[cols];
        int maxArea = 0;
        for (char[] row : matrix) {
            for (int j = 0; j < cols; j++) {
                heights[j] = (row[j] == '1') ? heights[j] + 1 : 0;
            }
            maxArea = Math.max(maxArea, largest(heights));
        }
        return maxArea;
    }

    private int largest(int[] heights) {
        java.util.Deque<Integer> stack = new java.util.ArrayDeque<>();
        int best = 0;
        int n = heights.length;
        for (int i = 0; i <= n; i++) {
            int h = (i == n) ? 0 : heights[i];
            while (!stack.isEmpty() && heights[stack.peek()] > h) {
                int top = stack.pop();
                int height = heights[top];
                int width = stack.isEmpty() ? i : i - stack.peek() - 1;
                best = Math.max(best, height * width);
            }
            stack.push(i);
        }
        return best;
    }
}