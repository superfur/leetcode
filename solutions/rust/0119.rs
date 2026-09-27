impl Solution {
    /// 119. 杨辉三角 II
    /// 只用一个长度为 row_index+1 的数组原地滚动更新：
    /// 每处理一行就从右往左把 row[j] 加上 row[j-1]（右往左是关键，
    /// 避免用本行已经更新过的值覆盖还没处理的旧值）。
    pub fn get_row(row_index: i32) -> Vec<i32> {
        let n = row_index as usize;
        let mut row = vec![1; n + 1];
        for i in 1..=n {
            for j in (1..i).rev() {
                row[j] += row[j - 1];
            }
        }
        row
    }
}
