class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        字符串乘法 - 模拟手工乘法过程
        
        时间复杂度: O(m * n)，其中 m 和 n 分别是两个字符串的长度
        空间复杂度: O(m + n)，用于存储结果
        
        思路:
        1. 两个数相乘，结果最多是 m + n 位
        2. num1[i] * num2[j] 的结果会累加到 result[i+j] 和 result[i+j+1]
        3. 从右向左遍历，模拟竖式乘法，处理进位
        
        示例: "123" * "456"
              1 2 3
          ×     4 5 6
          -----------
              7 3 8  (123 * 6)
            6 1 5    (123 * 5, 左移一位)
          4 9 2      (123 * 4, 左移两位)
          -----------
          5 6 0 8 8
        """
        # 特殊情况处理
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        # 结果最多 m + n 位
        result = [0] * (m + n)
        
        # 从右向左遍历两个字符串
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # 计算当前位的乘积
                mul = int(num1[i]) * int(num2[j])
                
                # 确定乘积在结果数组中的位置
                p1, p2 = i + j, i + j + 1
                
                # 加上当前位置已有的值（之前计算累加的结果）
                sum_val = mul + result[p2]
                
                # 更新当前位（取个位）
                result[p2] = sum_val % 10
                # 处理进位（加到高位）
                result[p1] += sum_val // 10
        
        # 将结果数组转换为字符串
        # 跳过前导零
        result_str = ''.join(map(str, result))
        return result_str.lstrip('0') or '0'