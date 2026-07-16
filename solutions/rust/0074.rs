impl Solution {
    /// 74. 搜索二维矩阵
    /// 把二维矩阵视作一维有序数组，使用二分查找
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        if matrix.is_empty() || matrix[0].is_empty() {
            return false;
        }

        let m = matrix.len();
        let n = matrix[0].len();
        let mut left = 0usize;
        let mut right = m * n - 1;

        while left <= right {
            let mid = (left + right) / 2;
            let (row, col) = (mid / n, mid % n);
            let val = matrix[row][col];

            match val.cmp(&target) {
                std::cmp::Ordering::Equal => return true,
                std::cmp::Ordering::Less => left = mid + 1,
                std::cmp::Ordering::Greater => right = mid - 1,
            }
        }

        false
    }
}