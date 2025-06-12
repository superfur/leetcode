struct Solution;

impl Solution {
    fn my_atoi(s: String) -> i32 {
        let s = s.trim();
        if s.is_empty() {
            return 0;
        }
        
        let mut chars = s.chars().peekable();
        let mut sign = 1;
        
        // 处理符号
        if let Some(&c) = chars.peek() {
            if c == '+' || c == '-' {
                sign = if c == '-' { -1 } else { 1 };
                chars.next();
            }
        }
        
        let mut result = 0;
        while let Some(&c) = chars.peek() {
            if !c.is_digit(10) {
                break;
            }
            
            let digit = c.to_digit(10).unwrap() as i32;
            if result > i32::MAX / 10 || (result == i32::MAX / 10 && digit > i32::MAX % 10) {
                return if sign == 1 { i32::MAX } else { i32::MIN };
            }
            
            result = result * 10 + digit;
            chars.next();
        }
        
        result * sign
    }
}