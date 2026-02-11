package main

import (
    "fmt"
    "strings"
)

// 排列序列: 返回字典序第 k 个由 1..n 组成的排列（1-indexed）
func 排列序列(n int, k int) string {
    if n <= 0 || k <= 0 {
        return ""
    }
    // 计算阶乘
    fact := make([]int, n+1)
    fact[0] = 1
    for i := 1; i <= n; i++ {
        fact[i] = fact[i-1] * i
    }
    if k > fact[n] {
        return ""
    }

    nums := make([]int, n)
    for i := 0; i < n; i++ {
        nums[i] = i + 1
    }

    k-- // 转为 0-index
    var sb strings.Builder
    for i := n; i >= 1; i-- {
        f := fact[i-1]
        idx := k / f
        sb.WriteString(fmt.Sprintf("%d", nums[idx]))
        // 从 nums 中移除已选元素
        nums = append(nums[:idx], nums[idx+1:]...)
        k = k % f
    }

    return sb.String()
}

// getPermutation 是对外使用的函数名（与题目示例一致）
func getPermutation(n int, k int) string {
    return 排列序列(n, k)
}
