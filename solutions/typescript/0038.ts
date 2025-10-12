/**
 * 外观数列：递归应用行程长度编码（RLE）
 * 算法：从"1"开始，每次迭代对前一个结果进行RLE编码
 * 
 * 例如：
 * n=1: "1"
 * n=2: "11" (一个1)
 * n=3: "21" (两个1)
 * n=4: "1211" (一个2，一个1)
 * n=5: "111221" (一个1，一个2，两个1)
 * 
 * 时间复杂度：O(n * L)，其中L是当前字符串的长度
 * 空间复杂度：O(L)，用于存储结果字符串
 * 
 * @param n - 第n项
 * @returns 外观数列的第n项
 */
function countAndSay(n: number): string {
    // 基础情况
    if (n === 1) {
        return "1";
    }
    
    // 从"1"开始迭代
    let result = "1";
    
    // 迭代n-1次，每次对当前结果进行RLE编码
    for (let i = 2; i <= n; i++) {
        result = runLengthEncode(result);
    }
    
    return result;
}

/**
 * 对字符串进行行程长度编码
 * 例如："111221" -> "312211" (三个1，两个2，一个1)
 * 
 * @param s - 待编码的字符串
 * @returns 编码后的字符串
 */
function runLengthEncode(s: string): string {
    if (!s) {
        return "";
    }
    
    // 使用数组收集结果，最后join，性能更好
    const result: string[] = [];
    let i = 0;
    
    while (i < s.length) {
        // 当前字符
        const currentChar = s[i];
        let count = 1;
        
        // 统计连续相同字符的数量
        while (i + 1 < s.length && s[i + 1] === currentChar) {
            count++;
            i++;
        }
        
        // 写入：计数 + 字符
        result.push(count.toString(), currentChar);
        
        i++;
    }
    
    return result.join("");
}