impl Solution {
    pub fn multiply(num1: String, num2: String) -> String {
        /*
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
        if num1 == "0" || num2 == "0" {
            return "0".to_string();
        }
        
        let m = num1.len();
        let n = num2.len();
        
        // 将字符串转换为字节数组，方便索引操作
        let num1_bytes = num1.as_bytes();
        let num2_bytes = num2.as_bytes();
        
        // 结果数组，最多 m + n 位
        let mut result = vec![0u8; m + n];
        
        // 从右向左遍历两个字符串
        for i in (0..m).rev() {
            for j in (0..n).rev() {
                // 将字符转换为数字 (ASCII '0' = 48)
                let digit1 = (num1_bytes[i] - b'0') as u32;
                let digit2 = (num2_bytes[j] - b'0') as u32;
                
                // 计算当前位的乘积
                let mul = digit1 * digit2;
                
                // 确定乘积在结果数组中的位置
                let p1 = i + j;
                let p2 = i + j + 1;
                
                // 加上当前位置已有的值（之前计算累加的结果）
                let sum = mul + result[p2] as u32;
                
                // 更新当前位（取个位）
                result[p2] = (sum % 10) as u8;
                // 处理进位（加到高位）
                result[p1] += (sum / 10) as u8;
            }
        }
        
        // 将结果数组转换为字符串
        let result_str: String = result
            .iter()
            .map(|&digit| (digit + b'0') as char)
            .collect();
        
        // 移除前导零
        result_str.trim_start_matches('0')
            .to_string()
            .if_empty(|| "0".to_string())
    }
}

// 辅助 trait，用于处理空字符串情况
trait IfEmpty {
    fn if_empty<F: FnOnce() -> Self>(self, f: F) -> Self;
}

impl IfEmpty for String {
    fn if_empty<F: FnOnce() -> Self>(self, f: F) -> Self {
        if self.is_empty() {
            f()
        } else {
            self
        }
    }
}