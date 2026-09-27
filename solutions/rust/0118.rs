impl Solution {
    /// 118. 杨辉三角
    /// 逐行生成：每行首尾都是 1，中间第 j 个数等于上一行第 j-1 和第 j 个数之和。
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        let n = num_rows as usize;
        let mut result: Vec<Vec<i32>> = Vec::with_capacity(n);
        for i in 0..n {
            let mut row = vec![1; i + 1];
            for j in 1..i {
                row[j] = result[i - 1][j - 1] + result[i - 1][j];
            }
            result.push(row);
        }
        result
    }
}
