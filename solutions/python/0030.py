from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        找到字符串s中所有串联子串的起始位置
        
        思路：
        1. 使用滑动窗口遍历字符串s
        2. 对于每个窗口，检查是否包含words中的所有字符串
        3. 使用哈希表记录words中每个字符串的出现次数
        4. 维护当前窗口中的字符串计数
        
        时间复杂度：O(n * m)，其中n是s的长度，m是words的长度
        空间复杂度：O(m)
        """
        # 边界情况处理
        if not s or not words or not words[0]:
            return []
        
        word_len = len(words[0])  # 每个单词的长度
        word_count = len(words)   # 单词数量
        total_len = word_len * word_count  # 目标子串的总长度
        
        # 如果s长度小于目标长度，直接返回空数组
        if len(s) < total_len:
            return []
        
        # 统计words中每个字符串的出现次数
        word_freq = Counter(words)
        result = []
        
        # 只需要检查前word_len个起始位置
        # 因为后续位置会被前面的滑动窗口覆盖
        for i in range(word_len):
            left = i
            right = i
            current_freq = Counter()  # 当前窗口中的字符串计数
            
            # 滑动窗口遍历
            while right + word_len <= len(s):
                # 获取当前单词
                current_word = s[right:right + word_len]
                right += word_len
                
                # 如果当前单词不在words中，重置窗口
                if current_word not in word_freq:
                    current_freq.clear()
                    left = right
                else:
                    current_freq[current_word] += 1
                    
                    # 如果当前单词出现次数超过words中的次数，移动左边界
                    while current_freq[current_word] > word_freq[current_word]:
                        left_word = s[left:left + word_len]
                        current_freq[left_word] -= 1
                        left += word_len
                    
                    # 如果窗口大小等于words的总长度，找到一个有效子串
                    if right - left == total_len:
                        result.append(left)
        
        return result
