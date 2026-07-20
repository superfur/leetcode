impl Solution {
    /// 74. 搜索二维矩阵
    /// 把二维矩阵视作一维有序数组，使用二分查找
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        if matrix.is_empty() || matrix[0].is_empty() {
            return false;
        }

        let n = matrix[0].len();
        let total = matrix.len() * n;
        let mut left = 0usize;
        let mut right = total;

        while left < right {
            let mid = left + (right - left) / 2;
            let (row, col) = (mid / n, mid % n);
            let val = matrix[row][col];

            if val < target {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        left < total && matrix[left / n][left % n] == target
    }
}
