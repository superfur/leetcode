impl Solution {
    /// 137. 只出现一次的数字 II
    /// 逐位统计：出现三次的数，每一位上的 1 的个数一定是 3 的倍数，
    /// 所以把所有数在第 i 位上的 1 加起来对 3 取模，余数就是答案在第 i 位的值。
    /// i32 的右移是算术右移，1 << 31 得到 i32::MIN，所以负数和符号位不需要额外处理。
    /// 时间 O(32n)，空间 O(1)。
    pub fn single_number(nums: Vec<i32>) -> i32 {
        let mut result: i32 = 0;
        for i in 0..32 {
            let ones: i32 = nums.iter().map(|&x| (x >> i) & 1).sum();
            if ones % 3 != 0 {
                result |= 1 << i;
            }
        }
        result
    }
}
