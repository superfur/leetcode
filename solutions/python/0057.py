from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        插入区间
        
        时间复杂度: O(n)，其中 n 为区间数量
          - 只需遍历一次区间数组
        空间复杂度: O(n)，用于存储结果数组
        
        思路:
        1. 遍历 intervals，将所有在 newInterval 之前的区间（end < newInterval[0]）直接加入结果
        2. 找到所有与 newInterval 重叠的区间，合并它们：
           - 更新 newInterval[0] = min(newInterval[0], interval[0])
           - 更新 newInterval[1] = max(newInterval[1], interval[1])
        3. 将合并后的 newInterval 加入结果
        4. 将剩余的区间（start > newInterval[1]）加入结果
        
        判断重叠的条件: interval[0] <= newInterval[1] && interval[1] >= newInterval[0]
        
        示例:
        intervals = [[1,3],[6,9]], newInterval = [2,5]
        过程:
          - [1,3] 与 [2,5] 重叠，合并为 [1,5]
          - [6,9] 在 [1,5] 之后，直接加入
          结果: [[1,5],[6,9]]
        """
        result = []
        i = 0
        n = len(intervals)
        
        # 1. 将所有在 newInterval 之前的区间加入结果
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # 2. 合并所有与 newInterval 重叠的区间
        while i < n and intervals[i][0] <= newInterval[1]:
            # 更新 newInterval 的起点和终点
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        # 3. 将合并后的 newInterval 加入结果
        result.append(newInterval)
        
        # 4. 将剩余的区间加入结果
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result