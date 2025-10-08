func countAndSay(n int) string {
    // 外观数列：递归应用行程长度编码（RLE）
    // 算法：从"1"开始，每次迭代对前一个结果进行RLE编码
    // 例如：
    // n=1: "1"
    // n=2: "11" (一个1)
    // n=3: "21" (两个1)
    // n=4: "1211" (一个2，一个1)
    // n=5: "111221" (一个1，一个2，两个1)
    
    // 基础情况
    if n == 1 {
        return "1"
    }
    
    // 从"1"开始迭代
    result := "1"
    
    // 迭代n-1次，每次对当前结果进行RLE编码
    for i := 2; i <= n; i++ {
        result = runLengthEncode(result)
    }
    
    return result
}

// runLengthEncode 对字符串进行行程长度编码
// 例如："111221" -> "312211" (三个1，两个2，一个1)
func runLengthEncode(s string) string {
    if len(s) == 0 {
        return ""
    }
    
    var builder strings.Builder
    builder.Grow(len(s) * 2) // 预分配空间，避免多次扩容
    
    i := 0
    for i < len(s) {
        // 当前字符
        char := s[i]
        count := 1
        
        // 统计连续相同字符的数量
        for i+1 < len(s) && s[i+1] == char {
            count++
            i++
        }
        
        // 写入：计数 + 字符
        builder.WriteString(strconv.Itoa(count))
        builder.WriteByte(char)
        
        i++
    }
    
    return builder.String()
}