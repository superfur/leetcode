impl Solution {
    pub fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {
        let m = matrix.len();
        let n = matrix[0].len();
        let first_row_zero = (0..n).any(|j| matrix[0][j] == 0);
        let first_col_zero = (0..m).any(|i| matrix[i][0] == 0);

        for i in 1..m {
            for j in 1..n {
                if matrix[i][j] == 0 {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        for i in 1..m {
            for j in 1..n {
                if matrix[i][0] == 0 || matrix[0][j] == 0 {
                    matrix[i][j] = 0;
                }
            }
        }

        if first_row_zero {
            for j in 0..n {
                matrix[0][j] = 0;
            }
        }
        if first_col_zero {
            for i in 0..m {
                matrix[i][0] = 0;
            }
        }
    }
}
