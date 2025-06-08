impl Solution {
    fn reverse(x: i32) -> i32 {
        let mut x = x;
        let mut result: i64 = 0;  // 使用 i64 来避免中间计算溢出
        
        while x != 0 {
            result = result * 10 + (x % 10) as i64;
            x /= 10;
        }
        
        // 检查结果是否在 i32 范围内
        if result > i32::MAX as i64 || result < i32::MIN as i64 {
            return 0;
        }
        
        result as i32
    }
}