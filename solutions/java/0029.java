class Solution {
    public int divide(int dividend, int divisor) {
        // 处理特殊情况：-2^31 / -1 = 2^31，会溢出
        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }
        
        // 确定结果的符号
        boolean negative = (dividend < 0) != (divisor < 0);
        
        // 使用long类型避免溢出，特别是处理Integer.MIN_VALUE的情况
        long ldividend = Math.abs((long) dividend);
        long ldivisor = Math.abs((long) divisor);
        
        long result = 0;
        
        // 使用位运算优化：通过左移快速计算 2^k * divisor
        while (ldividend >= ldivisor) {
            long temp = ldivisor;
            long multiple = 1;
            
            // 找到最大的k使得 divisor * 2^k <= dividend
            // 使用左移代替乘法，避免溢出
            while (ldividend >= (temp << 1)) {
                temp <<= 1;
                multiple <<= 1;
            }
            
            ldividend -= temp;
            result += multiple;
        }
        
        // 根据符号返回结果，确保结果在int范围内
        result = negative ? -result : result;
        
        // 检查结果是否超出int范围
        if (result > Integer.MAX_VALUE) {
            return Integer.MAX_VALUE;
        }
        if (result < Integer.MIN_VALUE) {
            return Integer.MIN_VALUE;
        }
        
        return (int) result;
    }
}