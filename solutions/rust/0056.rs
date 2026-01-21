impl Solution {
    pub fn merge(intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        /*
         * 合并区间
         *
         * 时间复杂度: O(n log n)，其中 n 为区间数量（排序耗时）
         * 空间复杂度: O(n)，用于结果存储（原地排序）
         *
         * 思路:
         * 1. 按区间起点排序
         * 2. 线性扫描，用 current 表示当前合并区间
         *    - 若下一个区间的起点 > current 终点，则无重叠：推入结果，重置 current
         *    - 否则有重叠：更新 current 终点 = max(current 终点, 下个终点)
         * 3. 扫描结束推入最后的 current
         */
        let mut intervals = intervals;
        if intervals.is_empty() {
            return Vec::new();
        }

        // 按起点排序
        intervals.sort_by_key(|itv| itv[0]);

        let mut result: Vec<Vec<i32>> = Vec::new();
        let mut current = intervals[0].clone(); // [start, end]

        for itv in intervals.into_iter().skip(1) {
            let start = itv[0];
            let end = itv[1];
            let cur_end = current[1];

            if start > cur_end {
                // 不重叠，先保存 current，再开始新的区间
                result.push(current);
                current = vec![start, end];
            } else {
                // 重叠，扩展 current 的终点
                current[1] = cur_end.max(end);
            }
        }

        // 推入最后一个合并后的区间
        result.push(current);

        result
    }
}