function reverse(x: number): number {
    const MAX_INT = Math.pow(2, 31) - 1;
    const MIN_INT = -Math.pow(2, 31);
    
    const isNegative = x < 0;
    const reversed = parseInt(Math.abs(x).toString().split("").reverse().join(""));
    const result = isNegative ? -reversed : reversed;
    
    // 检查结果是否在有效范围内
    if (result > MAX_INT || result < MIN_INT) {
        return 0;
    }
    
    return result;
}
