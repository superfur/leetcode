/**
 * 旋转图像 90 度（顺时针）- 原地操作
 * 
 * 时间复杂度: O(n^2)，每个元素最多参与常数次交换
 * 空间复杂度: O(1)，只使用少量临时变量，满足原地旋转要求
 * 
 * 思路（两步法，均为原地操作）:
 * 1. 转置矩阵：matrix[i][j] 与 matrix[j][i] 交换（仅 i < j 时交换，避免重复）
 * 2. 每一行左右翻转：matrix[i][j] 与 matrix[i][n-1-j] 交换
 * 
 * 证明:
 * - 原始坐标 (row, col) 先转置到 (col, row)，再左右翻转到 (col, n-1-row)
 * - 这正是顺时针旋转 90 度后的位置
 * 
 * Do not return anything, modify matrix in-place instead.
 */
 function rotate(matrix: number[][]): void {
    const n = matrix.length;
    if (n === 0) return;
    
    // 1. 转置矩阵：沿主对角线交换
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
        }
    }
    
    // 2. 每一行左右翻转
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < Math.floor(n / 2); j++) {
            [matrix[i][j], matrix[i][n - 1 - j]] = [matrix[i][n - 1 - j], matrix[i][j]];
        }
    }
}