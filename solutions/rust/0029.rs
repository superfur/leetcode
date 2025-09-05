impl Solution {
    pub fn divide(dividend: i32, divisor: i32) -> i32 {
        // 处理特殊情况：-2^31 / -1 = 2^31，会溢出
        if dividend == i32::MIN && divisor == -1 {
            return i32::MAX;
        }
        
        // 确定结果的符号
        let negative = (dividend < 0) != (divisor < 0);
        
        // 转为正数处理，避免负数运算的复杂性
        // 使用i64来避免溢出，特别是处理i32::MIN的情况
        let mut ldividend = (dividend as i64).abs();
        let ldivisor = (divisor as i64).abs();
        
        let mut result = 0i64;
        
        // 使用位运算优化：通过左移快速计算 2^k * divisor
        while ldividend >= ldivisor {
            let mut temp = ldivisor;
            let mut multiple = 1i64;
            
            // 找到最大的k使得 divisor * 2^k <= dividend
            // 使用左移代替乘法，避免溢出
            while ldividend >= (temp << 1) {
                temp <<= 1;
                multiple <<= 1;
            }
            
            ldividend -= temp;
            result += multiple;
        }
        
        // 根据符号返回结果
        if negative {
            result = -result;
        }
        
        // 检查结果是否超出i32范围
        if result > i32::MAX as i64 {
            return i32::MAX;
        }
        if result < i32::MIN as i64 {
            return i32::MIN;
        }
        
        result as i32
    }
}