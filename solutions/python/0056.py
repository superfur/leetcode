from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        合并区间
        
        时间复杂度: O(n log n)，其中 n 为区间数量
          - 主要耗时在对区间按起点排序
        空间复杂度: O(n)，用于存储结果数组
        
        思路:
        1. 先按每个区间的起点从小到大排序
        2. 遍历排序后的区间数组，用一个结果数组保存合并后的区间
        3. 对于当前区间 curr:
           - 如果结果数组为空，或 curr 的起点 > 结果数组最后一个区间的终点，说明没有重叠，直接加入结果
           - 否则存在重叠，更新最后一个区间的终点为 max(原终点, curr 的终点)
        4. 遍历结束后，结果数组即为合并后的不重叠区间集合
        
        示例:
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        排序后: [[1,3],[2,6],[8,10],[15,18]]
        合并过程:
          - 结果: [[1,3]]
          - curr=[2,6] 与 [1,3] 重叠，合并为 [1,6]
          - curr=[8,10] 与 [1,6] 不重叠，加入 => [[1,6],[8,10]]
          - curr=[15,18] 与 [8,10] 不重叠，加入 => [[1,6],[8,10],[15,18]]
        """
        if not intervals:
            return []
        
        # 按起点从小到大排序
        intervals.sort(key=lambda x: x[0])
        
        result = []
        # 初始化为第一个区间
        current = intervals[0][:]
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            cur_start, cur_end = current
            
            # 没有重叠，推入当前区间，并开始新的区间
            if start > cur_end:
                result.append(current)
                current = [start, end]
            else:
                # 有重叠，更新当前区间的结束位置
                current[1] = max(cur_end, end)
        
        # 别忘了最后一个区间
        result.append(current)
        
        return result