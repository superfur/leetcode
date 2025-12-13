func myPow(x float64, n int) float64 {
	/*
	 * Pow(x, n) - 快速幂算法（二分法）
	 * 
	 * 时间复杂度: O(log n)
	 *   - 每次递归将指数减半，递归深度为 O(log n)
	 *   - 相比朴素方法 O(n)，大幅提升效率
	 * 空间复杂度: O(log n)，递归调用栈的深度
	 * 
	 * 思路:
	 * 1. 处理负数指数：如果 n < 0，转换为正数处理，最后取倒数
	 * 2. 使用快速幂（二分法）：
	 *    - 如果 n 是偶数：x^n = (x^(n/2))^2
	 *    - 如果 n 是奇数：x^n = x * (x^(n/2))^2
	 * 3. 递归实现，避免重复计算
	 * 
	 * 示例:
	 * - pow(2, 10) = pow(2, 5)^2 = (2 * pow(2, 2)^2)^2
	 * - pow(2, -2) = 1 / pow(2, 2) = 1 / 4 = 0.25
	 */
	
	// 处理负数指数：转换为正数，最后取倒数
	if n < 0 {
		return 1.0 / fastPow(x, -n)
	}
	return fastPow(x, n)
}

// fastPow 使用快速幂算法计算 x 的 n 次幂（n >= 0）
func fastPow(x float64, n int) float64 {
	// 边界情况
	if n == 0 {
		return 1.0
	}
	if n == 1 {
		return x
	}
	
	// 递归计算 x^(n/2)
	half := fastPow(x, n/2)
	
	// 如果 n 是偶数：x^n = (x^(n/2))^2
	// 如果 n 是奇数：x^n = x * (x^(n/2))^2
	if n%2 == 0 {
		return half * half
	}
	return half * half * x
}