func divide(dividend int, divisor int) int {
    // 处理特殊情况：-2^31 / -1 = 2^31，会溢出
    if dividend == -2147483648 && divisor == -1 {
        return 2147483647
    }
    
    // 确定结果的符号
    negative := (dividend < 0) != (divisor < 0)
    
    // 转为正数处理，避免负数运算的复杂性
    if dividend < 0 {
        dividend = -dividend
    }
    if divisor < 0 {
        divisor = -divisor
    }
    
    result := 0
    
    // 使用位运算优化：通过左移快速计算 2^k * divisor
    for dividend >= divisor {
        temp := divisor
        multiple := 1
        
        // 找到最大的k使得 divisor * 2^k <= dividend
        // 使用左移代替乘法，避免溢出
        for dividend >= (temp << 1) && (temp << 1) > 0 {
            temp <<= 1
            multiple <<= 1
        }
        
        dividend -= temp
        result += multiple
    }
    
    // 根据符号返回结果
    if negative {
        result = -result
    }
    
    return result
}
