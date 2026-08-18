/// 89. 格雷编码
/// 经典公式：gray(i) = i ^ (i >> 1)。
pub fn gray_code(n: i32) -> Vec<i32> {
    let size = 1usize << n;
    let mut result: Vec<i32> = Vec::with_capacity(size);
    for i in 0..size as i32 {
        result.push(i ^ (i >> 1));
    }
    result
}

impl Solution {
    pub fn gray_code(n: i32) -> Vec<i32> {
        gray_code(n)
    }
}