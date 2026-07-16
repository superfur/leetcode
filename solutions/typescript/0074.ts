/**
 * 74. 搜索二维矩阵
 * 把二维矩阵视作一维有序数组，使用二分查找
 */
function searchMatrix(matrix: number[][], target: number): boolean {
    if (matrix.length === 0 || matrix[0].length === 0) {
        return false;
    }

    const m = matrix.length;
    const n = matrix[0].length;
    let left = 0;
    let right = m * n - 1;

    while (left <= right) {
        const mid = (left + right) >>> 1;
        const row = Math.floor(mid / n);
        const col = mid % n;
        const val = matrix[row][col];

        if (val === target) {
            return true;
        } else if (val < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return false;
}

export default searchMatrix;