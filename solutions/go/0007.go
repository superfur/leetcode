package main

func reverse(x int) int {
    // 使用 int64 来避免中间计算溢出
    var result int64 = 0
    
    for x != 0 {
        result = result*10 + int64(x%10)
        x /= 10
    }
    
    // 检查结果是否在 int32 范围内
    if result > 1<<31-1 || result < -1<<31 {
        return 0
    }
    
    return int(result)
}
