use std::collections::HashMap;

fn gcd(mut a: i32, mut b: i32) -> i32 {
    a = a.abs();
    b = b.abs();
    while b != 0 {
        let t = a % b;
        a = b;
        b = t;
    }
    a
}

impl Solution {
    /// 149. 直线上最多的点数
    /// 固定一个点 i 作为「基准点」，统计它与后面每个点 j 连线的斜率，斜率相同的点与 i 共线。
    /// 为了避免浮点误差，不直接除，而是把方向向量 (dx, dy) 除以 gcd 约成最简，
    /// 再统一符号（dx < 0，或 dx == 0 且 dy < 0 时整体取反），同一斜率就对应唯一的 (dx, dy)。
    /// 只需统计 j > i 的点：共线的点集里编号最小的点作基准时就能数全，不用重复计算。
    /// 基准点自己算一个，所以答案为 max(同斜率计数) + 1。
    /// 时间 O(n^2 log C)，空间 O(n)。
    pub fn max_points(points: Vec<Vec<i32>>) -> i32 {
        let n = points.len();
        if n <= 2 {
            return n as i32;
        }
        let mut best = 1usize;
        for i in 0..n {
            if best >= n - i {
                break; // 剩下的点不够超过当前答案了
            }
            let mut slopes: HashMap<(i32, i32), usize> = HashMap::with_capacity(n - i);
            for j in i + 1..n {
                let mut dx = points[j][0] - points[i][0];
                let mut dy = points[j][1] - points[i][1];
                let g = gcd(dx, dy);
                dx /= g;
                dy /= g;
                if dx < 0 || (dx == 0 && dy < 0) {
                    dx = -dx;
                    dy = -dy;
                }
                let cnt = slopes.entry((dx, dy)).or_insert(0);
                *cnt += 1;
                best = best.max(*cnt + 1);
            }
        }
        best as i32
    }
}
