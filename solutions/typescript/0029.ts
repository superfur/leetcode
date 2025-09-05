function divide(dividend: number, divisor: number): number {
    // 处理特殊情况：-2^31 / -1 = 2^31，会溢出
    if (dividend === -2147483648 && divisor === -1) {
        return 2147483647;
    }
    
    // 确定结果的符号
    const negative = (dividend < 0) !== (divisor < 0);
    
    // 转为正数处理，避免负数运算的复杂性
    dividend = Math.abs(dividend);
    divisor = Math.abs(divisor);
    
    let result = 0;
    
    // 使用位运算优化：通过左移快速计算 2^k * divisor
    while (dividend >= divisor) {
        let temp = divisor;
        let multiple = 1;
        
        // 找到最大的k使得 divisor * 2^k <= dividend
        // 添加溢出检查，防止无限循环
        while (dividend >= (temp << 1) && (temp << 1) > 0 && (temp << 1) <= dividend) {
            temp <<= 1;
            multiple <<= 1;
        }
        
        dividend -= temp;
        result += multiple;
    }
    
    // 根据符号返回结果
    result = negative ? -result : result;
    
    // 检查结果是否超出32位整数范围
    if (result > 2147483647) {
        return 2147483647;
    }
    if (result < -2147483648) {
        return -2147483648;
    }
    
    return result;
}