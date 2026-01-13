import java.util.*;

class Solution {
    /**
     * 螺旋矩阵 - 边界模拟法
     * 
     * 时间复杂度: O(m * n)，其中 m 是行数，n 是列数
     * 空间复杂度: O(1)，除了结果数组外只使用常数个变量
     * 
     * 思路:
     * 1. 定义四个边界：top, bottom, left, right
     * 2. 按照 右->下->左->上 的顺序遍历
     * 3. 每完成一个方向，更新对应的边界
     * 4. 当 top > bottom 或 left > right 时停止
     * 
     * 遍历顺序:
     * - 向右：从 left 到 right，遍历 top 行
     * - 向下：从 top+1 到 bottom，遍历 right 列
     * - 向左：从 right-1 到 left，遍历 bottom 行（逆序）
     * - 向上：从 bottom-1 到 top+1，遍历 left 列（逆序）
     * 
     * 示例:
     * matrix = [[1,2,3],[4,5,6],[7,8,9]]
     * 第一轮：
     *   - 向右：[1,2,3]
     *   - 向下：[6,9]
     *   - 向左：[8,7]
     *   - 向上：[4]
     * 第二轮：
     *   - 向右：[5]
     * 输出：[1,2,3,6,9,8,7,4,5]
     */
    public List<Integer> spiralOrder(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return new ArrayList<>();
        }
        
        int m = matrix.length;
        int n = matrix[0].length;
        List<Integer> result = new ArrayList<>();
        
        // 定义四个边界
        int top = 0;
        int bottom = m - 1;
        int left = 0;
        int right = n - 1;
        
        while (top <= bottom && left <= right) {
            // 向右：遍历 top 行，从 left 到 right
            for (int j = left; j <= right; j++) {
                result.add(matrix[top][j]);
            }
            top++;
            
            // 向下：遍历 right 列，从 top 到 bottom
            // 需要检查是否还有行可以遍历
            if (top > bottom) {
                break;
            }
            for (int i = top; i <= bottom; i++) {
                result.add(matrix[i][right]);
            }
            right--;
            
            // 向左：遍历 bottom 行，从 right 到 left（逆序）
            // 需要检查是否还有行可以遍历，并且 right >= left
            if (top > bottom || left > right) {
                break;
            }
            for (int j = right; j >= left; j--) {
                result.add(matrix[bottom][j]);
            }
            bottom--;
            
            // 向上：遍历 left 列，从 bottom 到 top（逆序）
            // 需要检查是否还有列可以遍历，并且 bottom >= top
            if (left > right || top > bottom) {
                break;
            }
            for (int i = bottom; i >= top; i--) {
                result.add(matrix[i][left]);
            }
            left++;
        }
        
        return result;
    }
}