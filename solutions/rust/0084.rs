/// 84. 柱状图中最大的矩形
/// 单调递增栈：栈中保存索引，对应高度严格递增。
/// 遇到 heights[i] < heights[stack.top] 时弹栈并以弹出的高度为基准计算面积：
///   width = i - stack[stack.len()-1] - 1（栈空则为 i）。
/// 末尾追加 0 哨兵确保所有柱子被清算。
pub fn largest_rectangle_area(heights: Vec<i32>) -> i32 {
    let n = heights.len();
    let mut extended: Vec<i32> = heights.clone();
    extended.push(0); // 哨兵

    let mut stack: Vec<usize> = Vec::new();
    let mut max_area: i32 = 0;

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
            if area > max_area {
                max_area = area;
            }
        }
        stack.push(i);
    }
    let _ = n;
    max_area
}

impl Solution {
    pub fn largest_rectangle_area(heights: Vec<i32>) -> i32 {
        largest_rectangle_area(heights)
    }
}