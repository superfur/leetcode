class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 处理特殊情况：-2^31 / -1 = 2^31，会溢出
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # 确定结果的符号
        negative = (dividend < 0) != (divisor < 0)
        
        # 转为正数处理，避免负数运算的复杂性
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        result = 0
        
        # 使用位运算优化：通过左移快速计算 2^k * divisor
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            
            # 找到最大的k使得 divisor * 2^k <= dividend
            # 使用左移代替乘法，避免溢出
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            dividend -= temp
            result += multiple
        
        # 根据符号返回结果
        result = -result if negative else result
        
        # 检查结果是否超出32位整数范围
        if result > 2**31 - 1:
            return 2**31 - 1
        if result < -2**31:
            return -2**31
        
        return result
