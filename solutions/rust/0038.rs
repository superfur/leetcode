impl Solution {
    /// 外观数列：递归应用行程长度编码（RLE）
    /// 算法：从"1"开始，每次迭代对前一个结果进行RLE编码
    /// 
    /// 例如：
    /// n=1: "1"
    /// n=2: "11" (一个1)
    /// n=3: "21" (两个1)
    /// n=4: "1211" (一个2，一个1)
    /// n=5: "111221" (一个1，一个2，两个1)
    /// 
    /// 时间复杂度：O(n * L)，其中L是当前字符串的长度
    /// 空间复杂度：O(L)，用于存储结果字符串
    pub fn count_and_say(n: i32) -> String {
        // 基础情况
        if n == 1 {
            return String::from("1");
        }
        
        // 从"1"开始迭代
        let mut result = String::from("1");
        
        // 迭代n-1次，每次对当前结果进行RLE编码
        for _ in 2..=n {
            result = Self::run_length_encode(&result);
        }
        
        result
    }
    
    /// 对字符串进行行程长度编码
    /// 例如："111221" -> "312211" (三个1，两个2，一个1)
    fn run_length_encode(s: &str) -> String {
        if s.is_empty() {
            return String::new();
        }
        
        // 预分配容量，避免多次重新分配
        let mut result = String::with_capacity(s.len() * 2);
        
        // 将字符串转换为字符数组进行迭代
        let chars: Vec<char> = s.chars().collect();
        let mut i = 0;
        
        while i < chars.len() {
            // 当前字符
            let current_char = chars[i];
            let mut count = 1;
            
            // 统计连续相同字符的数量
            while i + 1 < chars.len() && chars[i + 1] == current_char {
                count += 1;
                i += 1;
            }
            
            // 写入：计数 + 字符
            result.push_str(&count.to_string());
            result.push(current_char);
            
            i += 1;
        }
        
        result
    }
}