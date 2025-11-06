function multiply(num1: string, num2: string): string {
    /**
     * 字符串乘法 - 模拟手工乘法过程
     * 
     * 时间复杂度: O(m * n)，其中 m 和 n 分别是两个字符串的长度
     * 空间复杂度: O(m + n)，用于存储结果
     * 
     * 思路:
     * 1. 两个数相乘，结果最多是 m + n 位
     * 2. num1[i] * num2[j] 的结果会累加到 result[i+j] 和 result[i+j+1]
     * 3. 从右向左遍历，模拟竖式乘法，处理进位
     * 
     * 示例: "123" * "456"
     *       1 2 3
     *   ×     4 5 6
     *   -----------
     *       7 3 8  (123 * 6)
     *     6 1 5    (123 * 5, 左移一位)
     *   4 9 2      (123 * 4, 左移两位)
     *   -----------
     *   5 6 0 8 8
     */
    
    // 特殊情况处理
    if (num1 === "0" || num2 === "0") {
        return "0";
    }
    
    const m: number = num1.length;
    const n: number = num2.length;
    
    // 结果数组，最多 m + n 位
    const result: number[] = new Array(m + n).fill(0);
    
    // 从右向左遍历两个字符串
    for (let i = m - 1; i >= 0; i--) {
        for (let j = n - 1; j >= 0; j--) {
            // 将字符转换为数字
            const digit1: number = parseInt(num1[i]);
            const digit2: number = parseInt(num2[j]);
            
            // 计算当前位的乘积
            const mul: number = digit1 * digit2;
            
            // 确定乘积在结果数组中的位置
            const p1: number = i + j;
            const p2: number = i + j + 1;
            
            // 加上当前位置已有的值（之前计算累加的结果）
            const sum: number = mul + result[p2];
            
            // 更新当前位（取个位）
            result[p2] = sum % 10;
            // 处理进位（加到高位）
            result[p1] += Math.floor(sum / 10);
        }
    }
    
    // 将结果数组转换为字符串，并移除前导零
    const resultStr: string = result.join('');
    return resultStr.replace(/^0+/, '') || '0';
};