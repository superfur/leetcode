import java.util.*;

class Solution {
    /**
     * 合并区间
     *
     * 时间复杂度: O(n log n)，其中 n 为区间数量
     *   - 主要耗时在对区间按起点排序
     * 空间复杂度: O(n)，用于存储结果数组
     *
     * 思路:
     * 1. 先按每个区间的起点从小到大排序
     * 2. 遍历排序后的区间数组，用一个列表保存合并后的区间
     * 3. 对于当前区间 curr:
     *    - 如果结果列表为空，或 curr 的起点 > 结果列表最后一个区间的终点，说明没有重叠，直接加入结果
     *    - 否则存在重叠，更新最后一个区间的终点为 max(原终点, curr 的终点)
     * 4. 遍历结束后，将列表转换为二维数组返回
     *
     * 示例:
     * intervals = [[1,3],[2,6],[8,10],[15,18]]
     * 排序后: [[1,3],[2,6],[8,10],[15,18]]
     * 合并过程:
     *   - 结果: [[1,3]]
     *   - curr=[2,6] 与 [1,3] 重叠，合并为 [1,6]
     *   - curr=[8,10] 与 [1,6] 不重叠，加入 => [[1,6],[8,10]]
     *   - curr=[15,18] 与 [8,10] 不重叠，加入 => [[1,6],[8,10],[15,18]]
     */
    public int[][] merge(int[][] intervals) {
        if (intervals == null || intervals.length == 0) {
            return new int[0][];
        }

        // 按起点从小到大排序
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));

        List<int[]> result = new ArrayList<>();
        // 初始化为第一个区间的拷贝，避免直接引用原数组被后续修改影响
        int[] current = Arrays.copyOf(intervals[0], 2);

        for (int i = 1; i < intervals.length; i++) {
            int start = intervals[i][0];
            int end = intervals[i][1];
            int curStart = current[0];
            int curEnd = current[1];

            // 没有重叠，推入当前区间，并开始新的区间
            if (start > curEnd) {
                result.add(current);
                current = new int[]{start, end};
            } else {
                // 有重叠，更新当前区间的结束位置
                current[1] = Math.max(curEnd, end);
            }
        }

        // 别忘了最后一个区间
        result.add(current);

        // 将列表转换为二维数组返回
        return result.toArray(new int[result.size()][]);
    }
}