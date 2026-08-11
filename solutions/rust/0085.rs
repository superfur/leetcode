/// 85. 最大矩形
/// 逐行累加直方图高度 heights[j]，对每行 heights 调用单调栈求最大矩形。
pub fn maximal_rectangle(matrix: Vec<Vec<char>>) -> i32 {
    if matrix.is_empty() || matrix[0].is_empty() {
        return 0;
    }
    let cols = matrix[0].len();
    let mut heights: Vec<i32> = vec![0; cols];
    let mut max_area: i32 = 0;
    for row in &matrix {
        for j in 0..cols {
            heights[j] = if row[j] == '1' { heights[j] + 1 } else { 0 };
        }
        let area = largest(&heights);
        if area > max_area {
            max_area = area;
        }
    }
    max_area
}

fn largest(heights: &[i32]) -> i32 {
    let mut extended: Vec<i32> = heights.to_vec();
    extended.push(0); // 哨兵
    let mut stack: Vec<usize> = Vec::new();
    let mut best: i32 = 0;
    for i in 0..extended.len() {
        let h = extended[i];
        while let Some(&top) = stack.last() {
            if extended[top] <= h {
                break;
            }
            stack.pop();
            let height = extended[top];
            let width = if stack.is_empty() {
                i as i32
            } else {
                (i - stack.last().unwrap() - 1) as i32
            };
            let area = height * width;
            if area > best {
                best = area;
            }
        }
        stack.push(i);
    }
    best
}

impl Solution {
    pub fn maximal_rectangle(matrix: Vec<Vec<char>>) -> i32 {
        maximal_rectangle(matrix)
    }
}