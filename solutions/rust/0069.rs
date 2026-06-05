impl Solution {
    pub fn my_sqrt(x: i32) -> i32 {
        if x < 2 {
            return x;
        }
        let (mut left, mut right) = (1i64, (x / 2) as i64);
        while left <= right {
            let mid = (left + right) / 2;
            let sq = mid * mid;
            if sq == x as i64 {
                return mid as i32;
            } else if sq < x as i64 {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        right as i32
    }
}
