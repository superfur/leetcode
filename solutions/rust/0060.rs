impl Solution {
    /*
     * 排列序列 / Permutation Sequence
     *
     * 返回由数字 1..n 组成的所有排列中，按字典序排序后的第 k 个排列（1-indexed）。
     *
     * 时间复杂度: O(n^2)
     *   - 每一位选择时需要从数组中移除一个元素，remove 是 O(n)
     * 空间复杂度: O(n)
     *   - 需要存储阶乘数组和候选数字
     */
    pub fn get_permutation(n: i32, k: i32) -> String {
        if n <= 0 || k <= 0 {
            return String::new();
        }

        let n_usize = n as usize;

        // 计算阶乘数组 fact[i] = i!
        let mut fact: Vec<i64> = vec![1; n_usize + 1];
        for i in 1..=n_usize {
            fact[i] = fact[i - 1] * i as i64;
        }

        if (k as i64) > fact[n_usize] {
            return String::new();
        }

        // 候选数字 1..n
        let mut nums: Vec<i32> = (1..=n).collect();

        // 将 k 转为 0-index
        let mut k0: i64 = (k - 1) as i64;
        let mut result = String::with_capacity(n_usize);

        for i in (1..=n_usize).rev() {
            let f = fact[i - 1];
            let idx = (k0 / f) as usize;
            let val = nums.remove(idx);
            result.push_str(&val.to_string());
            k0 %= f;
        }

        result
    }

    /// 中文包装方法，保持与其它语言版本一致
    pub fn 排列序列(n: i32, k: i32) -> String {
        Self::get_permutation(n, k)
    }
}
