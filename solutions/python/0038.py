class Solution:
    def countAndSay(self, n: int) -> str:
        """
        外观数列：递归应用行程长度编码（RLE）
        算法：从"1"开始，每次迭代对前一个结果进行RLE编码
        例如：
        n=1: "1"
        n=2: "11" (一个1)
        n=3: "21" (两个1)
        n=4: "1211" (一个2，一个1)
        n=5: "111221" (一个1，一个2，两个1)
        
        时间复杂度：O(n * L)，其中L是当前字符串的长度
        空间复杂度：O(L)，用于存储结果字符串
        """
        # 基础情况
        if n == 1:
            return "1"
        
        # 从"1"开始迭代
        result = "1"
        
        # 迭代n-1次，每次对当前结果进行RLE编码
        for _ in range(2, n + 1):
            result = self._run_length_encode(result)
        
        return result
    
    def _run_length_encode(self, s: str) -> str:
        """
        对字符串进行行程长度编码
        例如："111221" -> "312211" (三个1，两个2，一个1)
        """
        if not s:
            return ""
        
        # 使用列表收集结果，最后join，性能更好
        result = []
        i = 0
        
        while i < len(s):
            # 当前字符
            current_char = s[i]
            count = 1
            
            # 统计连续相同字符的数量
            while i + 1 < len(s) and s[i + 1] == current_char:
                count += 1
                i += 1
            
            # 写入：计数 + 字符
            result.append(str(count))
            result.append(current_char)
            
            i += 1
        
        return ''.join(result)