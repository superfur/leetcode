impl Solution {
    /*
     * Pow(x, n) - 快速幂算法（迭代版）
     * 
     * 时间复杂度: O(log n)
     *   - 每次迭代将指数减半，迭代次数为 O(log n)
     *   - 相比朴素方法 O(n)，大幅提升效率
     * 空间复杂度: O(1)，只使用常数额外空间
     *   - 相比递归实现的 O(log n) 空间，迭代版本更优
     * 
     * 思路:
     * 1. 处理负数指数：如果 n < 0，转换为正数处理，最后取倒数
     * 2. 使用快速幂（迭代法）：
     *    - 将指数 n 转为二进制表示
     *    - 从低位到高位遍历每一位
     *    - 如果当前位为 1，则将当前累积结果乘入结果
     *    - 每次迭代将底数平方，指数右移一位
     * 3. 迭代实现，避免递归栈开销
     * 
     * 示例:
     * - pow(2, 10): 10 = 1010(二进制)
     *   - 第0位(0): result = 1, base = 2^2 = 4
     *   - 第1位(1): result = 1 * 4 = 4, base = 4^2 = 16
     *   - 第2位(0): result = 4, base = 16^2 = 256
     *   - 第3位(1): result = 4 * 256 = 1024
     * - pow(2, -2) = 1 / pow(2, 2) = 1 / 4 = 0.25
     */
    pub fn my_pow(x: f64, n: i32) -> f64 {
        // 处理 i32::MIN 的特殊情况：直接取反会溢出
        // 使用 i64 避免溢出
        let n_long = n as i64;
        let mut exp = if n_long < 0 {
            (-n_long) as u64
        } else {
            n_long as u64
        };
        
        // 边界情况
        if exp == 0 {
            return 1.0;
        }
        
        let mut result = 1.0;
        let mut base = x;
        
        // 迭代计算：将指数转为二进制，逐位处理
        while exp > 0 {
            // 如果当前位为 1，将当前 base 乘入结果
            if exp & 1 == 1 {
                result *= base;
            }
            // base 平方，相当于指数左移一位
            base *= base;
            // 指数右移一位，处理下一位
            exp >>= 1;
        }
        
        // 如果原指数为负数，返回倒数
        if n_long < 0 {
            1.0 / result
        } else {
            result
        }
    }
}