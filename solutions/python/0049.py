from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        字母异位词分组 - 哈希表 + 字符计数（优化版）
        
        时间复杂度: O(n * k)，其中 n 是字符串数组长度，k 是字符串的最大长度
          - 遍历 n 个字符串，每个字符串需要 O(k) 时间统计字符
          - 相比排序方案的 O(n * k * log k)，去掉了 log k 因子
        空间复杂度: O(n * k)，用于存储哈希表和结果
        
        思路:
        1. 字母异位词的特征：包含相同的字母及其出现次数，只是顺序不同
        2. 使用字符计数代替排序：统计每个字符出现的次数，生成唯一键
        3. 由于只包含小写字母，使用固定大小的计数数组（26个元素）
        4. 将计数数组转为元组作为字典的键（元组可哈希，比字符串更高效）
        5. 最后将字典的所有值（分组）转为列表返回
        
        优化点:
        - 避免了排序操作（O(k log k) → O(k)）
        - 使用固定大小的计数数组，空间开销固定为 O(26) = O(1)
        - 使用元组作为键，比字符串更高效（无需字符串拼接）
        
        示例:
        - "eat" → (1,0,0,0,1,0,...,1,0,...)
        - "tea" → (1,0,0,0,1,0,...,1,0,...)
        - "ate" → (1,0,0,0,1,0,...,1,0,...)
        - 它们生成相同的键，被分到同一组
        """
        # 使用 defaultdict 存储分组，键是字符计数的元组，值是该组的字符串列表
        # defaultdict 可以自动创建空列表，简化代码
        groups = defaultdict(list)
        
        for s in strs:
            # 统计每个字符出现的次数（26个小写字母）
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            # 将计数列表转为元组作为键（元组可哈希，可直接作为字典键）
            # 使用元组比字符串更高效，无需字符串拼接操作
            key = tuple(count)
            
            # 添加到对应分组
            groups[key].append(s)
        
        # 将所有分组转为列表返回
        return list(groups.values())