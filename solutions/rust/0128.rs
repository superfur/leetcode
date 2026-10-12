use std::collections::HashSet;

impl Solution {
    /// 128. 最长连续序列
    /// 哈希集合去重，只从「序列起点」（x - 1 不在集合里）出发往后数 x+1, x+2, ...，
    /// 每个数最多被数一次，所以整体 O(n)。
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        let set: HashSet<i32> = nums.into_iter().collect();
        let mut best = 0;
        for &x in &set {
            if set.contains(&(x - 1)) {
                continue;
            }
            let mut end = x;
            while set.contains(&(end + 1)) {
                end += 1;
            }
            best = best.max(end - x + 1);
        }
        best
    }
}
